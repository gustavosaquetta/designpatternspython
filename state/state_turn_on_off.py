'''
Created on 13 de set de 2017

@author: gustavosaquetta
'''

from abc import abstractmethod, ABCMeta

class State(metaclass=ABCMeta):
	
	@abstractmethod
	def doThis(self):
		pass
	
class TurnOn(State):
	def doThis(self):
		print('Ligou...')

class TurnOff(State):
	def doThis(self):
		print('Desligou...')

class Interruptor(State):
	
	def __init__(self):
		self.state = None

	def getState(self):
		return self.state
	
	def setState(self, state):
		self.state = state

	def doThis(self):
		self.state.doThis()

if __name__ == '__main__':
	I   = Interruptor()
	I.getState()

	TOn  = TurnOn()
	TOff = TurnOff()
	
	I.setState(TOff)
	I.doThis()