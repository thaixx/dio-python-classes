#operadores aritméticos
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
divisao_inteira = 10 // 5
modulo = 10 % 5
exponenciacao = 10 ** 5 

#operadores de atribuição
a = 10
b = 5
a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a //= b  # a = a // b
a %= b  # a = a % b
a **= b  # a = a ** b   

#operadores de comparação
igual = (10 == 5)  # False
diferente = (10 != 5)  # True    
maior = (10 > 5)  # True
menor = (10 < 5)  # False
maior_igual = (10 >= 5)  # True
menor_igual = (10 <= 5)  # False 

#operadores lógicos
e = (10 > 5) and (5 < 10)  # True
ou = (10 > 5) or (5 > 10)  
nao = not (10 > 5)  # False

#operadores de identidade
is_a = (a is b)  # False
is_not_a = (a is not b)  # True

#operadores de associação
lista = [1, 2, 3, 4, 5]
pertence = (3 in lista)  # True
nao_pertence = (6 not in lista)  # True

string =  "curso de python"
pertence_string = ("py" in string)  # True
print(pertence_string)
nao_pertence_string = ("java" not in string)  # True    
