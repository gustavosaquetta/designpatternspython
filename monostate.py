'''
	Monostate
	Objetivo: permitir que uma classe tenha mais de uma instancia
	e mesmo assim seus atributos possuam o mesmo valor.
	Retorno : Ao sobreescrever o __dict__ todas instancias da classe sempre vão ter atributos iguais.
'''
class Monostate:
	__defaul_dict = {}
	
	def __init__(self):
		self.isAtivo = False
		self.__dict__ = self.__defaul_dict
		pass
		
M = Monostate()
M.isAtivo = True

MS = Monostate()
print('O valor do atributo isAtivo do obj M é : ', M.isAtivo)
print('O valor do atributo isAtivo do obj MS é: ', MS.isAtivo)

#Outra alternativa para utilização do padrão monostate.
#Nesta o método reservado __new__ é sobreescrito
'''
class Monostate(object):
	__defaul_dict = {}
	
	def __new__(cls, *args, **kwags):
	obj = super(Monostate, cls).new(cls, *args, **kwags)
	obj.__dict__ = cls.__defaul_dict
	return obj
'''