#Descreve a ideia de agrupar dados e métodos, para evitar alterações acidentais
#self._saldo = saldo > significa privado porque usa o (_)
#depurador > @ funçao que executa antes da sua função

class Conta:
    def __init__(self, agencia, saldo = 0):
        self._saldo = saldo
        self.agencia = agencia
    
    def depositar(self, valor):
        self._saldo += valor
    def sacar(self, valor):
        self._saldo -= valor

    @property #permite executar como sintaxe de atributo nao precisa usar () depois do mostrar saldo
    def mostrar_saldo(self):
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.agencia)
print(conta.mostrar_saldo) #é possivel executar assim por causa do property


