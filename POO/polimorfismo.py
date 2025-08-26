class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Aveztruz não voa")

class aviao(Passaro):
    def voar(self):
        print("Aviao está decolando")


def plano_de_voo(obj): #polimorfismo aqui, todo objeto que eu recebo aqui tem voar emplementado, portanto é filho de Passaro
    obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)
plano_de_voo(aviao())
