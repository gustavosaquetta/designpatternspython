'''
Created on 8 de set de 2017

@author: gustavo.saquetta
'''
from abc import ABCMeta, abstractmethod

class OrdemEstoque(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class ComprarEstoque(OrdemEstoque):
    def __init__(self, estoque):
        self.estoque = estoque

    def execute(self):
        self.estoque.comprar()

class VenderEstoque(OrdemEstoque):
    '''
        like a promotion
    '''
    def __init__(self, estoque):
        self.estoque = estoque

    def execute(self):
        self.estoque.vender()

class MovimentarEstoque:
    def comprar(self):
        print('Agendando compra de estoque..')

    def vender(self):
        print('Agendando venda de estoque..')

class Agendar:
    def __init__(self):
        self.__evento_estoque = []

    def gerarOrdem(self, evento):
        self.__evento_estoque.append(evento)
        evento.execute()

if __name__ == '__main__':
    #back
    ME  = MovimentarEstoque()
    CE = ComprarEstoque(ME)
    VE = VenderEstoque(ME)
    
    #front 
    A = Agendar()
    A.gerarOrdem(CE)
    A.gerarOrdem(VE)