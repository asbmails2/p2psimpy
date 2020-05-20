import logging
from threading import Lock

import singleton

# Possíveis problemas de uso mútuo nesta classe? Veremos quando testarmos.
class UniqueHandleController(metaclass=Singleton):

    def __init__(self):
        self.next_available_handle = 1
        self.lock = threading.Lock()
    
    def generate_handle(self)
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
        self.lock = threading.Lock()

    def write_to(self, data):
        with self.lock:
            self.data_buffer.append(data)

    def read_from(self, container):
        with self.lock:
            container = copy(self.data_buffer)
            self.data_buffer = []

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

# Talvez seja necessário fazer dictionaries personalizados, que evitem problemas de acesso mútuo.
class DDS_Service(Entity):

    def __init__(self, driver, handle_controller):
        self.handle_controller = handle_controller
        self.instance_handle = self.handle_controller.generate_handle()
        self.driver = driver
        self.peer_list = []
        self.data_buffer = Data_Buffer()
        self.local_changes = Data_Buffer()
        self.handles = {} # Handle: Entity
        self.participants = {} # Handle: Participant
        self.topics = {}  # Topic name: Topic
        self.data_objects = {} # Handle: Data object
        self.message_handlers = {}

    def set_instance_handle(self, handle):
        raise RuntimeError("DDS Service's handle cannot be changed.")

    def get_instance_handle(self):
        return self.instance_handle

    # TODO: Notificar na rede quando houver atualização, para todos os métodos 'add'

    # Enfileiramos todas as mudanças locais, para mandá-las na rede de uma vez só.
    def queue_local_modification(self, type_name, data):
        change = (type_name, data)
        self.local_changes.write_to(change)

    # Fazer verificação de handle duplicada
    def assign_handle(self, entity):
        handle = self.handle_controller.generate_handle()
        entity.set_instance_handle(handle)
        self.handles[handle] = entity
    
    def add_participant(self, participant):
        self.assign_handle(participant)
        handle = participant.get_instance_handle()
        self.participants[handle] = participant
        self.queue_local_modification(('NEW_PARTICIPANT', participant))

    def add_topic(self, topic):
        self.assign_handle(topic)
        topic_key = topic.get_name()
        self.topics[topic_key] = topic
        self.queue_local_modification(('NEW_TOPIC', topic))

    def topic_exists(self, topic_name):
        return topic_name in self.topics

    def get_topic(self, topic_name)
        if self.topic_exists(topic_name):
            return self.topics[topic_name]
        else: # Como lidar com isto?
            pass

    def discover_peers(self):
        self.peer_list = self.driver.fetch_peer_list()
    
    def receive_incoming_data(self, msg):
        self.data_buffer.write_to(msg)
        logging.info(str(self.driver.get_time() + ' :: ' + f'Data received by DDS Service, handle {self.instance_handle}'))

    def append_remote_participant(self, r_participant):
        handle = r_participant.get_instance_handle()
        if handle not in self.participants and handle not in self.handles:
            self.handles[handle] = r_participant
            self.participants[handle] = r_participant

    def append_remote_topics(self, r_topic):
        topic_name = r_topic.get_name()
        if not self.topic_exists(topic_name):
            handle = r_topic.get_instance_handle()
            self.handles[handle] = r_topic
            self.topics[topic_name] = r_topic
        else:
            self.resolve_topic_conflict(r_topic)

    def update_data_objects(self, r_data):
        handle = r_data.get_instance_handle()
        self.data_objects[handle] = r_data
        if handle not in self.handles:
            self.handles[handle] = r_data

    def attach_msg_reception_handler_to_driver(self):
        self.driver.register_handler(self.receive_incoming_data, 'on_message')

    # Não gosto muito deste nome.
    def interpret_data(self, data):
        # Presumimos que os dados estejam em uma 2-tupla, sendo o primeiro elemento..
        # .. uma string descrevendo o pedido, o segundo elemento os dados em si
        if data[1] not in self.message_handlers:
            logging.warning(str(self.driver.get_time() + ' :: ' + f'DDS Service (Handle {self.instance_handle}): Invalid request: {data[1]}'))
        else
            self.message_handlers[data[1]](data[2])
    
    def process_received_messages(self):
        message_queue = []
        self.data_buffer.read_from(message_queue)
        for message in message_queue:
            self.interpret_data(message)

    def propagate_local_changes(self):
        changes_to_send = []
        self.local_changes.write_to(changes_to_send)
        message = ('UPDATE', changes_to_send)
        # Aqui, usaríamos o método advertise do driver, mas ele só lida com msgs tipo string. E agora?

    def setup(self):
        self.add_message_handler_methods()
        self.attach_msg_reception_handler_to_driver()
        self.discover_peers()

    def run(self):
        # Através do driver, queremos:
        # - Achar participantes
        # - Atualizar instâncias de dados
        # - Enviar dados relevantes aos subscribers
        # - Processar dados recebidos
        self.setup()


class Domain_Participant(Entity):

    def __init__(self, dds_service):
        self.service = dds_service
        self.publishers = {}
        self.subscribers = {}
        self.topics = {}
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

    def get_discovered_participants(self):
        # Usar o service

class Topic(Entity):

    def __init__(self, topic_name, participant):
        self.name = topic_name
        self.parent = participant
        self.publishers = []
        self.subscribers = []

    def get_name(self):

class Publisher(Entity):

    def __init__(self, participant, topic):
        self.parent = participant
        self.topic = topic
        self.data_buffer = []

    def write(self, message):
        pass

class Subscriber(Entity):
    pass
