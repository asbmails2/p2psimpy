from simple_dds import entity
from simple_dds import data_object

class Publisher(entity.Entity):

    def __init__(self, participant, topic):
        super(Publisher, self).__init__()
        self.participant = participant
        self.topic = topic

    def write(self, data):
        pub_handle = self.get_instance_handle()
        new_data = data_object.Data_Object(pub_handle, self.topic, data)
        self.participant.service.add_data_object(new_data)