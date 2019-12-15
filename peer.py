"""
Class peer for create all the base stack for peer

Definir as caracteristicas do nodo basicas - ID , Recursos - Qualidade

riar um canal broadcast onde o peer precisa se conectar
E criar os links de comunicacao unicast

agente tem (ref de um canal broad)

Resources e uma lista de recursos com a sua qualidade

"""
# -*- coding: utf-8 -*-

class Peer:
    def __init__(self, driver):
        self.driver = driver
        self.driver.register_handler(self.handle_msgs)
        self.driver.register_handler(self.on_connect, 'on_connect')
        self.driver.register_handler(self.on_disconnect, 'on_disconnect')
        self.name = None

    def handle_msgs (self, msg):
        print ('peer received msg: {}'.format(msg))

    def on_connect (self, address):
        print('Peer connection success. Address {}'.format(address))
        self.name = 'Node {}'.format(address)
        #self.driver.advertise("Hello World")

        for z in self.driver.send(1, 'hello'):
            yield z
        for z in self.driver.send(address -1 , 'hello'):
            yield z

    def on_disconnect (self):
        self.driver.advertise("Bye World")








