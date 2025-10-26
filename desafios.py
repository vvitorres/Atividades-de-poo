lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

#a)
print(f'Maior número da lista: {max(lista)}')

#b)
print(f'Menor número da lista: {min(lista)}')

#c)
pares = []
for i in lista:
    if i % 2 == 0:
        pares.append(i)
print(f"Numeros páres: {''.join(str(pares))}")

#d)
elemento = lista[0]
print(f'Repetições doprimeiro elemento: {lista.count(elemento)}')

#e)
numero_elementos = len(lista)
soma = 0
for i in lista:
    soma += i
media = soma/numero_elementos
print(f'Média: {media}')

#f)
soma_negativa = 0
for i in lista:
    if i < 0:
        soma_negativa += i
print(f'Soma Negativa: {soma_negativa}')