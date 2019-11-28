# -*- coding: utf-8 -*-
import random
import simpy

class Driver:

    def __init__(self,network):
        self.buffer_in = simpy.Store(network.env)
        self.network = network
        self.env = network.env
        self.address = 0
        self.connect()
        self.methods = []

    def connect (self):
        self.network.register(self)

    def recieve (self, msg_envelope):
        self.buffer_in.put(msg_envelope)

    def send (self, to_addr , msg):
        self.network.unicast(self.address, to_addr , msg)

    def advertise (self, msg):
        self.network.broadcast(self.address,msg)

    def register_handler (self, method):
        self.methods.append(method)

    def process_handler_msgs (self):
        while True:
            yield self.env.timeout(2)
            print(self.buffer_in.get())

    def test_run (self):
        while True:
            yield self.env.timeout(5)
            self.methods[1]()
            print("Test_Run")

