from funcoes import validacoes
palavras = ['casa', 'abacaxi', 'ignorante']
indice = {}
posicao = []
caracteres = []
n = 0
for palavra in palavras:
    caracteres.append(len(palavra))
    for letras in palavra:
        indice[n] = letras
        if n > 0 and indice[n - 1] == letras:
            continue
        posicao.append([n])
        n += 1
n = -1
print('☻')
print(' |-É onde moramos\n v')
for i in posicao:
    n += 1
    if n < (caracteres[0]-1):
        print(i)
    elif n < (caracteres[1]+caracteres[0]-1):
        print(i, end='')
        if n == (caracteres[1]+2):
          print(' <-É uma fruta rainha')
    elif n < (caracteres[2]+caracteres[1]+caracteres[0]-1):
        print(' ', '   ' * (caracteres[1]-2), i)
jogando = True
erros = 0
max_acertos = n
while jogando:
    escolha = input(f'\nDigite o número da letra que você quer digitar: ')
    validacao = validacoes(escolha, n, -1)
    while not validacao:
        escolha =  input('Escolha um número que esteja sendo apresentado: ')
        validacao = validacoes(escolha, n, -1)
    escolha = int(escolha)

    chute = input('Digite a letra: ')

    if indice[escolha] == chute:
        n = -1
        posicao[escolha] = [chute]
        max_acertos -= 1
        print(' |-É onde moramos\n v')
        for i in posicao:
            n += 1
            if n < (caracteres[0] - 1):
                print(i)
            elif n < (caracteres[1] + caracteres[0] - 1):
                print(i, end='')
                if n == (caracteres[1] + 2):
                    print(' <-É uma fruta rainha')
            elif n < (caracteres[2] + caracteres[1] + caracteres[0] - 1):
                print(' ', '   ' * (caracteres[1] - 2), i)

    else:
        erros += 1
        print('Você errou a letra.')
    if erros == 5:
        print('Você Perdeu!')
        jogando = False
    elif max_acertos == -1:
        print('Você Ganhou!')
        jogando = False
print('Fim de jogo')