import logging
from threading import Lock
from singleton import Singleton
from simple_dds import entity

# Possíveis problemas de uso mútuo nesta classe? Veremos quando testarmos.
class UniqueHandleController(metaclass=Singleton):

    def __init__(self):
        self.next_available_handle = 1
        self.lock = Lock()
    
    def generate_handle(self):
        handle = None
        with self.lock:
            handle = self.next_available_handle
            self.next_available_handle += 1
        return handle

# Classe criada para impedir conflito entre leitura e escrita.
# Poderia fazer a lógica usando um Resource do simpy, mas prefiro evitar o uso..
# ... do simpy na lógica do DDS.
class Data_Buffer:

    def __init__(self):
        self.data_buffer = []
        self.lock = Lock()

    def write_to(self, data):
        with self.lock:
            self.data_buffer.append(data)

    def read_from(self, container):
        with self.lock:
            container = copy(self.data_buffer)
            self.data_buffer = []

    def is_empty(self):
        return len(self.data_buffer) == 0

# Talvez seja necessário fazer dictionaries personalizados, que evitem problemas de acesso mútuo.
class DDS_Service(entity.Entity):

    def __init__(self, driver):
        self.handle_controller = UniqueHandleController()
        self.instance_handle = self.handle_controller.generate_handle()
        self.driver = driver
        self.peer_list = []
        self.handles = {} # Handle: Entity
        self.participants = {} # Handle: Participant
        self.local_participants = {}
        self.topics = {}  # Topic name: Topic
        self.data_objects = {} # Handle: Data object
        self.message_handlers = {}

        self.add_message_handler_methods()
        self.attach_msg_reception_handler_to_driver()
        self.discover_peers()
        self.request_full_domain_data()

    def set_instance_handle(self, handle):
        raise RuntimeError("DDS Service's handle cannot be changed.")

    def get_instance_handle(self):
        return self.instance_handle

    def send_to_all_peers(self, msg):
        self.driver.async_function_call(['advertise', msg])

    def send_local_modification(self, type_name, data):
        change = (type_name, data)
        self.send_to_all_peers(change)

    # Fazer verificação de handle duplicada
    def assign_handle(self, entity):
        handle = self.handle_controller.generate_handle()
        entity.set_instance_handle(handle)
        self.handles[handle] = entity
    
    def add_participant(self, participant):
        self.assign_handle(participant)
        handle = participant.get_instance_handle()
        self.participants[handle] = participant
        self.local_participants[handle] = participant
        self.send_local_modification('NEW_PARTICIPANT', participant)

    def add_topic(self, topic):
        self.assign_handle(topic)
        topic_key = topic.get_name()
        self.topics[topic_key] = topic
        self.send_local_modification('NEW_TOPIC', topic)

    def add_data_object(self, data_object):
        self.assign_handle(data_object)
        handle = data_object.get_instance_handle()
        self.data_objects[handle] = data_object
        self.attach_data_object_to_topic(data_object)
        self.send_local_modification('NEW_DATA', data_object)

    def topic_exists(self, topic_name):
        return topic_name in self.topics

    def get_topic(self, topic_name):
        if self.topic_exists(topic_name):
            return self.topics[topic_name]
        else: # Como lidar com isto?
            pass
    
    def erase_topic_from_domain(self, topic):
        # Deleta tópico e todos os dados associados a ele.
        pass

    def discover_peers(self):
        self.peer_list = self.driver.fetch_peer_list()
    
    def receive_incoming_data(self, msg):
        logging.info(str(self.driver.get_time()) + ' :: ' + f'Data received by DDS Service, handle {str(self.instance_handle)}')
        for z in self.interpret_data(msg):
            yield z

    def add_message_handler_methods(self):
        self.message_handlers['NEW_PARTICIPANT'] = self.append_remote_participant
        self.message_handlers['NEW_TOPIC'] = self.append_remote_topic
        self.message_handlers['NEW_DATA'] = self.append_data_object
        self.message_handlers['SEND_ALL_DATA'] = self.send_full_domain_data
        self.message_handlers['ALL_DATA'] = self.receive_full_domain_data

    def append_remote_participant(self, r_participant):
        handle = r_participant.get_instance_handle()
        if handle not in self.participants and handle not in self.handles:
            self.handles[handle] = r_participant
            self.participants[handle] = r_participant

    def append_remote_topic(self, r_topic):
        topic_name = r_topic.get_name()
        if not self.topic_exists(topic_name):
            handle = r_topic.get_instance_handle()
            self.handles[handle] = r_topic
            self.topics[topic_name] = r_topic
        else:
            self.resolve_topic_conflict(r_topic)

    def resolve_topic_conflict(self, topic):
        # TODO: Completar este método.
        # O tópico com a instance handle menor tem prioridade.
        # Caso o serviço local tenha prioridade, é necessário informar os outros nodos.
        pass

    def append_data_object(self, new_data):
        handle = new_data.get_instance_handle()
        self.data_objects[handle] = new_data
        if handle not in self.handles:
            self.handles[handle] = new_data
        self.send_data_object_to_all_participants(new_data)
        self.attach_data_object_to_topic(new_data)

    def send_data_object_to_all_participants(self, data_object):
        for participant in self.local_participants.values():
            participant.update_all_subscribers(data_object)

    def attach_data_object_to_topic(self, data_object):
        topic_name = data_object.get_topic_name()
        if self.topic_exists(topic_name):
            self.topics[topic_name].attach_data_object(data_object)

    def send_full_domain_data(self, to_address):
        local_data = []
        for key, value in self.participants.items():
            packet = ('NEW_PARTICIPANT', value)
            local_data.append(packet)
        for key, value in self.topics.items():
            packet = ('NEW_TOPIC', value)
            local_data.append(packet)
        for key, value in self.data_objects.items():
            packet = ('NEW_DATA', value)
            local_data.append(packet)
        msg = ('ALL_DATA', local_data)
        self.driver.async_function_call(['send', to_address, msg])
    
    def receive_full_domain_data(self, r_data):
        # TODO: Remove this hack.
        # HACK ALERT I JUST WANT THIS TO WORK
        for element in r_data:
            envelope = [0,0, element]
            for z in self.interpret_data(envelope):
                z

    def interpret_data(self, msg):
        #breakpoint()
        data = msg[2]
        # Presumimos que os dados estejam em uma 2-tupla, sendo o primeiro elemento..
        # .. uma string descrevendo o pedido, o segundo elemento os dados em si
        if data[0] not in self.message_handlers:
            logging.warning(str(self.driver.get_time()) + ' :: ' + f'DDS Service (Handle {str(self.instance_handle)}): Invalid request: {str(data[1])}')
        else:
            self.message_handlers[data[0]](data[1])
        yield self.driver.env.timeout(0)

    def attach_msg_reception_handler_to_driver(self):
        self.driver.register_handler(self.receive_incoming_data, 'on_message')

    def request_full_domain_data(self):
        request_msg = ('SEND_ALL_DATA', self.driver.address)
        self.send_to_all_peers(request_msg)

    def retrieve_all_data_objects(self):
        return self.data_objects.values()

    def retrieve_filtered_data_objects(self, topic_name):
        data = []
        for element in self.data_objects.values():
            if element.get_topic_name() == topic_name:
                data.append(element)
        return data