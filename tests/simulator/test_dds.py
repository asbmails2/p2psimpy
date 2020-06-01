import pytest
import pprint
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../simulator/')
pprint.pprint(sys.path)

import simpy
import random
from network import Network
from processor import Processor
from driver import Driver
from peer import Peer
from simple_dds import *

@pytest.fixture
def environment_and_network():
    network_latency = 2
    max_peers = 100
    env = simpy.Environment()
    net = Network(env, network_latency, max_peers)
    return (env, net)

@pytest.fixture
def subscriber_number():
    # Set Number:
    return 5

def test_simple_publication_two_peers(environment_and_network):
    env, net = environment_and_network
    proc_latency = 3
    random.seed()
    message = random.randrange(1000)
    topic_name = random.randrange(1000)
    wait_before_publication = 100
    wait_before_reading = 150
    simulation_time = 400
    container = None

    publishing_peer = initialize_peer(env, net, 0, 0, proc_latency)
    subscribing_peer = initialize_peer(env, net, 1, 1, proc_latency)
    publication = publishing_peer.wait_then_publish_message
    reading = subscribing_peer.wait_then_read_message
    add_process_to_simulation(env, publication(topic_name, message, wait_before_publication))
    add_process_to_simulation(env, reading(topic_name, message, wait_before_reading))
    env.run(until=simulation_time)
    container = str(subscribing_peer.latest_read_msg)
    assert container == str(message)

def test_simple_publication_to_multiple_peers(environment_and_network, subscriber_number):
    env, net = environment_and_network
    proc_latency = 3
    random.seed()
    message = random.randrange(1000)
    topic_name = random.randrange(1000)
    wait_before_publication = 100
    wait_before_reading = 150
    simulation_time = 1000
    subscriber_id = 1
    subscribers = []
    received_msg = None

    publishing_peer = initialize_peer(env, net, 0, 0, proc_latency)
    publication = publishing_peer.wait_then_publish_message(topic_name, message, wait_before_publication)
    add_process_to_simulation(env, publication)
    for i in range(subscriber_number):
        subscriber = initialize_peer(env, net, 0, i, proc_latency)
        reading = set_up_subscription(subscriber, topic_name, message, wait_before_reading)
        add_process_to_simulation(env, reading)
        subscribers.append(subscriber)

    env.run(until=simulation_time)
    for subscriber in subscribers:
        received_msg = str(subscriber.latest_read_msg)
        assert received_msg == str(message)

def initialize_peer(environment, network, proc_id, peer_id, proc_latency):
    proc = Processor(environment, proc_id, proc_latency)
    dri = Driver(network, proc)
    peer = Peer(dri, peer_id)
    environment.process(dri.run())
    return peer

def add_process_to_simulation(environment, method):
    environment.process(method)

def set_up_subscription(peer, topic_name, message, wait_time=100):
    yield peer.driver.env.timeout(wait_time)
    the_service = dds_service.DDS_Service(peer.driver)
    participant = domain_participant.Domain_Participant(the_service)
    topic = participant.create_topic(topic_name)
    sub = participant.create_subscriber(topic, peer.read_new_message)