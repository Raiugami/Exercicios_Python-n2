print('=========== TABUADA ==========')

numero = int(input("digite um numero: "))

for c in range(1, 10+1):
    print("{} x {} = {}".format(numero, c, numero*c))
