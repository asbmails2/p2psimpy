# -*- coding: utf-8 -*-
import random
import simpy
import logging

class Processor:
    def __init__(self, env, id, latency):
        self.timeout = env.timeout
        self.processor = simpy.Resource(env)
        self.latency = latency
        self.name = 'proc_{}'.format(id)
        self.env = env
        # Possivelmente colocar o próximo bloco de código em uma função separada, própria para a configuração do logger, para limpar um pouco
        self.proc_logger = logging.getLogger(__name__)
        self.proc_logger.propagate = False            # Evita que o root logger também receba os handlers, assim evitando registro duplo
        if not self.proc_logger.handlers:             # Garantimos que não estamos readicionando handlers
            self.console_handler = logging.StreamHandler()
            self.console_handler.setLevel(logging.INFO)
            self.log_format = logging.Formatter('[%(levelname)s] [%(name)10s] %(message)s')
            self.console_handler.setFormatter(self.log_format)
            self.proc_logger.addHandler(self.console_handler)

    def process_message(self, method, value):
        self.proc_logger.info(str(self.env.now) + ' :: ' + self.name + ': scheduling process of message')
        with self.processor.request() as rec:
            yield rec
            yield self.timeout(self.latency)
            for z in method(value):
                yield z
            # try:
            #     iter_call = iter(call)
            #     for z in iter_call:
            #         yield z
            # except TypeError as err:
            #     print(err)
                #print('handle method is not iterable')
            


