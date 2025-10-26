from random import randrange
def validacoes(numero_escolhido, intervalo_maior, intervalo_menor, numeros_chutados = None, letras_chutadas = None):
    numeros = ' '
    for n in range(intervalo_maior):
        numeros = str(numeros) + ' 0' + str(n)
    if numero_escolhido in '0 1 2 3 4 5 6 7 8 9 ':
        numero_escolhido = ' 0' + numero_escolhido
    if not numero_escolhido in numeros:
        validacao = False
    elif int(numero_escolhido) >= intervalo_maior or int(numero_escolhido) <= intervalo_menor:
        validacao = False
    else:
        validacao = True

    if numeros_chutados is not None:
        if not numero_escolhido in numeros_chutados:
            validacao = False
    if letras_chutadas is not None:
        if numero_escolhido in letras_chutadas:
            validacao = True
    return validacao
##################################################################################
def continue_ou_pare():
            print('\n1.Continuar jogando;\n2.encerrar o jogo.') # saida das opções do usuário
            continuacao = input('Você quer jogar novamente esse jogo? Digite um número:') # (opcional) Entrada para saber se o usuário que jogar novamente ou quer encerrar o jogo
            jogando = True
            while not continuacao in '12':
                continuacao = input('Você quer jogar novamente esse jogo? Digite um número válido:')
            if continuacao == '1':
                jogando = True
            elif continuacao == '2':
                jogando = False
            return jogando
#####################################################################################
def imprime_mensagem_vencedor():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta = None):
    print('Puxa, Você perdeu!')
    if palavra_secreta is not None:
        print('A palavra era {}'.format(palavra_secreta))
    print(r"    __________________   ")
    print(r"   /                  \_ ")
    print(r"  /                   / \ ")
    print(r" //                   \ \ ")
    print(r" \|   XXXX     XXXX   | /")
    print(r"  |   XXXX     XXXX   |/ ")
    print(r"  |   XXX       XXX   |  ")
    print(r"  |                   |  ")
    print(r"  \__      XXX      __/  ")
    print(r"    |\     XXX     /|    ")
    print(r"    | |           | |    ")
    print(r"    | I I I I I I I |    ")
    print(r"    | I I I I I I I |    ")
    print(r"    \_             _/    ")
    print(r"      \_         _/      ")
    print(r"        \_______/        ")


def imprime_mensagem_abertura(mensagem):
    print('*' * (len(mensagem) + 4))
    print(f'*{mensagem:^{int(len(mensagem) + 2)}}*')
    print('*' * (len(mensagem) + 4))

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    dicas = []
    for linha in arquivo:
        linha = linha.split(':')
        palavras.append(linha[0].strip())
        dicas.append(linha[1].strip())
    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    dica = dicas[numero]

    return palavra_secreta, dica

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for _ in palavra_secreta]

def pede_chute():
    chute = input('Digite a letra: ').strip()
    return chute.lower()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1
    return letras_acertadas
###############################################################################
def imprime_nivel_dificuldade():
    nivel_l = ['NÍVEL FÁCIL', 'NÍVEL MÉDIO', 'NÍVEL DIFÍCIL']
    print('*' * 30)
    for n in range(3):
        print(f'*{f"{n + 1} = {nivel_l[n]}":<28}*')
    print('*' * 30)
    nivel = '0'
    while not nivel in '123':
        nivel = input('\nDigite o número válido do nível que você deseja jogar:')
    print('\n')
    imprime_mensagem_abertura(f"{nivel_l[int(nivel) - 1]}")
    return int(nivel)
###############################################################################
def forca(erros):
    forca = ['''
        ______
        |    |
        |
        |
        |
        |
        |
        |__________

        ''', '''
        ______
        |    |
        |    O
        |
        |
        |
        |
        |__________

        ''', '''
        ______
        |    |
        |    O
        |    |
        |    |
        |
        |
        |__________

        ''', '''
        ______
        |    |
        |    O
        |   /|
        |  / |
        |
        |__________

        ''', '''
        ______
        |    |
        |    O
        |   /|\\
        |  / | \\
        |
        |__________

        ''', '''
        ______
        |    |
        |    O
        |   /|\\
        |  / | \\
        |   /
        |  /
        |__________

        ''', '''
        ______
        |    |
        |    O
        |   /|\\
        |  / | \\
        |   / \\
        |  /   \\
        |__________
        Enforcou!
        ''']
    print(forca[erros])
#############################################################################