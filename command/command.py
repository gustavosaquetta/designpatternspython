'''
Created on 6 de set de 2017

@author: gustavosaquetta
'''

class Wizard():
	def __init__(self, src, rootdir):
		self.escolhas = []
		self.diretorio = rootdir
		self.src = src
	
	def preferences(self, command):
		self.escolhas.append(command)

	def execute(self):
		for escolha in self.escolhas:
			if list(escolha.values())[0]:
				print("Copiando arquivos -- ", self.src, "to ", self.diretorio)
			else:
				print("Não foi possível efetuar a operação.")

if __name__ == '__main__':
	## Código do Cliente
	wizard = Wizard('python3.6.gzip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/')
	wizard.preferences({'python': True})
	wizard.preferences({'psychopg': False})
	wizard.execute()