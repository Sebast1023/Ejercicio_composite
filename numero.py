from expresion import Expresion
class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self):
        return self.valor