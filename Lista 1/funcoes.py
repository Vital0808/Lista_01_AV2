def exercicio1_divisao():
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return None

    if segundo_numero == 0:
        print("Não é possível dividir por zero!")
        return None

    resultado = primeiro_numero / segundo_numero
    print(f"Resultado da divisão: {resultado:.2f}")
    return resultado


def exercicio2_media():
    notas_texto = input("Digite as notas separadas por espaço: ").strip()
    if not notas_texto:
        print("Nenhuma nota informada.")
        return 0

    try:
        notas = [float(nota) for nota in notas_texto.split()]
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return None

    if not notas:
        return 0

    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
    return media


def exercicio3_carga_horaria():
    try:
        horas_trabalhadas = float(input("Digite as horas trabalhadas na semana: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return None

    resultado = "Carga completa" if horas_trabalhadas >= 40 else "Carga incompleta"
    print(resultado)
    return resultado


def exercicio4_saldo():
    try:
        saldo_atual = float(input("Digite o saldo atual: "))
        valor = float(input("Digite o valor da operação: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return None

    print("Escolha a operação:")
    print("1 - Depósito")
    print("2 - Saque")

    try:
        tipo_operacao = int(input("Digite 1 para depósito ou 2 para saque: "))
    except ValueError:
        print("Entrada inválida! Digite 1 para depósito ou 2 para saque.")
        return None

    if tipo_operacao == 1:
        saldo_final = saldo_atual + valor
    elif tipo_operacao == 2:
        saldo_final = saldo_atual - valor
    else:
        print("Operação inválida! Use 1 para depósito ou 2 para saque.")
        return None

    print(f"Saldo final: {saldo_final:.2f}")
    return saldo_final


def exercicio5_aprovados():
    notas_texto = input("Digite as notas separadas por espaço: ").strip()
    if not notas_texto:
        print("Nenhuma nota informada.")
        return []

    try:
        notas = [float(nota) for nota in notas_texto.split()]
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        return []

    aprovados = [nota for nota in notas if nota >= 7]
    print(f"Notas aprovadas: {aprovados}")
    return aprovados
