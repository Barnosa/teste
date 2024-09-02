def tarefa1_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    print("Soma:", SOMA)


def tarefa2_fibonacci():
    def is_fibonacci(n):
        if n < 0:
            return False
        a, b = 0, 1
        while a < n:
            a, b = b, a + b
        return a == n

    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    if is_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")


def tarefa3_faturamento():
    import json

    data = {
        "dias": [
            {"dia": 1, "valor": 150.0},
            {"dia": 2, "valor": 200.0},
            {"dia": 3, "valor": 0.0},
            {"dia": 4, "valor": 300.0},
            {"dia": 5, "valor": 250.0},
            # Adicione mais dias conforme necessário
        ]
    }

    valores = [dia['valor'] for dia in data['dias'] if dia['valor'] > 0]

    if not valores:
        print("Não há dados de faturamento para análise.")
    else:
        menor_valor = min(valores)
        maior_valor = max(valores)
        media_mensal = sum(valores) / len(valores)

        dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

        print(f"Menor valor de faturamento: R${menor_valor:.2f}")
        print(f"Maior valor de faturamento: R${maior_valor:.2f}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")


def tarefa4_percentual():
    faturamento = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total = sum(faturamento.values())

    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")


def tarefa5_inverter_string():
    def inverter_string(s):
        resultado = ''
        for char in s:
            resultado = char + resultado
        return resultado

    entrada = input("Digite uma string para inverter: ")
    print("String invertida:", inverter_string(entrada))


def main():
    print("Escolha a tarefa a ser executada:")
    print("1 - Cálculo da soma")
    print("2 - Verificação na sequência de Fibonacci")
    print("3 - Análise de faturamento diário")
    print("4 - Percentual de representação por estado")
    print("5 - Inversão de string")

    escolha = int(input("Digite o número da tarefa desejada: "))

    if escolha == 1:
        tarefa1_soma()
    elif escolha == 2:
        tarefa2_fibonacci()
    elif escolha == 3:
        tarefa3_faturamento()
    elif escolha == 4:
        tarefa4_percentual()
    elif escolha == 5:
        tarefa5_inverter_string()
    else:
        print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()
