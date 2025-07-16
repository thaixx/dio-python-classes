#POO: classes + objetos
#classe: projeto da casa "a planta"
#objeto: a casa em si
#metodo = funçao dentro da class

class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Triiiim....triiiim")
    
    def parar(self):
        print("Parando a bicicleta")
    
    def correr(self):
        print("Vruuuumm ...")

    #def __str__(self):
    #    return f"Bicicleta: cor ={self.cor}, modelo={self.modelo} ..."
    #refazendo de maneira dinâmica:

    def __str__(self):
        # 1 - pega o nome da class: 2 - usa o list compreehsion para passar por todos os atributos (itens) do dict
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

    
    

bike1 = Bicicleta("vermelho", "caloi", 2022, 600)

bike1.buzinar() # == Bicicleta.buzinar(bike1)
bike1.correr()
bike1.parar()
print(bike1) # chama o str


