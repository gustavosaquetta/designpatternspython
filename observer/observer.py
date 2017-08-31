'''
Created on 31 de ago de 2017

@author: gustavosaquetta
'''

class Subject:

	def __init__(self):
		self.__observers = []

	def register(self, observer):
		self.__observers.append(observer)

	def notifyAll(self, *args, **kwargs):
		for observer in self.__observers:
			observer.notify(self, *args, **kwargs)

class observerOne:
	def __init__(self, subject):
		subject.register(self)

	def notify(self, subject, *args):
		print(type(self).__name__, 'tem:', args, 'de: ', subject)

class observerTwo:
	def __init__(self, subject):
		subject.register(self)

	def notify(self, subject, *args):
		print(type(self).__name__, 'tem:', args, 'de: ', subject)

if __name__ == '__main__':
	subject = Subject()
	obs1 = observerOne(subject)
	obs2 = observerTwo(subject)
	subject.notifyAll('Notificação...')