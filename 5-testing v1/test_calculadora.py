from calculadora import Calculadora
import pytest


def test_suma_positivos():
    calc = Calculadora()
    assert calc.suma(2, 2) == 4

def test_suma_positivo_y_negativo():
    calc = Calculadora()
    assert calc.suma(-2, 2) == 0

def test_suma_numero_grande():
    calc = Calculadora()
    assert calc.suma(7, 255) == 262

def test_suma_negativos():
    calc = Calculadora()
    assert calc.suma(-7, -2) == -9

def test_suma_error_tipo():
    calc = Calculadora()

    with pytest.raises(TypeError) as the_error:
        calc.suma("hola", 2)
    assert str(the_error.value) == "Debes introducir un número"