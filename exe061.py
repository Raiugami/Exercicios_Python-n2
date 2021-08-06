pt = int(input("Informe o primeiro termo: "))
raz = int(input("Informe a razão : "))
contador = 0
decimo = pt + (10-1) * raz
while contador < decimo:
    contador = contador + raz
    print('{} '.format(contador), end='-> ')
print('ACABOU')
