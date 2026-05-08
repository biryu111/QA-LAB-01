from src.calculadora import *

def test_suma():
    assert suma(3, 2) == 5

def test_resta():
    assert resta(10, 4) == 6

def test_multiplicacion():
    assert multiplicacion(2, 5) == 10

def test_division():
    assert division(20, 4) == 5