import pytest
import simpy

from simulator.network import Network
from simulator.processor import Processor
from simulator.driver import Driver
from simulator.peer import Peer     


def test_connection():
    # create env
    env = simpy.Environment()
    # network
    net = Network(env,2)
    #create peers
    teste = env.timeout(50)
    
    proc = Processor(env, 0, 3)
    dri = Driver(net, proc)
    new_peer = Peer(dri, 0)
    env.process(dri.connect())
    
    env.run(until=10)
    
    assert dri.address != None

def test_timeout_keep_alive():
    # create env
    env = simpy.Environment()
    # network
    net = Network(env,2)
    #create peers
    teste = env.timeout(50)
    
    proc = Processor(env, 0, 3)
    dri = Driver(net, proc)
    new_peer = Peer(dri, 0)
    
    #env.process(dri.disconnect())
    
    env.run(until=50)
    
    assert dri.address == None
