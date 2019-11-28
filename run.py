import simpy
import peer
import network
import driver

"""
Run app.
Controll of peers, duration and others details.

"""

NUM_PEERS = 5
SIM_DURATION = 20


# create env
env = simpy.Environment()

# network
net = network.Network(env,2)

#create peers

nodes = []

for i in range (NUM_PEERS):
     dri = driver.Driver(net)
     new_peer = peer.Peer(dri)
     nodes.append(new_peer)

for a in nodes:
    env.process(a.driver.test_run())

env.run(until=SIM_DURATION)