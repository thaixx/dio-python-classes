menu = """"
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        if numero_saques < LIMITE_SAQUES and valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n" #imprimi com duas casas decimais
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Limite de saques atingido ou saldo insuficiente.")
    elif opcao == "3":
        print("=== Extrato ===")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
