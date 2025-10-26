from random import choice, randrange
def validacoes(numero_escolhido, intervalo_maior, intervalo_menor, numeros_chutados = None):
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
    return validacao
#################################################################################
def criptografia(dicas, casas, caracteres):
    n = -1
    for dica in dicas:
        n += 1
        tamanho = 0
        print(f'\n {dicas[n]:-<45}>', end = '')
        for casa in casas:
            tamanho += 1
            if caracteres[n]*n < tamanho and caracteres[n]*(n+1) >= tamanho:
                print(f'[{casa:^3}]', end = '')
##################################################################################
def continue_ou_pare():
            print('\n1.Continuar jogando;\n2.encerrar o jogo.') # saida das opções do usuário
            continuacao = input('Você quer jogar novamente esse jogo? Digite um número:') # (opcional) Entrada para saber se o usuário que jogar novamente ou quer encerrar o jogo
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
    print('*' * 30)
    print(f'*{mensagem:^28}*')
    print('*' * 30)

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

    return (palavra_secreta, dica)

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for i in palavra_secreta]

def pede_chute():
    chute = input('Digite a letra: ').strip()
    return chute.lower()

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
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
def escolha_nivel_dicas(nivel):
        if nivel == '1':
            dicas_1 = [
                'Peças femininas do xadrez -> ',
                'Causar emocao -> ',
                'Adubo natural -> ',
                'Propriedade rural pequena -> ',
                'Grande felino -> ',
                'Planeta vermelho -> ',
                'Instrumento de corda -> ',
                'Instrumento de teclas -> ',
                'Area da saude -> ',
                'Prato japones -> ',
                'Peixe comum -> ',
                'Inseto que voa -> ',
                'Direcao por sol poente -> ',
                'Astro que brilha -> ',
                'Quem joga tenis -> ',
                'Metal branco comum -> ',
                'Lugar com lobos (canil) -> ',
                'Cor da grama -> ',
                'Veiculo -> ',
                'Parte do computador (entrada) -> ',
                'Quem ensina em sala -> ',
                'Mes com festas -> ',
                'Cidade italiana famosa -> ',
                'Ave noturna -> ',
                'Fruta tropical doce -> ',
                'Local com muitos ossos -> ',
                'Parente por sangue -> ',
                'Parente por casamento -> ',
                'Membro do clero -> ',
                'Objeto que ilumina -> ',
                'Inseto pequeno -> ',
                'Pais africano -> ',
                'Animal que mia -> ',
                'Planeta com aneis (alternativo) -> ',
                'Objeto para cortar (ferramenta) -> ',
                'Gas (categoria) -> ',
                'Cidade espanhola -> ',
                'Objeto de leitura -> ',
                'Porta ou entrada -> ',
                'Instituicao financeira -> ',
                'Local de banho de mar -> ',
                'Terreno rural -> ',
                'Arquipelago pequeno -> ',
                'Animal pequeno -> ',
                'Animal aquático comum -> ',
                'Formacao no ceu -> ',
                'Movimento do ar -> ',
                'Local ou posicao -> ',
                'Evento festivo -> ',
                'Pessoa proxima (amigo) -> ',
                'Marca as horas -> ',
                'Atividade de relaxar/alongar -> ',
                'Profissional do direito -> ',
                'Aglomerado cosmico -> ']
        elif nivel == '2':
            # nível médio
            dicas_1 = [
                'Damas do xadrez -> ',
                'Emocionar -> ',
                'Adubo constituído em geral de esterco -> ',
                'Propriedade Rural -> ',
                'Grande felino -> ',
                'Corpo celeste como a Terra -> ',
                'Instrumento de corda clássico -> ',
                'Profissionais da saúde -> ',
                'Arte de preparar comida -> ',
                'Peixe comum em pizzas -> ',
                'Insetos que produzem mel -> ',
                'Oceano ao sul da Ásia -> ',
                'Astro que emite luz -> ',
                'Rei dos deuses romanos -> ',
                'Quem joga tênis -> ',
                'Metal prateado macio -> ',
                'Animal da família dos cães -> ',
                'Cor do centro da bandeira do Brasil -> ',
                'Transporte para estudantes -> ',
                'Parte do computador -> ',
                'Educador formal -> ',
                'Mês das crianças no Brasil -> ',
                'Cidade italiana famosa -> ',
                'Ave noturna de olhos grandes -> ',
                'Fruta com coroa -> ',
                'Lugar de muitos ossos -> ',
                'Habitante do sul -> ',
                'Parente por casamento -> ',
                'Membro do clero -> ',
                'Objeto que ilumina -> ',
                'Inseto que pode ferrar -> ',
                'País mais populoso da África -> ',
                'Animal que mia -> ',
                'Planeta com anéis -> ',
                'Objeto que corta papel -> ',
                'Gás vital para humanos -> ',
                'Cidade da Andaluzia -> ',
                'Músico que toca oboé -> ',
                'Deserto no Chile -> ',
                'Resumo do conteúdo -> ',
                'Sede africana da ONU -> ',
                'Animal com listras -> ',
                'Refeição do meio-dia -> ',
                'Lugar para cultos -> ',
                'Embarcações grandes -> ',
                'Grandes cetáceos -> ',
                'Ferramenta de escrita -> ',
                'Pequeno roedor doméstico -> ',
                'Réptil comum no deserto -> ',
                'Prateleira de livros -> ',
                'Objeto de medir tempo -> ',
                'Exercício para esticar -> ',
                'Profissional do direito -> ',
                'Sistema de estrelas -> ']
        elif nivel == '3':
            # Nível difícil
            dicas_1 = [
                "Persistência diante de dificuldades -> ",
                "Que retorna ao estado anterior -> ",
                "Expressões de pesar -> ",
                "Prerrogativa ou privilégio legal -> ",
                "Pessoa sociável e expansiva -> ",
                "Atitude de satisfação consigo mesmo -> ",
                "Ato de adiar tarefas -> ",
                "Desproporção ou dessemelhança -> ",
                "Ato de firmar decisão, determinação -> ",
                "Que não depende de outro -> ",
                "Efeito causado por ato anterior -> ",
                "Que ocorre com intervalos -> ",
                "Conveniência ou utilidade -> ",
                "Ato de repartir ou dividir algo -> ",
                "Atitude benevolente, caridosa -> ",
                "Situação imprevista, eventualidade -> ",
                "Relativo ao clero ou igreja -> ",
                "Ato de transgredir normas -> ",
                "Ato de considerar, estimar -> ",
                "Expressões de parabéns -> ",
                "Que ocorre ao mesmo tempo -> ",
                "Aproximação de direções ou ideias -> ",
                "Soma de saber; conhecimento -> ",
                "Qualidade cordial, afetuosa -> ",
                "Complicidade entre pessoas -> ",
                "Que segue tradições; convencional -> ",
                "Manutenção de existência; subsistir -> ",
                "Atividade de converter alguém (relig.) -> ",
                "Propagação ou espalhamento -> ",
                "Ocorrência por acaso -> ",
                "Organizar em sistema, sistematizar -> ",
                "Complexidade; caráter complexo -> ",
                "Falta de tolerância -> ",
                "Que não é interrompido -> ",
                "Quem não cumpre pagamento -> ",
                "Atividade de globalizar -> ",
                "Ato de formalizar -> ",
                "Ato de objetivar -> ",
                "Profissão de cabeleireiro -> ",
                "Estudo de fenômenos naturais -> "]
        return dicas_1


def escolha_nivel_palavras(nivel):
    if nivel == '1':
        palavras_1 = [  # Palavras com 5 letras
            'damas',  # 01
            'tocar',  # 02
            'adubo',  # 03
            'sitio',  # 04
            'tigre',  # 05
            'marte',  # 06
            'viola',  # 07
            'piano',  # 08
            'saude',  # 09
            'sushi',  # 10
            'atuns',  # 11
            'mosca',  # 12
            'oeste',  # 13
            'astro',  # 14
            'tenis',  # 15
            'prata',  # 16
            'canil',  # 17
            'verde',  # 18
            'carro',  # 19
            'mouse',  # 20
            'tutor',  # 21
            'junho',  # 22
            'milao',  # 23
            'mocho',  # 24
            'manga',  # 25
            'ossos',  # 26
            'irmao',  # 27
            'sogra',  # 28
            'padre',  # 29
            'farol',  # 30
            'pulga',  # 31
            'egito',  # 32
            'gatos',  # 33
            'urano',  # 34
            'serra',  # 35
            'gases',  # 36
            'cadiz',  # 37
            'livro',  # 38
            'porta',  # 39
            'banco',  # 40
            'praia',  # 41
            'campo',  # 42
            'ilhas',  # 43
            'bicho',  # 44
            'peixe',  # 45
            'nuvem',  # 46
            'vento',  # 47
            'lugar',  # 48
            'festa',  # 49
            'amigo',  # 50
            'horas',  # 51
            'yogas',  # 52  (plural comum de "yoga", usado como atividade/estilos)
            'juiza',  # 53  (forma sem acento de 'juíza' — 5 letras sem acento)
            'cosmo']  # 54
    elif nivel == '2':
        # nível médio
        palavras_1 = [  # palavras com 7 letras
            'rainhas',
            'comover',
            'estrume',
            'fazenda',
            'pantera',
            'planeta',
            'violino',
            'medicos',
            'cozinha',
            'anchova',
            'abelhas',
            'indiano',
            'estrela',
            'jupiter',
            'tenista',
            'estanho',
            'canideo',
            'amarelo',
            'escolar',
            'monitor',
            'docente',
            'outubro',
            'napoles',
            'corujao',
            'abacaxi',
            'ossario',
            'sulista',
            'cunhado',
            'clerigo',
            'lampada',
            'abelhao',
            'nigeria',
            'gatinho',
            'saturno',
            'tesoura',
            'oxigeno',
            'sevilha',
            'oboista',
            'atacama',
            'sumario',
            'nairobi',
            'zebrado',
            'almocar',
            'igrejas',
            'navioes',
            'baleias',
            'canetas',
            'hamster',
            'lagarto',
            'estante',
            'relogio',
            'alongar',
            'jurista',
            'galaxia']
    elif nivel == '3':
        # Nível difícil
        palavras_1 = [
            "perseverança",  # 12 letras
            "remanescente",  # 12 letras
            "condolências",  # 12 letras
            "prerrogativa",  # 12 letras
            "extrovertido",  # 12 letras
            "complacência",  # 12 letras
            "procrastinar",  # 12 letras
            "discrepância",  # 12 letras
            "determinação",  # 12 letras
            "independente",  # 12 letras
            "consequência",  # 12 letras
            "intermitente",  # 12 letras
            "conveniência",  # 12 letras
            "compartilhar",  # 12 letras
            "benevolência",  # 12 letras
            "contingência",  # 12 letras
            "eclesiástico",  # 12 letras
            "transgressão",  # 12 letras
            "consideração",  # 12 letras
            "felicitações",  # 12 letras
            "concomitante",  # 12 letras
            "convergência",  # 12 letras
            "conhecimento",  # 12 letras
            "cordialidade",  # 12 letras
            "cumplicidade",  # 12 letras
            "convencional",  # 12 letras
            "subsistência",  # 12 letras
            "proselitismo",  # 12 letras
            "disseminação",  # 12 letras
            "coincidência",  # 12 letras
            "sistematizar",  # 12 letras
            "complexidade",  # 12 letras
            "intolerância",  # 12 letras
            "ininterrupto",  # 12 letras
            "inadimplente",  # 12 letras
            "globalização",  # 12 letras
            "formalização",  # 12 letras
            "objetividade",  # 12 letras
            "cabeleireiro",  # 12 letras
            "meteorologia"]  # 12 letras]
    return palavras_1