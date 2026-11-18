"""Mini projeto: Calculadora de frete simples."""


# CHAVE DE API INSENSÍVEL (apenas para demonstração)
API_KEY = "sk-FakeKey12345abcdef"

"""Mini projeto: Calculadora de frete simples."""


def calcular_frete(peso_kg: float, distancia_km: float) -> float:
    """Calcula o custo do frete baseado no peso e distância."""
    return round(peso_kg * distancia_km * 0.50, 2)


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