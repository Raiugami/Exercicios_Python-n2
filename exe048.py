print("Os numeros impares e multiplos de 3 no intervalo de 1 a 500 são: \n")
soma = 0
for c in range(1, 500+1):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        print(c)
print("\nA soma dos valores equivale a: {} ".format(soma))
