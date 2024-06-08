menu = """
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 0:
        valor = abs(float(input("Digite o valor: ")))
        saldo += valor
        print(f"Voce depositou R$ {valor} e o seu saldo atual é R$ {saldo}")
    elif opcao == 1:
        if numero_saques == LIMITE_SAQUES:
            print('Você já ultrapassou o limite de saques diários')
            continue

        valor = abs(float(input("Digite o valor: ")))

        if valor > 500:
            print('Valor do saque não pode ultrapassar R$ 500,00')
        elif valor <= saldo:
            saldo -= valor
            numero_saques += 1
            print(f"Voce sacou R$ {valor} e o seu saldo atual é R$ {saldo}")
        else:
            print('Ops! Verifique seu saldo')
    elif opcao == 2:
        print(f"Seu saldo atual é R$ {saldo}")
    elif opcao == 3:
        break
    else:
        print("Opção inválida, escolha uma opção inválida!")
