"""
Class peer for create all the base stack for peer

Definir as caracteristicas do nodo basicas - ID , Recursos - Qualidade

riar um canal broadcast onde o peer precisa se conectar
E criar os links de comunicacao unicast

agente tem (ref de um canal broad)

Resources e uma lista de recursos com a sua qualidade

"""
# -*- coding: utf-8 -*-

class Peer:

    def start(self):
        self.driver.send(1, 'hello')

    def handle_msgs (self, msg):
        print (msg)

    def on_connect (self, address):
        print('driver connected with address {}'.format(address))
        self.driver.advertise("Hello World")

    def on_disconnect (self):
        self.driver.advertise("Bye World")

    def __init__ (self,driver):
        self.driver = driver
        self.driver.register_handler(self.handle_msgs)
        self.driver.register_handler(self.on_connect, 'on_connect')
        self.driver.register_handler(self.on_disconnect, 'on_disconnect')
        self.start()
        #self.exec()






