from termcolor import colored

circulo_y = colored("●", "yellow")
circulo_r = colored("●", "red")
JOG1 = "X"
JOG2 = "0"
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
jogadas = 0
ganhou = 0  # serve pra parar o jogo quando alguem ganhar
print(colored("### BEM VINDO(a) AO LIG4! ###", "yellow"))
vencedor = ""
tamanho = (6, 7)  # serve pra setar o tamanho do jogo infinito
colunas = tamanho[1]
contador1 = 0
contador2 = 0
nome = ""
nome1 = ""
nome2 = ""
jogo = []
ganhador = ""
modo = ""
jogador_atual = 0
turno = ""