import simpy
import driver

# Uma mensagem tem o seguinte formato:
# - Timestamp
# - Remetente
# - Destino
# - Conteúdo
# Representamos usando um dictionary
# -------------
# Neste rascunho, a rede está contida em DHCP_Server.
# Nodos são hosts, armazenados na lista self.hosts. O índice da lista é o endereço.
# A princípio, deveríamos fazer um interpretador de mensagens, mas, para facilitar as coisas,
# vamos adicionar um campo chamado "tipo" nas mensagens, o qual nos dirá o propósito da mensagem.
# Nesse pequeno teste, temos os seguintes tipos:
# 1 - DHCP discovery
# 2 - DHCP offer
# 3 - DHCP request
# 4 - DHCP acknowledgement

def log():
    pass

class DHCP_Server:

    leaseTime = 10                     # Por quanto tempo um endereço será emprestado

    def __init__(self, environment, maxHosts = 100):
        self.env = environment
        host = {
            'id': 0                         # Representa endereço MAC. 0 = Livre
        }
        self.maxHosts = maxHosts
        self.hosts = [host] * maxHosts
        lease = {
            'address': 0,
            'time': 0                       # Tempo de empréstimo. 0 = infinito (reservado)
        }
        self.leases = []
        self.messageBuffer = []             # Buffer de mensagens da rede
        self.available = 0                  # Próximo endereço disponível
        self.time = self.env.now
        self.action = self.env.process(self.run())

        self.commands = {
        'lease': self.lease
        }


    def getTime(self):
        self.time = self.env.now

    def getMessageList(self, messagesReceived):
        self.messageBuffer = list(messagesReceived)

    def clearBuffer(self):
        self.messageBuffer = []


    def lease(self):
        pass
        

    def checkLease(self):
        for lease in self.leases:
            if lease['time'] != 0 and lease['time'] >= self.currentTime:
                self.hosts[lease['address']] = 0    # Libera endereço
                del lease
    
    def parse(self):
        pass




    def run(self, messages = []):
        #while True:
            self.getTime()                               # Talvez não usar, visto que já temos uma referência a env.now. Acho getTime mais legível
            self.checkLease()
            self.getMessageList(messages)
            self.commands['lease']
            yield self.env.timeout(1)


environment = simpy.Environment()
thing = DHCP_Server(environment)
environment.run(until=2)

