'''
Created on 8 de set de 2017

@author: gustavo.saquetta
'''
from abc import ABCMeta

class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        pass

class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()

class Receiver:
    def action(self):
        print('Receiver em action...')

class Invoker:
    def command(self, cc):
        self.cmd = cc

    def execute(self):
        self.cmd.execute()
        
if __name__ == '__main__':
    R = Receiver()
    CC = ConcreteCommand(R)
    I = Invoker()
    I.command(CC)
    I.execute()