class Animal():
    def __init__(self, numero_patas, ):
        self.numero_patas = numero_patas

    def __str__(self):
        # 1 - pega o nome da class: 2 - usa o list compreehsion para passar por todos os atributos (itens) do dict
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass
class Gato(Mamifero):
    pass
class Leao(Mamifero):
    pass
class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(numero_patas = 4,cor_pelo= "preto")
print(gato)

ornito = Ornitorrinco(numero_patas = 2,cor_pelo="Marrom", cor_bico="Amarelo")
print(ornito)