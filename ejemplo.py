from numero import Numero
from suma import suma
from multiplicacion import multiplicacion
from division import division

#((4+5)+(3*2))/3
ejemplo = division(suma(suma(Numero(4),Numero(5)), multiplicacion(Numero(3),Numero(2))), Numero(3))

try:
    print("((4+5)+(3*2))/3 = "+ str(ejemplo.evaluar()))
except ValueError as e:
    print("Error en la expresión:", e)
