'''
Created on 13 de set de 2017

@author: gustavosaquetta
'''
class ComputerState(object):
	nome = 'state'
	allowed = []

	def switch(self, state):
		if state.name in self.allowed:
			print('O estado atual: ', self, '. Atualizando estado para: ', state.name)
			self.__class__ = state

		else:
			print('Estado atual: ', self, ' tentativa de troca para: ', state.name, 'deu ruim!')

	def __str__(self):
		return self.name

class Off(ComputerState):
	name = 'off'
	allowed = ['on']

class On(ComputerState):
	name = 'on'
	allowed = ['off', 'suspend', 'hibernate']

class Suspend(ComputerState):
	name = 'suspend'
	allowed = ['on']

class Hibernate(ComputerState):
	name = 'hibernate'
	allowed = ['on']

class Computer(object):
	def __init__(self, model='MAC'):
		self.model = model
		self.state = Off()

	def change(self, state):
		self.state.switch(state)


if __name__ == '__main__':
	C = Computer()
	C.change(On)