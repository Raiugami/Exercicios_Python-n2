pt = int(input("Informe o primeiro termo: "))
raz = int(input("Informe a razão : "))
decimo = pt + (10-1) * raz
for c in range (pt, decimo+1, raz):
    print('{} '.format(c),end='-> ')
print('ACABOU')
