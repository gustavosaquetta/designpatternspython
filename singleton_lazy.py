'''
	LazySingleton
	Objetivo: Garatir que um unico objeto da classe possa ser instanciado.
	Retorno : Um unico objeto será instanciado evitando endereçamento de memória desnecessário.
	Útil para telas de login, classe de conexão com banco de dados e outros.
'''

class LazySingleton:
	__instance = None
	def __init__(self):
		if not LazySingleton.__instance:
			print('Inicializando classe Singleton.')
		else:
			print('Instancia já realizada: ', self. get_instance())

	@classmethod
	def get_instance(cls):
		if not cls.__instance:
			cls.__instance = LazySingleton()
			print('Instancia realizada com sucesso: ', cls.__instance)
			return True
			
	def get_value(self):
		return True

# classe inicializada
LS = LazySingleton()

# instanciando a classe
if LS.get_instance():
	print('Retorno da instancia LS:', LS.get_value())

# classe inicializada
LSS = LazySingleton()
# a segunda instancia não será inicializada
if LSS.get_instance():
	print('Retorno da instancia LSS:', LSS.get_value())