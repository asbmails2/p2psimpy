# -*- coding: utf-8 -*-
import random
import simpy

class Processor:
    def __init__(self, env, latency):
        self.timeout = env.timeout
        self.processor = simpy.Resource(env)
        self.latency = latency

    def process_message(self, method, value):
        print('scheduling process of message')
        with self.processor.request() as rec:
            yield rec
            for z in method(value):
                yield z
            yield self.timeout(self.latency)


