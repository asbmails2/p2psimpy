from simple_dds import entity

class Topic(entity.Entity):

    def __init__(self, topic_name, participant):
        super(Topic, self).__init__()
        self.name = topic_name
        self.participant = participant
        self.publishers = []
        self.subscribers = []
        self.data_objects = {}

    def get_name(self):
        return self.name

    def attach_data_object(self, data_object):
        if data_object.get_topic_name() == self.name:
            handle = data_object.get_instance_handle()
            self.data_objects[handle] = data_object