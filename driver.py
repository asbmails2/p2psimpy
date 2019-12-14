# -*- coding: utf-8 -*-
import random
import simpy

class Driver:

    def __init__(self,network):
        self.buffer_in = simpy.Store(network.env)
        self.network = network
        self.env = network.env
        self.address = 0
        self.methods = {
            'on_message': [],
            'on_connect': [],
            'on_disconnect': []
            }

    def connect(self):
        self.network.register(self)
        self.issue_event('on_connect', self.address)

    def advertise(self, msg):
        self.network.send_broadcast(self.address, msg)

    def recieve (self, msg_envelope):
        self.buffer_in.put(msg_envelope)
        print('<')

    def send (self, to_addr , msg):
        print('>')
        self.network.send_unicast(self.address, to_addr, msg)

    def register_handler (self, method, event='on_message'):
        self.methods[event].append(method)

    def process_handler_msgs (self):
        while True:
            yield self.env.timeout(2)
            print(self.buffer_in.get())

    def test_run (self):
        while True:
            yield self.env.timeout(5)
            self.methods[1]()
            print("Test_Run")

    def issue_event (self, event, value):
        print('issuing ' + event)
        for handle in  self.methods[event]:
            handle(value)
