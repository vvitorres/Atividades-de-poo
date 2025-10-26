#Vitor Vinícius Porangaba Torres - 512
import funcoes
def jogar():
    import random
    print('*' * 70)
    print(f"*{'Jogo da forca':^68}*")
    print('*' * 70, '\n')
    jogando = True
    while (jogando):
        erros = 0
        palavras = [
            'otorrinolaringologista', 'anticonstitucionalissimamente', 'inconstitucionalidade',
            'hipopotomonstrosesquipedaliofobia',
            'hexakosioihexekontahexafobia', 'paralelepipedo', 'interdisciplinaridade', 'esdruxulo', 'heterocromia',
            'circunlocucao',
            'proparoxitona', 'idiossincrasia', 'metamorfose', 'claustrofobia', 'concomitante',
            'inexoravel', 'irrefutavel', 'inefavel', 'peremptorio', 'onipresente',
            'obnubilar', 'subrepticio', 'cacofonia', 'pusilanime', 'pernicioso',
            'ultracrepidario', 'vicissitude', 'epistemologia', 'procrastinar', 'heuristica',
            'demagogia', 'ignominia', 'misantropo', 'soliloquio', 'prolegomeno',
            'panaceia', 'contumelia', 'recalcitrante', 'estapafurdio', 'incognoscivel',
            'nefando', 'abnegacao', 'perscrutar', 'imperturbavel', 'inequivoco',
            'obsequioso', 'alvitre', 'emulacao', 'logomaquia', 'desiderato'
        ]

        dicas = [
            'Medico especializado em ouvidos, nariz e garganta',
            'De maneira extremamente contra a constituicao',
            'Qualidade de algo que fere a constituicao',
            'Medo irracional de palavras muito grandes',
            'Medo do numero 666',
            'Solido com varias faces retangulares',
            'Ligacao entre diversas areas do conhecimento',
            'Muito estranho ou fora do comum',
            'Diferenca na cor dos olhos',
            'Forma de se expressar de modo indireto',
            'Palavra com acento na antepenultima silaba',
            'Caracteristica propria de um individuo',
            'Transformacao profunda na forma ou estado',
            'Medo de espacos fechados',
            'Que ocorre ao mesmo tempo',
            'Que nao pode ser evitado ou parado',
            'Que nao pode ser negado logicamente',
            'Tao belo ou intenso que nao pode ser descrito',
            'Que tem efeito definitivo e final',
            'Presente em todos os lugares',
            'Tornar a mente ou vista confusa',
            'Feito de modo escondido ou dissimulado',
            'Som desagradavel causado por combinacoes de palavras',
            'Pessoa covarde ou sem coragem',
            'Extremamente prejudicial ou maligno',
            'Pessoa que opina sem ter conhecimento',
            'Mudanca inesperada ou reviravolta',
            'Estudo filosofico do conhecimento',
            'Ato de adiar algo continuamente',
            'Metodo de descoberta por tentativa e erro',
            'Manipulacao do povo por meio de discursos',
            'Grande desonra publica',
            'Pessoa que evita o convívio social',
            'Ato de falar sozinho',
            'Texto introdutorio de uma obra',
            'Cura imaginaria para todos os males',
            'Ofensa verbal grave e humilhante',
            'Teimoso ou resistente a mudancas',
            'Totalmente absurdo ou sem sentido',
            'Que nao pode ser conhecido ou compreendido',
            'Que causa repulsa ou e moralmente condenavel',
            'Renuncia ao interesse proprio em favor de outro',
            'Investigar com muito cuidado e profundidade',
            'Que nao perde a calma com facilidade',
            'Que nao deixa duvidas',
            'Pessoa extremamente servil ou bajuladora',
            'Conselho, sugestao ou proposta',
            'Ato de tentar superar ou igualar algo ou alguem',
            'Discussao baseada em palavras vazias ou jogos verbais',
            'Desejo intenso ou aspiracao profunda'
        ]

        funcoes.forca(erros)
        lchutadas = []
        palavra = random.choice(palavras)
        pposicao = 0
        for i in palavras:
            if str(i).upper() == str(palavra).upper():
                posicao_palavra = pposicao
            pposicao += 1
        letras = []
        for i in palavra:
            for letra in i:
                letras.append('_')
        print(" ".join(letras))
        enforcou = False
        acertou = False
        erros = 0
        while (not enforcou and not acertou):

            chute = input('\nDigite uma letra ou tente acertar a palavra: ')
            if len(chute) > 1:
                if chute.upper() == palavra.upper():
                    acertou = True
                else:
                    enforcou = True
            else:
                while chute.upper() in str(lchutadas).upper():
                    chute = input('\nDigite uma letra que não tenha sido digitada: ')
                lchutadas.append(chute)
                if chute.upper() in str(palavra).upper():
                    posicao = 0
                    for i in palavra:
                        if chute.upper() == i.upper():
                            letras[posicao] = i
                        posicao += 1
                else:
                    erros += 1
                    print(f'Você errou, agora você tem {6 - erros} chances')

                    funcoes.forca(erros)  # Retorna a função que mostra a forca

                    if erros == 5:
                        print(f'Dica: {dicas[posicao_palavra]}!\n')
                enforcou = erros == 6
                acertou = '_' not in letras
                print(" ".join(letras))
                print(f'\nVocê já chutou essas letras: {", ".join(lchutadas)}.\n')
        if (acertou):
            print('Você ganhou!')
            dicas.pop(posicao_palavra)
            palavras.pop(posicao_palavra)
        elif (enforcou):
            print('Você perdeu')
            print(f'A palavra é: {palavra}')
        dicas.pop(posicao_palavra)
        palavras.pop(posicao_palavra)

        jogando = funcoes.continue_ou_pare()
    print('\nFim de jogo.')