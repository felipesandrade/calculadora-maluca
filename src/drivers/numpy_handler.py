import numpy
from typing import List

# Utilizando biblioetecas externas de forma organizada
# Padrão de Projeto Facade
# Criando uma fachada para acessar uma biblioteca
class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)