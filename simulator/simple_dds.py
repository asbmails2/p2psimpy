import logging

import singleton

# Possíveis problemas de uso mútuo nesta classe? Veremos quando testarmos.
class UniqueHandleController(metaclass=Singleton):

    def __init__(self):
        self.next_available_handle = 0
    
    def generate_handle(self)
        handle = self.next_available_handle
        self.next_available_handle += 1
        return handle

class Entity:

    def __init__(self):
        self.instance_handle = 0
    
    def set_instance_handle(self, handle)
        if self.instance_handle is not 0:
            raise RuntimeError("DDS Instance already has a handle.")
        else
            self.instance_handle = handle

    def get_instance_handle(self):
        if self.instance_handle is 0:
            raise RuntimeError("DDS Instance has not been assigned a handle")
        return self.instance_handle

class DDS_Service(Entity):

    def __init__(self, driver, handle_controller):
        self.handle_controller = handle_controller
        self.instance_handle = self.handle_controller.generate_handle()
        self.driver = driver
        self.handles = {}
        self.participants = {}
        self.topics = {}
        self.data_objects = {}

    def set_instance_handle(self, handle):
        raise RuntimeError("DDS Service's handle cannot be changed.")

    def get_instance_handle(self):
        return self.instance_handle

    def assign_handle(self, entity):
        handle = self.handle_controller.generate_handle()
        entity.set_instance_handle(handle)
        self.handles[handle] = entity
        self.next_available_instance += 1
    
    def add_participant(self, participant):
        self.assign_handle(participant)
        handle = participant.get_instance_handle()
        self.participants[handle] = participant

    def add_topic(self, topic):
        self.assign_handle(topic)
        topic_key = topic.get_name()
        self.topics[topic_key] = topic

    def topic_exists(self, topic_name):
        return topic_name in self.topics

    def run(self):
        # Através do driver, queremos:
        # - Achar participantes
        # - Atualizar instâncias de dados
        # - Enviar dados relevantes aos subscribers
        pass

class Domain_Participant(Entity):

    def __init__(self, dds_service):
        self.service = dds_service
        self.publishers = {}
        self.subscribers = {}
        self.topics = {}
        self.discovered_participants = {}

        self.dds_service.add_participant(self)

    def create_topic(self, topic_name):
        if self.service.topic_exists(topic_name):
            logging.warning(f'{topic_name} already exists.')
        else
            new_topic = Topic(topic_name, self)
            self.service.add_topic(new_topic)
            self.topics.append(new_topic)

    def delete_topic(self, topic):
        # Pré-condição: tópico deve ter sido criado por este participante
        pass

    def find_topic(self, topic_name):
        # Deve retornar um objeto do tipo Topic
        pass

    def create_publisher(self, topic):
        new_publisher = Publisher(self, topic)
        self.service.assign_handle(new_publisher)
        handle = new_publisher.get_instance_handle()
        self.publishers[handle] = new_publisher

    def delete_publisher(self, publisher):
        pass

    def create_subscriber(self, topic):
        new_subscriber = Subscriber(self, topic)
        self.service.assign_handle(new_subscriber)
        handle = new_subscriber.get_instance_handle()
        self.subscribers[handle] = new_subscriber

    def delete_subscriber(self, subscriber):
        pass

class Topic(Entity):

    def __init__(self, topic_name, participant):
        self.name = topic_name
        self.parent = participant
        self.publishers = []
        self.subscribers = []

class Publisher(Entity):

    def __init__(self, participant, topic):
        self.parent = participant
        self.topic = topic
        self.data_buffer = []

    def write(self, message):
        pass

class Subscriber(Entity):
    pass
