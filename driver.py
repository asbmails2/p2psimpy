# -*- coding: utf-8 -*-
import random
import simpy

class Driver:

    def __init__(self,network, processor):
        self.buffer_in = simpy.Store(network.env)
        self.network = network
        self.env = network.env
        self.processor = processor
        self.address = None
        self.methods = {
            'on_message': [],
            'on_connect': [],
            'on_disconnect': []
            }

    def connect(self):
        for z in  self.network.register(self):
            yield z
        for z in self.issue_event('on_connect', self.address):
            yield z
        # for z in self.issue_event('on_connect', self.address):
        #     yield z

    def advertise(self, msg):
        self.network.send_broadcast(self.address, msg)

    def recieve (self, msg_envelope):
        print('{} received from {}: {}'.format(
            msg_envelope[1], msg_envelope[0], msg_envelope[2]))

        return self.issue_event('on_message', msg_envelope)

    def send (self, to_addr , msg):
        return self.network.send_unicast(self.address, to_addr, msg)

    def register_handler (self, method, event='on_message'):
        self.methods[event].append(method)

    def process_handler_msgs (self):
        while True:
            yield self.env.timeout(2)
            print(self.buffer_in.get())

    def issue_event (self, event, value=None):
        print('issuing ' + event)
        for handle in  self.methods[event]:
            yield self.env.timeout(1)
            for z in self.processor.process_message(handle, value):
                yield z
