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
        self.addr_list = []

    def register(self, node_driver):
        with self.channel.request() as rec:
            yield rec
            curr_address = self.next_avaible_address
            self.next_avaible_address += 1
            print('connecting {}'.format(curr_address))

            self.node_map[curr_address] = node_driver
            node_driver.address = curr_address
            self.addr_list.append(curr_address)
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
                if node:
                    node.recieve(msg_envelope)
                    yield self.env.timeout(self.latency)
                    print(msg_envelope)
                else:
                    print('{} address not found (msg from {})'.format(
                        to_addr, from_addr))

    def send_broadcast(self, from_addr, msg):
        print('Message Broadcast from {} - {}'.format(from_addr,msg))
        for to_addr in self.addr_list:
            if(to_addr <= 0):
                print('{} address not found (msg from {})'.format(
                    to_addr, from_addr))
                yield self.env.timeout(0)
            else: 
                msg_envelope2 = [from_addr, to_addr, msg]
                with self.channel.request() as rec:
                    yield rec
                    node = self.node_map[to_addr]
                    if node:
                        node.recieve(msg_envelope2)
                        yield self.env.timeout(self.latency)
                        print('Broadcast:'+ str(msg_envelope2))
                    else:
                        print('{} address not found (msg from {})'.format(
                            to_addr, from_addr))