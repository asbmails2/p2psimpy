import simpy
import logging
import peer
import network
import driver
import processor

"""
Run app.
Peer control, duration and others details.

"""
logging.basicConfig(level=logging.INFO)

NUM_PEERS = 5
SIM_DURATION = 1000


# create env
env = simpy.Environment()

# network
net = network.Network(env,2)

#create peers

nodes = []

teste = env.timeout(200)

for i in range (NUM_PEERS):
     proc = processor.Processor(env, i, 3)
     dri = driver.Driver(net, proc)
     new_peer = peer.Peer(dri, i)
     nodes.append(new_peer)
     env.process(dri.run())


env.run(until=SIM_DURATION)
