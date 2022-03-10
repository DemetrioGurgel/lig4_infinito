from jogo import *

def modos():
    '''Seleção do modo de jogo'''
    global modo
    while True:
        modo = input("SELECIONE O MODO QUE DESEJA JOGAR (1=TRADICIONAL / 2=INFINITO): ")
        if modo == "1" or modo == "2":
            break
        else:
            print(colored("PARA SELECIONAR O MODO, INSIRA APENAS O NÚMERO 1 OU 2", "red"))

def main_tradicional():
    """Laço do modo tradicional"""
    global ganhou
    jogo = ini_matriz(tamanho)
    turno = inicia_turno()

    while not ganhou:
        nome = ""
        if turno == JOG1:
            nome = colored(nome1, "yellow")
        else:
            nome = colored(nome2, "red")
        mostra_matriz(jogo)
        print(colored('Quem vai jogar agora é o jogador {}!'.format(nome), "green"))
        print('Escolha em qual coluna você quer jogar (escolha de 1 a ', tamanho[1], '): ')
        escolha = input()
        while True:
            if jogada_formato_valido(escolha) == True:
                break
            else:
                print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                escolha = input()
        escolha = int(escolha)

        while escolha < 1 or escolha > tamanho[1]:
            print(colored("Número inválido.", "red"))
            print("Escolha em qual coluna você quer jogar (escolha de 1 a ", tamanho[1], "): ")
            escolha = input()
            while True:
                if jogada_formato_valido(escolha) == True:
                    break
                else:
                    print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                    escolha = input()
            escolha = int(escolha)


        if turno == JOG1:
            jogo = jogada(jogo, escolha - 1, circulo_y)
        else:
            jogo = jogada(jogo, escolha - 1, circulo_r)

        ganhou = verificar_tradicional(jogo)
        turno = troca_turno(turno)

    def ganhador():
        """define ganhador do modo tradicional"""
        ganhador = ""
        if ganhou == circulo_y:
            ganhador = colored(nome1, "yellow")
        if ganhou == circulo_r:
            ganhador = colored(nome2, "red")
        print('O jogador {} venceu!'.format(ganhador))

    mostra_matriz(jogo)
    print()
    ganhador()
    return 0


def main_infinito():
    """Laço do modo infinito"""
    global jogadas, ganhou, contador1, contador2
    jogo = ini_matriz(tamanho)
    turno = inicia_turno()
    while not ganhou:
        if turno == JOG1:
            nome = colored(nome1, "yellow")
        else:
            nome = colored(nome2, "red")
        mostra_matriz(jogo)
        print(colored('Quem vai jogar agora é o jogador {}!'.format(nome), "green"))
        print('Escolha em qual coluna você quer jogar (escolha de 1 a ', tamanho[1], '): ')
        escolha = input()
        while True:
            if jogada_formato_valido(escolha) == True:
                break
            else:
                print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                escolha = input()

        escolha = int(escolha)
        while escolha < 1 or escolha > tamanho[1]:

            print(colored("Número inválido.", "red"))
            print("Escolha em qual coluna você quer jogar (escolha de 1 a ", tamanho[1], "): ")
            escolha = input()
            while True:
                if jogada_formato_valido(escolha) == True:
                    break
                else:
                    print(colored(f"DIGITE APENAS NUMEROS DE 1 A {tamanho[1]}: ", "red"))
                    escolha = input()
            escolha = int(escolha)
        if turno == JOG1:
            jogo = jogada(jogo, escolha - 1, circulo_y)
        if turno == JOG2:
            jogo = jogada(jogo, escolha - 1, circulo_r)

        if turno == JOG1:
            verificar_infinito_y(jogo, turno)
        else:
            verificar_infinito_red(jogo, turno)

        turno = troca_turno(turno)
        jogadas += 1

        limite = tamanho[0] * tamanho[1]
        if jogadas == limite:
            ganhou = 1

    mostra_matriz(jogo)

    return 0

modos()

global modo
if modo == "1":
    print(colored("### \n"
        "COMO JOGAR: \n"
        "O objetivo do jogo é um dos jogadores fazer uma sequência \n"
        "de 4 peças da mesma cor, essa sequência pode ser formada \n"
        "de forma vertical, horizontal ou diagonal. Ganha o jogador \n"
        "que conseguir realizar o objetivo primeiro. \n"
        "###", "green"))
    main_tradicional()
if modo == "2":
    print(colored("### \n"
        "COMO JOGAR: \n"
        "O objetivo principal do jogo é fazer a maior quantidade \n"
        "de sequências de 4 peças da mesma cor, contudo, cada jogador \n"
        "só poderá fazer apenas uma sequência em cada direção (vertical \n"
        "horizontal e diagonal). Ganha o jogador que ao fim de todos os \n"
        "espaços do tabuleiro, tiver a maior quantidade de pontos \n"
        "###", "green"))
    main_infinito()
