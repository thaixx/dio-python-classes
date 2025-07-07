preco = 10
idade = 28
print(type(preco))  # Exibindo o tipo da variável preco
print(preco)  # Exibindo o valor da variável preco
preco = float(preco)  # Convertendo inteiro para float
print(type(preco))  # Exibindo o tipo da variável preco após conversão
print(preco)  # Exibindo o valor da variável preco após conversão


texto = f"idade {idade} preco {preco}"
print(texto)  # Exibindo o texto formatado com idade e preco
texto = "idade " + str(idade) + " preco " + str(preco)
print(texto)  # Exibindo o texto formatado com idade e preco usando concatenação

numero = "13"
print(type(numero))  # Exibindo o tipo da variável string
print(numero)  # Exibindo o valor da variável numero
numero = int(numero)  # Convertendo string para inteiro
print(type(numero))  # Exibindo o tipo da variável numero após conversão
print(numero)  # Exibindo o valor da variável numero após conversão


nome = input("informe seu nome:")  # Lendo o nome do usuário
age= input("informe sua idade:")  # Lendo a idade do usuário
print(f"Olá {nome}, seja bem-vindo(a)!" "\n" f"Você tem {age} anos.")  # Exibindo uma mensagem de boas-vindas com o nome do usuário