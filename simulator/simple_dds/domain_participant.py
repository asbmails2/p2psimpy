from simple_dds import entity
from simple_dds import topic
from simple_dds import publisher
from simple_dds import subscriber

class Domain_Participant(entity.Entity):

    def __init__(self, dds_service):
        super(Domain_Participant, self).__init__()
        self.service = dds_service
        self.publishers = {}
        self.subscribers = {}
        self.topics = {}
        self.service.add_participant(self)

    def create_topic(self, topic_name):
        if self.service.topic_exists(topic_name):
            logging.warning(f'{topic_name} already exists.')
            return None
        else:
            new_topic = topic.Topic(topic_name, self)
            self.service.add_topic(new_topic)
            self.topics[topic_name] = new_topic
            return new_topic

    def delete_topic(self, topic):
        # Pré-condição: tópico deve ter sido criado por este participante
        pass

    def find_topic(self, topic_name):
        return self.service.get_topic(topic_name)

    def create_publisher(self, topic):
        new_publisher = publisher.Publisher(self, topic)
        self.service.assign_handle(new_publisher)
        handle = new_publisher.get_instance_handle()
        self.publishers[handle] = new_publisher
        return new_publisher

    def delete_publisher(self, publisher):
        pass

    def create_subscriber(self, topic, listener=None):
        data = self.service.retrieve_filtered_data_objects(topic.get_name())
        new_subscriber = subscriber.Subscriber(self, topic, data, listener)
        self.service.assign_handle(new_subscriber)
        handle = new_subscriber.get_instance_handle()
        self.subscribers[handle] = new_subscriber
        return new_subscriber

    def delete_subscriber(self, subscriber):
        pass

    def get_discovered_participants(self):
        pass
        # Usar o service

    def update_all_subscribers(self, data_object):
        for subscriber in self.subscribers.values():
            subscriber.receive_data(data_object)