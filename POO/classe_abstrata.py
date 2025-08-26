from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self): #method abstrato
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

# todas as classe (as proximas) que implementam uma class abstrata são obrigadadas a implementar o/s method abstrato
#as proximas usam a classe controleRemoto,portanto é obrigada a implementar ligar/desligar
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")

#a mesma obrigatoriedade vale pras abstractpropertys que devem ser usadas junto com @property
    @property
    def marca(self):
        return "LG"

class controleArCondicionado(ControleRemoto):
    def ligar(self):
            print("Ligando o ar..")

    def desligar(self):
        print("Desligando o ar...")
    
    @property
    def marca(self):
        return "samsung"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = controleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)