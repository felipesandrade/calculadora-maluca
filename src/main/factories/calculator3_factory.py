from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

# Factory Design Pattern
# Método para criação de objetos ao invés de chamar diretamente o construtor
def calculator3_factory():
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    return calc