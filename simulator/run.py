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
# Configuração do root logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
handlers = [console_handler]
logging.basicConfig(level = logging.INFO,
                    format = '[%(levelname)s] [%(module)10s] %(message)s',
                    handlers = handlers
)

NUM_PEERS = 1
SIM_DURATION = 300

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
