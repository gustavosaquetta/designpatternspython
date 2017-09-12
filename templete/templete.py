'''
Created on 11 de set de 2017

@author: gustavo.saquetta
'''
from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation(self):
        pass
    
    @abstractmethod
    def operationTwo(self):
        pass

    def templeteMethod(self):
        print('Definindo algoritimos da operacao 1 e 2.')
        self.operation()
        self.operationTwo()
        
class ConcreteClass(AbstractClass):

    def operation(self):
        print('Operacao um...')

    def operationTwo(self):
        print('Operacao doix...')

class Venda:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.templeteMethod()

if __name__ == '__main__':
    V = Venda()
    V.main()