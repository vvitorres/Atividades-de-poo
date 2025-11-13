# Vitor Vinícius Porangaba Torres - 512

from conta import Conta, Cliente, Historico

cliente1 = Cliente("Vitor", "Torres", "111.222.333-44")
conta1 = Conta('123-45', cliente1, 120.0, 1000.0)

cliente2 = Cliente("Vinícius", "Porangaba", "555.666.777-88")
conta2 = Conta('678-90', cliente2, 300.0, 2000.0)

#print(conta1.__numero)
#print(conta1._Conta__numero)

conta1.saldo = 120
print(conta1.saldo)

conta1.saldo = -30