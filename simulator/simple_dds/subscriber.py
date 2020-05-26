import logging
from queue import *

from simple_dds import entity

# TODO: Adicionar suporte para chamada de listener (callback).
class Subscriber(entity.Entity):
    
    def __init__(self, participant, topic, data_objects):
        super(Subscriber, self).__init__()
        self.participant = participant
        self.topic = topic
        self.available_data = Queue()
        for element in data_objects:
            self.available_data.put(element)

    def get_topic_name(self):
        return self.topic.get_name()

    def receive_data(self, data_object):
        if data_object.get_topic_name() == self.topic.get_name():
            self.available_data.put(data_object)

    def read(self):
        try:
            data_object = self.available_data.get(block=False)
            return data_object
        except Empty:
            logging.debug('No data objects available')
            return None