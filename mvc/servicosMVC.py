'''
Created on 12 de set de 2017

@author: gustavo.saquetta
O ideial é dividir o MVC em 3 camadas de arquivo neste exemplo o MVC é utilizada em um unico arquivo,
a divisão será lógica e não lógica/fisica.
'''

class Model(object):
    
    modulos = {
                'nfe':  {'codigo': '001', 'preco': 300.00},
                'nfce': {'codigo': '002', 'preco': 300.00},
                'BI':   {'codigo': '003', 'preco': 500.00},
        }

class View(object):
    def exibe_modulos(self, modulos):
        for modulo in modulos:
            #não está printando, apenas exemplo
            modulo

    def exibe_valor_modulo(self, modulos):
        M = Model()
        for modulo in modulos:
            print('Código: ', M.modulos[modulo]['codigo'],
                  '\nMódulo: ', modulo,
                  '\nNo valor: ', M.modulos[modulo]['preco'])
            print('#'*30)

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_modulos(self):
        modulos = self.model.modulos.keys()
        return(self.view.exibe_modulos(modulos))
    
    def get_precos(self):
        modulos = self.model.modulos.keys()
        return(self.view.exibe_valor_modulo(modulos))

class Modulo(object):
    C = Controller()
    C.get_modulos()
    C.get_precos()

if __name__ == '__main__':
    M = Modulo()