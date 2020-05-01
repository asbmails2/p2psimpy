# -*- coding: utf-8 -*-
import random
import simpy
import logging

class Driver:

    def __init__(self, network, processor):
        self.async_events = simpy.Store(network.env)
        self.network = network
        self.env = network.env
        self.processor = processor
        self.address = None
        self.methods = {
            'on_message': [],
            'on_connect': [],
            'on_advertise': [],
            'on_disconnect': []
            }
        self.keep_alive_interval = 20
        # Possivelmente colocar o próximo bloco de código em uma função separada, própria para a configuração do logger, para limpar um pouco
        self.driver_logger = logging.getLogger(__name__)
        self.driver_logger.propagate = False            # Evita que o root logger também receba os handlers, assim evitando registro duplo
        if not self.driver_logger.handlers:             # Garantimos que não estamos readicionando handlers
            self.console_handler = logging.StreamHandler()
            self.console_handler.setLevel(logging.INFO)
            self.log_format = logging.Formatter('[%(levelname)s] [%(name)10s] %(message)s')
            self.console_handler.setFormatter(self.log_format)
            self.driver_logger.addHandler(self.console_handler)

    def run(self):
        if self.address is None:
            for z in self.connect():
                yield z
            self.env.process(self.send_keepalive())  # A partir de agora, mandamos um sinal de vida constantemente
                
        while True:
            event = yield self.async_events.get()
            for z in self.issue_event(event[0], event[1]):
                if z:
                    yield z
            for z in self.issue_event(event[0], 'on_advertise'):
                if z:
                    yield z
            
    def connect(self):
        for z in  self.network.register(self):
            yield z
        for z in self.issue_event('on_connect', self.address):
            yield z

    def advertise(self, msg):
        msg = 'ADV-'+str(msg)
        return self.network.send_broadcast(self.address, msg)

    def recieve (self, msg_envelope):
        self.driver_logger.info(str(self.env.now) + ' :: ' + '{} received from {}: {}'.format(
            msg_envelope[1], msg_envelope[0], msg_envelope[2]))       

        event = ['on_message', msg_envelope]
        self.async_events.put(event)

    def send (self, to_addr , msg):
        return self.network.send_unicast(self.address, to_addr, msg)

    def register_handler (self, method, event='on_message'):
        self.methods[event].append(method)

    def issue_event (self, event, value=None):
        self.driver_logger.info(str(self.env.now) + ' :: ' + 'issuing ' + event)
        for handle in self.methods[event]:
            yield self.env.timeout(1)
            for z in self.processor.process_message(handle, value):
                yield z

    def send_keepalive(self):
            yield self.env.timeout(self.keep_alive_interval)
            self.network.renew(self.address)
