import random
import time
print('-=-' * 20)
numero = int(input("Entre 0 a 5, qual numero você acha que o computador escolheu? "))
print('-=-' * 20)
c = 1
n = random.randrange(0, 6)
while numero != n:
    print("Você errou, o numero escolhido foi {}".format(n))
    numero = int(input("Entre 0 a 5, qual numero você acha que o computador escolheu? "))
    n = random.randrange(0, 6)
    if numero != n:
        c = c + 1
print("processando...")
time.sleep(2)
print("Você acertou! O numero escolhido foi {}".format(n))
print("Você tentou {} vezes até acertar :D".format(c))
