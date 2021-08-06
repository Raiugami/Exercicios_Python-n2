from math import factorial
numero = int(input("Informe um numero: "))
fatorial = numero
print("Calculando {}! = ".format(numero), end='')
while fatorial > 0:
    print("{}".format(fatorial), end='')
    print('x' if fatorial > 1 else ' = ', end='')
    fatorial -= 1
print("{}".format(factorial(numero)), end='')
