'''
	Singleton
	Objetivo : Garantir que um objeto possa ser instanciado na memória apenas uma vez.
	Resultado: O objeto é instanciado 2 vezes, mas com o mesmo endereço de memória.
'''

class Singleton(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Singleton, cls).__new__(cls)
		return cls.instance


S = Singleton()
print('Objeto S instanciado: ', id(S))

S2 = Singleton()
print('Objeto S2 instanciado: ', id(S2))


