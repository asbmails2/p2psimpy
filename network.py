# -*- coding: utf-8 -*-
import simpy


class Network:

    next_avaible_address = 1

    def __init__(self, env, latency):
        self.channel = simpy.Resource(env)
        self.env = env
        self.timeout = env.timeout
        self.latency = latency
        self.node_map = {}

    def register(self, node_driver):
        with self.channel.request() as rec:
            yield rec
            curr_address = self.next_avaible_address
            self.next_avaible_address += 1
            print('connecting {}'.format(curr_address))

            self.node_map[curr_address] = node_driver
            node_driver.address = curr_address
            yield self.timeout(self.latency)

    def send_unicast(self, from_addr, to_addr, msg):
        print('network sending unicast {} => {}'.format(from_addr, to_addr))
        if(to_addr <= 0):
            print('{} address not found (msg from {})'.format(
                to_addr, from_addr))
            yield self.env.timeout(0)
        else: 
            msg_envelope = [from_addr, to_addr, msg]
            with self.channel.request() as rec:
                yield rec
                node = self.node_map[to_addr]
                if node is not None:
                    for z in node.recieve(msg_envelope):
                        yield z
                    yield self.env.timeout(self.latency)
                else:
                    print('{} address not found (msg from {})'.format(
                        to_addr, from_addr))

    def send_broadcast(self, from_addr, msg):
        print('broadcast')
        msg_envelope = [from_addr, None, msg]
        with self.channel.request() as rec:
            yield rec
            yield self.env.timout(self.latency)
            for to_addr in self.node_map:
                node = self.node_map [to_addr]
                node.recieve(msg_envelope)

