from simple_dds import entity

class Topic(entity.Entity):

    def __init__(self, topic_name, participant):
        super(Topic, self).__init__()
        self.name = topic_name
        self.participant = participant
        self.publishers = []
        self.subscribers = []
        self.data_objects = {}
        self.creation_time = self.participant.service.driver.get_time()
        self.last_modified = self.creation_time

    def get_name(self):
        return self.name

    def attach_data_object(self, data_object):
        if data_object.get_topic_name() == self.name:
            handle = data_object.get_instance_handle()
            self.data_objects[handle] = data_object
            self.last_modified = self.participant.service.driver.get_time()

    def can_be_deleted(self):
        no_pubs = len(self.publishers) == 0
        no_subs = len(self.subscribers) == 0
        return no_pubs and no_subs