import textwrap

def menu():
    menu = """"\n
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques > limite_saques

     if excedeu_saldo:
         print("Operação falhou, você não tem saldo o suficiente")
     elif excedeu_limite:
         print("Operação falhou, o valor do saque excede o limite")
     elif excedeu_saques:
         print("Operação falhou, você excedeu o limite de saques")

     elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n" #imprimi com duas casas decimais
        numero_saques += 1
        print("Saque realizado com sucesso!")
     else:
        print("Operação falhou! O valor informado é inválido")
     return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("=== Extrato ===")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Já existe um usuário com essse CPF!")
        return
    nome = input("Informe seu nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço completo")

    usuarios.append({"nome": nome,
                     "data_nascimento": data_nascimento,
                     "cpf": cpf,
                     "endereco": endereco})
    print("Usuário criado com sucesso")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF:")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia" : agencia,
                "numero_conta":numero_conta,
                "usuario": usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas): 
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular: \t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def operacao_bancaria():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 1000
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES, 
            )
           
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

operacao_bancaria()