
class Calculadora():
    def suma(self, x, y):
        try:
            suma = x + y
        except TypeError:
            raise TypeError("Debes introducir un número")
        return suma

    def resta(self): ...

    def multiplicacion(self): ...

    def division(self): ...