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


    def handle_msgs (self, msg):
        print (msg)


    def exec_1 (self):
        self.driver.advertise("Hello World")

    def __init__ (self,driver):
        self.driver = driver
        self.driver.register_handler(self.handle_msgs)
        self.driver.register_handler(self.exec_1)
        #self.exec()






