menorpeso = 0
maiorpeso = 0

for c in range(1, 6):
    pessoa = int(input("informe o peso da {}º pessoa: ".format(c)))

    if c == 1:
        maiorpeso = pessoa
        menorpeso = pessoa
    else:
        if pessoa > maiorpeso:
            maiorpeso = pessoa
        if pessoa < menorpeso:
            menorpeso = pessoa

print("O maior peso é: {}".format(maiorpeso))
print("O menor peso é: {}".format(menorpeso))

