curso = "a PyThon b"
curso2 = "pythonclass"
print(curso.upper())  # Convierte a mayúsculas
print(curso.lower())  # Convierte a minúsculas
print(curso.title())  
print(curso.lstrip()) 
print(curso.rstrip())  # Elimina los espacios en blanco al final
print(curso.strip())   # Elimina los espacios en blanco al principio y al final
print(curso.center(20, "*"))  # Centra el texto en un ancho de 20 caracteres, rellenando con '*'
print(".".join(curso))  # Une los caracteres con un punto
print(list(curso))  # Convierte la cadena en una lista de caracteres

print(curso[0])
print(curso[:3])
print(curso[3:6])
print(curso[2:])
print(curso2[1:6:2]) #comneça no 1 termina no 6 e pula de 2 em 2
print(curso[:])
print(curso[::-1])

nome = "Thaixx"
idade = 33
profissao = "Programador"
linguagem = "Python"
print("Olá, me chamo %s, tenho %d ano e trabalho com %s de %s." % (nome, idade, profissao, linguagem))  # Formato antiguo
print("Olá, me chamo {}, tenho {} ano e trabalho com {} de {}.".format(nome, idade, profissao, linguagem))  # Formato con .format()
print(f"Olá, me chamo {nome}, tenho {idade} ano e trabalho com {profissao} de {linguagem}.")  # Formato con f-strings

pi = 3.14159
print(f"{pi:.2f}")  # Formato de número con dos decimales

#multiplas linhas
texto_multilinea = """Este es un texto
que ocupa varias líneas.
Puedes escribir lo que quieras aquí."""
print(texto_multilinea)
