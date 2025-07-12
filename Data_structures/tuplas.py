frutas = ("maçã", "banana", "laranja",)
letras = tuple("maçã")
print(frutas)
print(letras)
numeros = tuple(range(10))
print(numeros)
pais = ("Brasil",)
print(pais)

#comportamento semelhante às listas
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(matriz)
print(matriz[0])  # Acessa a primeira tupla
print(matriz[0][0]) # Acessa o primeiro elemento da primeira tupla      
print(matriz[0][-1]) #linha 0, último elemento
print(matriz[-1][-1])  # ultima linha, último elemento

lista = ("p", "y", "t", "h", "o", "n")
print(lista[2:])
print(lista[:2])  # Acessa os dois primeiros elementos
print(lista[1:3])  # Acessa do segundo ao terceiro elemento (3-1) o ultimo não é incluído
print(lista[0:4:2])  # Acessa do primeiro ao quarto elemento, pulando de 2 em 2
print(lista[::-1])  # Inverte a tupla
print(lista[::]) # Acessa todos os elementos da tupla

#usar tuplas quando não se deseja alterar os dados<<<<<<<

cores = ("vermelho", "verde", "azul")
print(cores)
size = len(cores)  # Tamanho da tupla
print(size)  # 3
cores.count("verde")  # Conta quantas vezes "verde" aparece
print(cores.count("verde"))  # 1
cores.index("azul")  # Retorna o índice do primeiro elemento "azul"
print(cores.index("azul"))  # 2 

# Tuplas são imutáveis, não podem ser alteradas após a criação
# cores[0] = "amarelo"  # Isso causaria um erro, pois tuplas não suportam atribuição de novos valores
