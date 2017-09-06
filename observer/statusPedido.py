'''
Created on 5 de set de 2017

@author: gustavosaquetta
'''
from abc import ABCMeta, abstractmethod
class novaCompra:
	def __init__(self):
		self._interessados = []
		self._compra = None
		
	def adicionarInteressado(self, interessado):
		self._interessados.append(interessado)

	def removerInteressado(self):
		self._interessados.pop()

	def interessados(self):
		return [type(x).__name__ for x in self._interessados]
	
	def notificarInteressados(self):
		for pessoa in self._interessados:
			pessoa.update()
	
	def addCompra(self, compra):
		self._compra = compra
		
	def getCompra(self):
		return "Temos um xeroque rolmes: ", self._compra
		
class notificarInteressado(metaclass=ABCMeta):
	@abstractmethod
	def update(self):
		pass

class NotificarInteressadorEMAIL:
	def __init__(self, compra):
		self.compra = compra
		self.compra.adicionarInteressado(self)

	def update(self):
		print(type(self).__name__, self.compra.getCompra())
	
class NotificarInteressadorSMS:
	def __init__(self, compra):
		self.compra = compra
		self.compra.adicionarInteressado(self)

	def update(self):
		print(type(self).__name__, self.compra.getCompra())

class NotificarInteressadorOutraVia:
	def __init__(self, compra):
		self.compra = compra
		self.compra.adicionarInteressado(self)

	def update(self):
		print(type(self).__name__, self.compra.getCompra())
		

if __name__ == '__main__':
	nova_compra = novaCompra()
	
	for Notificar in [NotificarInteressadorEMAIL, NotificarInteressadorOutraVia, NotificarInteressadorSMS]:
		Notificar(nova_compra)
	
	print("\nNotificacoes: ", nova_compra.interessados())
	
	nova_compra.addCompra("Pedido de 2 macbook air")
	nova_compra.notificarInteressados()
	
	print("\nRemovendo interessandos: ", type(nova_compra.removerInteressado()).__name__)
	print("\nNotificacoes: ", nova_compra.interessados())
		
	nova_compra.addCompra("Pedido de 2 monitores 27")
	nova_compra.notificarInteressados()
	
	