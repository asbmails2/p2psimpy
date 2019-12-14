# -*- coding: utf-8 -*-
import simpy


class Network:

    next_avaible_address = 1

    def __init__(self, env, latency):
        self.channel = simpy.Resource(env)
        self.env = env
        self.latency = latency
        self.node_map = {}

    def register(self, node_driver):
        curr_address = self.next_avaible_address
        self.node_map[curr_address] = node_driver
        node_driver.address = curr_address
        self.next_avaible_address += 1

    def unic(self):
        print('unic')

    def send_unicast(self, from_addr, to_addr, msg):
        print('unicast')
        msg_envelope = [from_addr, to_addr, msg]
        with self.channel.request() as rec:
            yield rec
            yield self.env.timout(self.latency)
            node = self.node_map[to_addr]
            node.recieve(msg_envelope)

    def send_broadcast(self, from_addr, msg):
        print('broadcast')
        msg_envelope = [from_addr, None, msg]
        with self.channel.request() as rec:
            yield rec
            yield self.env.timout(self.latency)
            for to_addr in self.node_map:
                node = self.node_map [to_addr]
                node.recieve(msg_envelope)

