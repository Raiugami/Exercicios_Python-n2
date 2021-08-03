soma = 0
for c in range(1, 6+1):
    numero = int(input("Informe o {}º numero: ".format(c)))
    if numero % 2 == 0:
        soma = soma + numero
print("A soma dos valores pares informados é igual a: {} ".format(soma))
1