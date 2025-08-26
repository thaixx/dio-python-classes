class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade

    @classmethod
    def criar_apartir_nascimento(cls, ano, mes,dia, nome): #usa cls no lugar do self por causa do class method
        idade = 2025 - ano #estou criando a idade aqui e usando na parte de cima usando o classmethod 
        return cls(nome, idade) #lembrar do cls
    
    @staticmethod
    def e_maior_idade(idade): # nao precisa de contexto/class/ou instancia do objeto, é totalmente independente
        return idade >= 18 


p = Pessoa.criar_apartir_nascimento(1992,7,6,"Thaixx") #chamando o class method
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(33))
    
print(Pessoa.e_maior_idade(15))