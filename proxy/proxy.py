'''
Created on 30 de ago de 2017

@author: gustavosaquetta

Exemplo de utilização de proxy.
'''

class Servico(object):
	'''
	classdocs
	'''
	def __init__(self):
		self.isAtivo = False

	def run(self):
		self.isAtivo = True
		print(type(self).__name__, "Está ativo no momento!")


	def stop(self):
		self.isAtivo = False
		print(type(self).__name__, "Está desativado no momento!")

	def getStatus(self):
		return self.isAtivo

class Interface(object):
	def ativar(self):
		self.servico = Servico()
		
		if not self.servico.getStatus():
			self.servico.run()
			
if __name__ == '__main__':
	Interface().ativar()
