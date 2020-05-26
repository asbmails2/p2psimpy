from simple_dds import entity

class Data_Object(entity.Entity):
    
    def __init__(self, publisher_handle, topic, data):
        super(Data_Object, self).__init__()
        self.publisher_handle = publisher_handle
        self.topic = topic
        self.content = data

    def __str__(self):
        return self.content

    def get_topic_name(self):
        return self.topic.get_name()