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
SIM_DURATION = 100000


# create env
env = simpy.Environment()

# network
net = network.Network(env,2)

#create peers

nodes = []

teste = env.timeout(2)

for i in range (NUM_PEERS):
     proc = processor.Processor(env, i, 3)
     dri = driver.Driver(net, proc)
     new_peer = peer.Peer(dri, i)
     nodes.append(new_peer)
     env.process(dri.run())


env.run(until=SIM_DURATION)
