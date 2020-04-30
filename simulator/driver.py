# -*- coding: utf-8 -*-
import random
import simpy

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
        print(str(self.env.now) + ' :: ' + '{} received from {}: {}'.format(
            msg_envelope[1], msg_envelope[0], msg_envelope[2]))

        event = ['on_message', msg_envelope]
        self.async_events.put(event)

    def send (self, to_addr , msg):
        return self.network.send_unicast(self.address, to_addr, msg)

    def register_handler (self, method, event='on_message'):
        self.methods[event].append(method)

    def issue_event (self, event, value=None):
        print(str(self.env.now) + ' :: ' + 'issuing ' + event)
        for handle in self.methods[event]:
            yield self.env.timeout(1)
            for z in self.processor.process_message(handle, value):
                yield z

    def send_keepalive(self):
            yield self.env.timeout(self.keep_alive_interval)
            self.network.renew(self.address)
