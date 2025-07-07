def sacar(valor):
    saldo = 1000
      # Exemplo de saldo disponível
    if saldo >= valor:
        print("Saque autorizado")
    else:
        print("Saque negado")
def depositar(valor):
    saldo = 1000
    # Exemplo de saldo disponível
    saldo += valor
    print(f"Depósito de {valor} realizado com sucesso. Saldo atual: {saldo}")


sacar(500)
depositar(200)

def maior_de_idade():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.Pode tirar carteira de motorista.")
    else:
        print("Você é menor de idade.Não pode tirar carteira de motorista.")

maior_de_idade()

def operacao_bancaria():
    print("Opção 1: Sacar")
    print("Opção 2: Depositar") 
    print("Opção 3: Transferir")
    saldo = 1000  # Exemplo de saldo disponível

    operacao = input("Escolha a operação (digite o número da opção): ")
    valor = float(input("Digite o valor da operação: "))

    if operacao == "1" and saldo >= valor:
        saldo -= valor
        print("Saque autorizado. Saldo atual:", saldo)
    elif operacao == "1":
        print("Saque negado. Saldo insuficiente.")
    elif operacao == "2":
        saldo += valor
        print("Depósito realizado com sucesso. Saldo atual:", saldo)
    elif operacao == "3" and saldo >= valor:
        saldo -= valor
        print("Transferência autorizada. Saldo atual:", saldo)
    elif operacao == "3":
        print("Transferência negada. Saldo insuficiente.")

operacao_bancaria()

def encontre_vogais(texto):

    vogais = "aeiouAEIOU"

    for letra in texto:
        if letra in vogais:
            print(f"A letra '{letra}' é uma vogal.")
        else:
            print(f"A letra '{letra}' não é uma vogal.")            

encontre_vogais("Python")

def tabuada(numero):
    for i in range(1, 11): # loop de 1 a 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabuada(5)

def tabuada_com_while(numero):
    i = 1
    while i <= 10:  # loop de 1 a 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1

tabuada_com_while(7)
