# Vitor Vinícius Porangaba Torres - 512

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
    
    def extrato(self):
        print(f"numero: {self.numero} \nsaldo: {self.saldo}")