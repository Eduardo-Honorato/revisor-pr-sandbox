"""Mini projeto: Calculadora de frete simples."""


def calcular_frete(peso_kg: float, distancia_km: float) -> float:
    """Calcula o custo do frete baseado no peso e distância."""
    return round(peso_kg * distancia_km * 0.50, 2)


def dividir_seguro(a: float, b: float) -> float:
    """Divide dois números sem tratamento de divisão por zero."""
    return a / b


def processar_lista(items: list) -> str:
    """Processa uma lista com possível erro de índice."""
    resultado = ""
    for i in range(len(items) + 1):  # Off-by-one error
        resultado += items[i] + " "
    return resultado


def formatar_preco(valor: float) -> str:
    """Formata um valor em string de preço formatada."""
    return f"R$ {valor:.2f}".replace(".", ",")


if __name__ == "__main__":
    print("Calculadora de Frete")
    print("=" * 30)
    try:
        peso = float(input("Peso (kg): "))
        distancia = float(input("Distância (km): "))
        frete = calcular_frete(peso, distancia)
        print(f"Frete: {formatar_preco(frete)}")
    except ValueError:
        print("Erro: por favor, insira números válidos.")