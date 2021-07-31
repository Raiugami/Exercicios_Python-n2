import time
import random

while True:

    jogador = int(input(''' -=- -=- -=- -=- JOKENPÔ -=- -=- -=- -=-
        
        Escolha um dos comandos abaixo :D
        
        [1] Pedra
        [2] Papel
        [3] Tesoura
        
        
        Comando:  '''))

    computador = random.randint(1, 3)
    print("JÒÒÒÒOOH...")
    time.sleep(1)
    print("KEEEEEEN...")
    time.sleep(1)
    print("pÔÔOO!!!\n\n")
    time.sleep(1)

    if jogador == computador:
        print("EMPATE")
    elif jogador == 2 and computador == 1:
        print("VOCÊ GANHOU!")
        print("\nVocê escolheu PAPEL e o computador escolheu PEDRA.")
    elif jogador == 1 and computador == 3:
        print("VOCÊ GANHOU!")
        print("\nVocê escolheu PEDRA e o computador escolheu TESOURA.")
    elif jogador == 3 and computador == 2:
        print("VOCÊ GANHOU!")
        print("\nVocê escolheu TESOURA e o computador escolheu PAPEL.")
    elif jogador == 1 and computador == 2:
        print("VOCÊ PERDEU!")
        print("\nVocê escolheu PEDRA e o computador escolheu PAPEL.")
    elif jogador == 3 and computador == 1:
        print("VOCÊ PERDEU!")
        print("\nVocê escolheu TESOURA e o computador escolheu PEDRA.")
    elif jogador == 2 and computador == 3:
        print("VOCÊ PERDEU!")
        print("\nVocê escolheu PAPEL e o computador escolheu TESOURA.")
    print("iniciando nova partida...\n\n")
    time.sleep(2)
