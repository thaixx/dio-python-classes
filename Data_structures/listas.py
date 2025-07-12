frutas = ["maçã", "banana", "laranja"]
print(frutas)
print(frutas[0])
print(frutas[-1])
print(frutas[-3])

fruits = []
letras = list("maçã")
print(letras)
print(letras[2])
numeros = list(range(10))
carro = ["volkswagen", "fusca", 1969, True] #lista mista, todos atributos de um carro

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz)
print(matriz[0])  # Acessa a primeira lista
print(matriz[0][0]) # Acessa o primeiro elemento da primeira lista
print(matriz[0][-1]) #linha 0, último elemento
print(matriz[-1][-1])  # ultima linha, último elemento

lista = ["p","y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])  # Acessa os dois primeiros elementos
print(lista[1:3])  # Acessa do segundo ao terceiro elemento (3-1) o ultimo não é incluído
print(lista[0:4:2])  # Acessa do primeiro ao quarto elemento, pulando de 2 em 2
print(lista[::-1])  # Inverte a lista
print(lista[::]) # Acessa todos os elementos da lista

numbers = [1, 2, 3, 4, 5,6,7,8,9,10]

pares = [num for num in numbers if num % 2 == 0] #comprehension do for
print(pares)  # [2, 4, 6, 8, 10]
quadrado = [num ** 2 for num in numbers] #comprehension do for
print(quadrado)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list1 = [1, 2, 3]
list2 = list1.copy()  # Faz uma cópia da lista
list2.append(4)  # Adiciona um elemento à cópia
print(list1)  # [1, 2, 3]
print(list2)  # [1, 2, 3, 4]

linguagens = ["python", "java", "c++"]
linguagens.extend(["javascript", "c#"])  # Adiciona vários elementos ao final da lista
print(linguagens)  # ['python', 'java', 'c++', 'javascript', 'c#']
linguagens.extend(["ruby", "c++"])# Adiciona elementos repetidos
print(linguagens)  

linguagens.append("go")   
print(linguagens)
linguagens.pop()
print(linguagens)  
linguagens.pop(0)  # Remove o primeiro elemento
print(linguagens)  
linguagens.remove("c++")  # Remove o primeiro elemento encontrado
print(linguagens)

linguagens.sort()  # Ordena a lista em ordem alfabética
print(linguagens)  
linguagens.sort(reverse=True)  # Ordena a lista em ordem alfabética reversa
print(linguagens)   
linguagens.sort(key=len)  # Ordena a lista pelo tamanho das strings
print(linguagens)  # Ordena por tamanho das strings
linguagens.sort(key=len, reverse=True)  # Ordena a lista pelo tamanho das strings em ordem decrescente
print(linguagens)  # Ordena por tamanho das strings em ordem decrescente    

size = len(linguagens)  # Retorna o tamanho da lista
print(size)  # Exibe o tamanho da lista
linguagens.clear()  # Limpa todos os elementos da lista
print(linguagens)  # Exibe a lista vazia