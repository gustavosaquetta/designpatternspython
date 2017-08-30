'''
Singleton
Objetivo : Garantir que um objeto possa ser instanciado na memória apenas uma vez.
Resultado: O objeto é instanciado 2 vezes, mas com o mesmo endereço de memória.
'''

class ServiceCheck:
	_instance = None
	def __new__(cls, *args, **kwargs):
		if not ServiceCheck._instance:
			ServiceCheck._instance = super(ServiceCheck, cls).__new__(cls, *args, **kwargs)

		return ServiceCheck._instance

	def __init__(self):
		self._services = []

	def addService(self):
		self._services.append('Serviço 1')
		self._services.append('Serviço 2')
		self._services.append('Serviço 3')
		self._services.append('Serviço 4')
		self._services.append('Serviço 5')
		self._services.append('Serviço 6')

	def changeService(self):
		self._services.pop()
		self._services.append('Services 7')

HS1 = ServiceCheck()
HS2 = ServiceCheck()

HS1.addService()

for i in range(6):
	print('Verificando serviço na estação 1: ', HS1._services[i])

HS2.changeService()
for i in range(6):
	print('Verificando serviço na estação 2: ', HS2._services[i])