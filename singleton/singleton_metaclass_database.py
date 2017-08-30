'''
	MetaSingleton
	Objetivo: Garantir que a instancia da classe sempre referencie o mesmo objeto em memoria.
	Retorno : O metasingleton permite que outras classes recebam suas caracteristicas.
	Útil para telas de login, classe de conexão com banco de dados e outros.
'''

import sqlite3

class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
		return cls._instances[cls]

class Database(metaclass=MetaSingleton):
	connection = None
	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect("db.sqlite3")
			self.cursor = self.connection.cursor()
		return self.cursor
		
cur1 = Database().connect()
cur2 = Database().connect()

print(cur1, cur2)

