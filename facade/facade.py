'''
Created on 29 de ago de 2017

@author: gustavosaquetta

Objetivo: O padrão façade tem como objetivo criar um interface de comunicacao da 
instancia que inicia o sistema com uma fachada que irá manipular as subrotinas.

App (minimalista) > Menu(fachada) > SubClasses(sistema)
'''

class Menu(object):
	def estruturar(self):
		self.rel = Relatorio.run_rel(self)
		self.cad = Cadastro.run_cad(self)
		self.grf = Graficos.run_chartz(self)
	
class Relatorio:
	def run_rel(self):
		print("mod relatorios")

class Cadastro:
	def run_cad(self):
		print("mod cadastro")

class Graficos:
	def run_chartz(self):
		print("mod graficos")

class App:
	def run(self):
		M = Menu()
		M.estruturar()

	def __del__(self):
		print('Easy')

if __name__ == '__main__':
	App().run()