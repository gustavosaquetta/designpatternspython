'''
Created on 12 de set de 2017

@author: gustavo.saquetta
State, padrão utilizado para alterar o comportamento de objetos em tempo real.
'''
from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
	
	@abstractmethod
	def handle(self):
		pass
	
class ContextStateB(State):
	def handle(self):
		print("Processando B...")

class ContextStateA(State):
	def handle(self):
		print("Processando A...")

class Context(State):
	def __init__(self):
		self.state = None
	
	def getState(self):
		return self.state
	
	def setState(self, state):
		self.state = state

	def handle(self):
		self.state.handle()


if __name__ == '__main__':
	C  = Context()
	CA = ContextStateA()
	CB = ContextStateB()
	C.setState(CA)
	C.handle()