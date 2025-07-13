def exemplo_funcao(param1, param2):
    resultado = param1 + param2
    return resultado

print(exemplo_funcao(5, 10))

def calcular_total(numeros):
    return sum(numeros)

print(calcular_total([1, 2, 3, 4, 5]))

def antecessor_sucessor(numero):
    return numero - 1, numero + 1

print(antecessor_sucessor(10))  

def salvar_carro(marca, modelo, ano):
    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano
    }
    return carro

print(salvar_carro("Ford", "Mustang", 2020))

#args e **kwargs
def funcao_exemplo(*args, **kwargs):
    print("Argumentos posicionais:", args)  #args é uma tupla
    print("Argumentos nomeados:", kwargs)   #kwargs é um dicionário

funcao_exemplo(1, 2, 3, nome="João", idade=30)

#exemplo com /  e * 
def funcao_exemplo2(arg1, arg2, /, arg3, arg4, *, arg5):
    print("Argumentos:", arg1, arg2, arg3, arg4, arg5)
funcao_exemplo2(1, 2, 3, 4, arg5=5)  # arg1 e arg2 são posicionais obrigatórios, arg3 e arg4 são posicionais opcionais, arg5 é nomeado obrigatório

def somar(a, b):
    return a + b

def exibir_resultado(a,b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é: {resultado}")
exibir_resultado(5, 10, somar)

#variavel global:

salario = 1000

def salario_com_bonus(bonus):
    global salario  # Acessa a variável global
    salario += bonus
    return salario

print(salario_com_bonus(200))  # Imprime 1200
