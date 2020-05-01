import logging

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
    def __init__(self, driver, id):
        self.driver = driver
        self.driver.register_handler(self.on_message)
        self.driver.register_handler(self.on_connect, 'on_connect')
        self.driver.register_handler(self.on_advertise, 'on_advertise')
        self.driver.register_handler(self.on_disconnect, 'on_disconnect')
        self.name = 'peer_{}'.format(id)
        # Possivelmente colocar o próximo bloco de código em uma função separada, própria para a configuração do logger, para limpar um pouco
        self.peer_logger = logging.getLogger(__name__)
        self.peer_logger.propagate = False            # Evita que o root logger também receba os handlers, assim evitando registro duplo
        if not self.peer_logger.handlers:             # Garantimos que não estamos readicionando handlers
            self.console_handler = logging.StreamHandler()
            self.console_handler.setLevel(logging.INFO)
            self.log_format = logging.Formatter('[%(levelname)s] [%(name)10s] %(message)s')
            self.console_handler.setFormatter(self.log_format)
            self.peer_logger.addHandler(self.console_handler)

    def on_message (self, msg):
        self.peer_logger.info(str(self.driver.env.now) + ' :: ' + '{} received msg: {}'.format(self.name, msg))
        yield None

    def on_connect (self, address):
        self.peer_logger.info(str(self.driver.env.now) + ' :: ' + '{} connected with address {}'.format(self.name, address))
        for z in self.driver.advertise('Connecting 1, 2, 3'):
            yield z

    def on_disconnect (self):
        self.driver.advertise("Bye World")
    
    def on_advertise (self, msg):
        for z in self.driver.advertise(msg):
            yield z
        








