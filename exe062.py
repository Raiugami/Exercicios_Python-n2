pt = int(input("Informe o primeiro termo: "))
raz = int(input("Informe a razão : "))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='-> ')
        termo += raz
        cont += 1
    print('Pausa')
    mais = int(input("mais quantos deseja mostrar? "))
print("Progressão finalizada. O total de termos é igual á {}".format(total))
