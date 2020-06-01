import logging
from simple_dds import *

"""
Simulates the behavior of a peer in a network.
Uses driver object to interface with the network.

Definir as caracteristicas do nodo basicas - ID , Recursos - Qualidade

Criar um canal broadcast onde o peer precisa se conectar
E criar os links de comunicacao unicast

agente tem (ref de um canal broad)

Resources e uma lista de recursos com a sua qualidade

"""
# -*- coding: utf-8 -*-

class Peer:
    def __init__(self, driver, id):
        self.driver = driver
        self.driver.register_handler(self.on_message)
        self.driver.register_handler(self.on_connect, 'on_connect')
        self.driver.register_handler(self.on_advertise, 'on_advertise')
        self.driver.register_handler(self.on_disconnect, 'on_disconnect')
        self.name = 'peer_{}'.format(id)
        self.latest_read_msg = 0

    def on_message (self, msg):
        logging.info(str(self.driver.env.now) + ' :: ' + '{} received msg: {}'.format(self.name, msg))
        yield None

    def on_connect (self, address):
        logging.info(str(self.driver.env.now) + ' :: ' + '{} connected with address {}'.format(self.name, address))
        for z in self.driver.advertise('Connecting 1, 2, 3'):
            yield z

    def on_disconnect (self):
        self.driver.advertise("Bye World")
    
    def on_advertise (self, msg):
        for z in self.driver.advertise(msg):
            yield z

    # TODO: O nome não é adequado: faz mais do que publicar mensagem, antes cria objetos..
    # .. necessários. É preciso mudar depois.
    def wait_then_publish_message(self, topic_name, message, wait_time=100):
        yield self.driver.env.timeout(wait_time)
        the_service = dds_service.DDS_Service(self.driver)
        participant = domain_participant.Domain_Participant(the_service)
        topic = participant.create_topic(topic_name)
        pub = participant.create_publisher(topic)
        pub.write(message)

    def wait_then_read_message(self, topic_name, message, wait_time=100):
        yield self.driver.env.timeout(wait_time)
        the_service = dds_service.DDS_Service(self.driver)
        participant = domain_participant.Domain_Participant(the_service)
        topic = participant.create_topic(topic_name)
        sub = participant.create_subscriber(topic)
        # Atenção à linha a seguir. Talvez seja necessário alterar o valor mais tarde.
        yield self.driver.env.timeout(17)  # Tempo para recebimento de mensagens de outros peers contendo dados do domínio.
        self.latest_read_msg = sub.read()

    def dds_read_test (self):
        yield self.driver.env.timeout(150)
        print("read test")
        the_service = dds_service.DDS_Service(self.driver)
        participant = domain_participant.Domain_Participant(the_service)
        n_topic = participant.create_topic("TEST")
        sub = participant.create_subscriber(n_topic)
        yield self.driver.env.timeout(17)
        stuff = sub.read()
        print(str(self.driver.env.now) + ':: ' + str(stuff))

    def read_new_message(self, subscriber):
        self.latest_read_msg = subscriber.read()
        

        
