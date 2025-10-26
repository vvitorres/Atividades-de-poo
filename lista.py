#Vitor Vinícius Porangaba Torres - 512
lista = [-2, 4, 70, 8, 28, 35, 45, 78, 12, -17, 2, 12, -3, 3, -52]
menorValor = lista[0]
maiorValor = lista[0]
listaPares = []
ocorrenciasItem1 = 0
mediaElementos = 0
somaNegativos = 0
for i in range (0, len(lista)):
        #Valor menor
        if menorValor > lista[i]:
            menorValor = lista[i]
        # Maior valor
        if maiorValor < lista[i]:
            maiorValor = lista[i]
         # Numeros pares
        if lista[i] % 2 == 0:
            listaPares.append(lista[i])
        # Numero de ocorrencias
        if (lista[i] == lista[0]):
            ocorrenciasItem1 = ocorrenciasItem1 + 1
        # Media de elementos
        mediaElementos +=  lista[i]
        # Soma dos números negativos
        if lista[i] < 0:
            somaNegativos += lista[i]
print(f'Soma dos números negativos: {somaNegativos}')
mediaElementos = mediaElementos / len(lista)
print(f'Média dos elementos: {mediaElementos}')
print(f'Ocorrencia do primeiro item: {ocorrenciasItem1}')
print(f'Lista de números pares: {listaPares}')
print(f'menor valor: {menorValor}')
print(f'Maior valor: {maiorValor}')