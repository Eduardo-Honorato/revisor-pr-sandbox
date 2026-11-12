"""Testes unitários para a calculadora de frete."""


def test_calcular_frete_peso_distancia():
    """Testa cálculo de frete com peso e distância."""
    from src.calculator import calcular_frete
    resultado = calcular_frete(10.0, 100.0)
    assert resultado == 500.0, f"Esperava 500.0, got {resultado}"


def test_calcular_frete_zero_peso():
    """Testa frete com peso zero."""
    from src.calculator import calcular_frete
    resultado = calcular_frete(0.0, 100.0)
    assert resultado == 0.0, f"Esperava 0.0, got {resultado}"


def test_calcular_frete_zero_distancia():
    """Testa frete com distância zero."""
    from src.calculator import calcular_frete
    resultado = calcular_frete(10.0, 0.0)
    assert resultado == 0.0, f"Esperava 0.0, got {resultado}"


def test_formatar_preco():
    """Testa formatação de preço."""
    from src.calculator import formatar_preco
    assert formatar_preco(500.0) == "R$ 500,00"
    assert formatar_preco(0.0) == "R$ 0,00"