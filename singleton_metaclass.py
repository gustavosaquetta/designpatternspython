'''
	MetaSingleton
	Objetivo: Garantir que a instancia da classe sempre referencie o mesmo objeto em memoria.
	Retorno : O metasingleton permite que outras classes recebam suas caracteristicas.
	Útil para telas de login, classe de conexão com banco de dados e outros.
'''

class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]
		
class Abstrata(metaclass=MetaSingleton):
	pass
	
class Heranca(Abstrata):
	pass

A0 =  Abstrata()
A1 =  Abstrata()
H = Heranca()

#A metaclasse e a classe abstrata contem o memso endereço de memória, já a herança é um novo objeto.
print(A0, A1, H)