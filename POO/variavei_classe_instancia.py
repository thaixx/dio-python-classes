class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula ):
        self.nome = nome 
        self.matricula = matricula

    
    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovana", 2)

print(aluno_1)
print(aluno_2)

aluno_1.matricula = 3 #nao influencia no aluno_2 (variavel de instancia) cada objetivo tem uma copia da variavel

print(aluno_1)
print(aluno_2)

Estudante.escola = "Python" # muda em todos os alunos (variavel da classe(ESTUDANTE))

print(aluno_1)
print(aluno_2)