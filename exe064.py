num = int(input("Informe um numero: "))
cont = 1
total = num
while num < 999:
    num = int(input("Informe um numero: "))
    if num != 999:
        cont = cont + 1
    if num != 999:
        total = total + num

print("O total de numeros digitados é: {}".format(cont))
print("A soma de todos os numero é igual a {}".format(total))

