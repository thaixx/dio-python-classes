# fornece reutilização de código e é de natureza transitiva
# se a classe A herda B, todas subsclasses de A herda B

class Veiculo:
    def __init__(self, cor, placa, numero_rodas,):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        # 1 - pega o nome da class: 2 - usa o list compreehsion para passar por todos os atributos (itens) do dict
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if  self.carregado else 'Nao'} estou carregado")

moto = Motocicleta("Preta", "dom-1313", 2)
moto.ligar_motor()

carro = Carro("Prata", "HDZ - 1331", 4)
carro.ligar_motor()

caminhao = Caminhao("Azul", "trans- 3131", 8, "Sim")
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao) #chama o que ta no __str__ se usar o super na subclass
print(moto)
print(carro)