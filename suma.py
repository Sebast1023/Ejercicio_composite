from operacion import operacion
class suma(operacion):
    def evaluar(self):
        a = self.a.evaluar() if self.a else 0
        b = self.b.evaluar() if self.b else 0
        return a + b