import simpy
import peer
import network
import driver
import processor

"""
Run app.
Controll of peers, duration and others details.

"""

NUM_PEERS = 5
SIM_DURATION = 100


# create env
env = simpy.Environment()

# network
net = network.Network(env,2)

#create peers

nodes = []

teste = env.timeout(2)

for i in range (NUM_PEERS):
     proc = processor.Processor(env, 10)
     dri = driver.Driver(net, proc)
     new_peer = peer.Peer(dri)
     nodes.append(new_peer)
     env.process(dri.connect())


env.run(until=SIM_DURATION)
