from expresion import Expresion
class operacion(Expresion):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    def agregarDerecha(self, b):
        self.b = b
    def agregarIzquierda(self, a):
        self.a = a