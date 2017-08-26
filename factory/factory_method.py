'''
Created on 26 de ago de 2017

@author: gustavosaquetta

Implementação do factory method

São criadas as rotinas, as pessoas e a quais rotinas pertencem a quais pessoas.
Código com baixo acoplamento. O acrécimo de classes envolve pouca manutenção.
'''
from abc import ABCMeta, abstractmethod

class Rotina(metaclass=ABCMeta):
	@abstractmethod
	def listar(self):
		pass

class Compras(Rotina):
	def listar(self):
		print('Perfil de compras do consumidor...')

class ContasReceber(Rotina):
	def listar(self):
		print("Contas a receber do consumidor...")

class Pedidos(Rotina):
	def listar(self):
		print("Pedido de compras do fornecedor...")

class Catalogo(Rotina):
	def listar(self):
		print("Catalogo de pedidos do fornecedor...")

class Pessoa(metaclass=ABCMeta):
	def __init__(self):
		self.rotina = []
		self.createPessoa()

	def createPessoa(self):
		pass

	def getRotina(self):
		return self.rotina

	def addRotina(self, rotina):
		self.rotina.append(rotina)

class Fornecedor(Pessoa):
	def createPessoa(self):
		self.addRotina(Pedidos())
		self.addRotina(Catalogo())

class Cliente(Pessoa):
	def createPessoa(self):
		self.addRotina(Compras())
		self.addRotina(ContasReceber())

if __name__ == '__main__':
	tipo_pessoa = "Fornecedor"
	pessoa = eval(tipo_pessoa)()
	print("Pessoa: ", type(pessoa).__name__)
	print("Rotinas do perfil: ", pessoa.getRotina())