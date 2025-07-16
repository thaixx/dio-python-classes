#__init__ ou __del__ 
#Métodos especiais usam o __

class Cachorro:
    #constrói as características da classe
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado


#__del__ é usado para destruir um objeto que não será mais útil, mas o pyhton normalmente faz isso automaticamente

    def __del__(self):
        print("Destruindo a instância")
    
    def latir(self):
        print("Rouff")
    
    
cao = Cachorro("Tasha", "Preta")
cao.latir()


