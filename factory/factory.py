'''
Created on 26 de ago de 2017

@author: gustavosaquetta

Retornar um objeto sem que o responsável pela utilização saiba a origem do código fonte.
'''

from abc import ABCMeta,  abstractmethod

class Base(metaclass=ABCMeta):
	@abstractmethod
	def get_data(self):
		pass

class Pessoa(Base):
	def get_data(self):
		print("Get data da pessoa...")

class Produto(Base):
	def get_data(self):
		print("Get data do produto")

class CadastroFactory(object):
	def get(self, obj):
		return eval(obj)().get_data()

if __name__ == '__main__':
	CF = CadastroFactory()
	cadastro = "Pessoa"
	CF.get(cadastro)