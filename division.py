from operacion import Operacion
class Division(Operacion):
    def evaluar(self):
        a = self.a.evaluar() if self.a else 0
        b = self.b.evaluar() if self.b else 0
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b