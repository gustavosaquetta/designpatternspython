'''
Created on 11 de set de 2017

@author: gustavo.saquetta

Templetes sao utilizados para codificacaoes que pode se repetir ao logo do sistema.
Um sistema pode ter diversas importacoes todas muito parecidas mudando apenas o layout
'''

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def coletarDados(self):
        pass
    
    @abstractmethod
    def prepararLayout(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    def exportar(self):
        self.coletarDados()
        self.prepararLayout()
        self.run()

class Exportacao(Base):

    def coletarDados(self):
        print('Coletando informacoes...')

    def prepararLayout(self):
        print('Preparando layout...')

    def run(self):
        print('Executando exportação!')

if __name__ == '__main__':
    E = Exportacao()
    E.exportar()