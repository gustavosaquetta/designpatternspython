'''
Created on 30 de ago de 2017

@author: gustavosaquetta
'''
from abc import  ABCMeta, abstractmethod

class Pessoa:
	'''
	classdocs
	'''
	def __init__(self):
		print("Pessoa realizando resgate...")
		self.cartao_fidelidade = CartaoFidelidade()
		self.isResgate = False

	def fazer_resgate(self):
		self.isResgate = self.cartao_fidelidade.realizar_resgate()

	def __del__(self):
		if self.isResgate:
			print("Resgate realizado com sucesso.")
		else:
			print("Não foi possível realizar resgate.")

class Resgate(metaclass=ABCMeta):

	@abstractmethod
	def realizar_resgate(self):
		pass

class ServicoFidelidade(Resgate):
	
	def __init__(self):
		self.cartao = None
		self.id = None

	def __getId(self):
		self.id = self.cartao
		return self.id
	
	def __verificaSaldo(self):
		print("Verificando saldo da conta: ", self.__getId())
		return True

	def setCartao(self, cartao):
		self.cartao = cartao

	def realizar_resgate(self):
		if self.__verificaSaldo():
			print("Realizando resgate...")
			return True
		else:
			print("Não foi possóvel realizar resgate!")
			return False

class CartaoFidelidade(Resgate):
	
	def __init__(self):
		self.servico_fidelidade = ServicoFidelidade

	@abstractmethod
	def realizar_resgate(self):
		cartao = "8876"
		self.servico_fidelidade.setCartao(cartao)
		return self.servico_fidelidade.realizar_resgate()
	
Pessoa().fazer_resgate()