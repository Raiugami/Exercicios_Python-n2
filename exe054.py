maior = 0
menor = 0
for c in range(1, 6):
    pessoa = int(input("informe a idade da {}º pessoa: ".format(c)))
    if pessoa >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print("A quantidade de pessoas maiores de idade é: {}".format(maior))
print("A quantidade de pessoas menores de idade é: {}".format(menor))
