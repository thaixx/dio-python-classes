num = set([1,2,3,1,3,4])
print(num)
letras = set("abacaxi")
print(letras)   
carros = set(["fusca", "civic", "civic", "civic", "civic"])
print(carros)
print(len(carros))
print("civic" in carros)
print("civic" not in carros)
print("civic" in carros and "fusca" in carros)

#set não tem index

numeros = {1, 2, 3, 4, 5}
print(numeros)
#pode iterar normalmente
for numero in numeros:
    print(numero)
    
numeros = list(numeros)
print(numeros)
print(numeros[0])

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
conjunto_uniao = conjunto_a.union(conjunto_b)
print(conjunto_uniao)
conjunto_intersecao = conjunto_a.intersection(conjunto_b)
print(conjunto_intersecao)
conjunto_diferenca_a = conjunto_a.difference(conjunto_b)
print(conjunto_diferenca_a)
conjunto_diferenca_b = conjunto_b.difference(conjunto_a)
print(conjunto_diferenca_b)
conjunto_diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b) #diferenca dos 2 conjuntos
print(conjunto_diferenca_simetrica)

conjunto_a.add(4)  # adiciona um elemento
conjunto_a.add(5)  # adiciona outro elemento
print(conjunto_a)
conjunto_b.issubset(conjunto_a)  # verifica se conjunto_b é subconjunto de conjunto_a
print(conjunto_b.issubset(conjunto_a))  # True
conjunto_a.issuperset(conjunto_b)  # verifica se conjunto_a é superconjunto de conjunto_b
print(conjunto_a.issuperset(conjunto_b))  # True
conjunto_a.clear()  # limpa todos os elementos do conjunto_a        
print(conjunto_a)  # Conjunto vazio

conjunto_a.isdisjoint(conjunto_b)  # verifica se os conjuntos não têm elementos em comum
print(conjunto_a.isdisjoint(conjunto_b))  # True, pois conjunto_a está vazio
conjunto_b.isdisjoint(conjunto_a)  # verifica se os conjuntos não têm elementos em comum
print(conjunto_b.isdisjoint(conjunto_a))  # True, pois conjunto_a está vazio

conjunto_c = conjunto_b.copy()  # cria uma cópia do conjunto_b
conjunto_c.add(7)
print(conjunto_c)  # {3, 4, 5}

conjunto_c.remove(3)  # remove o elemento 3 do conjunto_c
print(conjunto_c)  # {4, 5}
  # adiciona o elemento 7, mas não gera erro se já existir
conjunto_c.discard(4)  # remove o elemento 4 do conjunto_c, mas não gera erro se o elemento não existir
print(conjunto_c)  # {5, 7}
conjunto_c.pop()  # remove e retorna um elemento aleatório do conjunto_c
print(conjunto_c)  # {7} ou {5}, dependendo do elemento removido








