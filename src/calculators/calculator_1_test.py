from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={ "number": 1 })
    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)
    
    # Em testes unitários duas coisas precisam ser testadas
    # Formato
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 14.25
    assert response["data"]["calculator"] == 1

# Teste de erro
def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "something": 1 })
    calculator_1 = Calculator1()

    # Verifica se o erro acontece
    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    # Verifica se o valor do erro ocorrido é igual
    assert str(excinfo.value) == 'body mal formatado!'
