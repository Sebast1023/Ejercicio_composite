from numero import Numero
from suma import Suma
from multiplicacion import Multiplicacion
from division import Division
from resta import Resta

#((4+5)+(3*2)-6)/3
ejemplo = Division(Resta(Suma(Suma(Numero(4),Numero(5)), Multiplicacion(Numero(3),Numero(2))),Numero(6)), Numero(3))

try:
    print("((4+5)+(3*2)-6)/3 = "+ str(ejemplo.evaluar()))
except ValueError as e:
    print("Error en la expresión:", e)
