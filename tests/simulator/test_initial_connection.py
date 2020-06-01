import pytest
import simpy
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../simulator/')
pprint.pprint(sys.path)

from network import Network
from processor import Processor
from driver import Driver
from peer import Peer    


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