from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

# Factory Design Pattern
# Método para criação de objetos ao invés de chamar diretamente o construtor
def calculator2_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    return calc