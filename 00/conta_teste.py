# Vitor Vinícius Porangaba Torres - 512

from conta import Conta, Cliente, Historico

cliente1 = Cliente("Vitor", "Torres", "111.222.333-44")
conta1 = Conta('123-45', cliente1, 120.0, 1000.0)

cliente2 = Cliente("Vinícius", "Porangaba", "555.666.777-88")
conta2 = Conta('678-90', cliente2, 300.0, 2000.0)

conta1.deposita(1000)
conta1.extrato(cliente1)
conta1.saca(200)
conta1.extrato(cliente1)
conta2.deposita(50)
conta2.extrato(cliente2)
conta2.saca(300)
conta2.extrato(cliente2)
conta1.transfere_para(conta2, 200)
conta1.historico.imprime(conta1.numero)
conta1.extrato(cliente1)
conta2.historico.imprime(conta2.numero)
conta2.extrato(cliente2)