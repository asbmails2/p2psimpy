import simpy
import logging
import peer
import network
import driver
import processor
import simple_dds

"""
Run app.
Peer control, duration and others details.

"""
# Configuração do root logger
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
handlers = [console_handler]
logging.basicConfig(level = logging.INFO,
                    format = '[%(levelname)10s] [%(module)10s] %(message)s',
                    handlers = handlers
)

NUM_PEERS = 1
SIM_DURATION = 1000

# create env
env = simpy.Environment()

# network
net = network.Network(env,2)

#create peers

nodes = []

teste = env.timeout(200)


proc_0 = processor.Processor(env, 0, 3)
dri_0 = driver.Driver(net, proc_0)
peer_0 = peer.Peer(dri_0, 0)
env.process(dri_0.run())
env.process(peer_0.dds_write_test())

proc_1 = processor.Processor(env, 1, 3)
dri_1 = driver.Driver(net, proc_1)
peer_1 = peer.Peer(dri_1, 1)
env.process(dri_1.run())
env.process(peer_1.dds_read_test())


env.run(until=SIM_DURATION)
