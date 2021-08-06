quant = n = cont = 0

while True:
    n = int(input("Informe um numero [999 = parar]:  "))
    if n == 999:
        break
    cont = cont + 1
    quant = quant + n
print(f"A soma dos {cont} valores é {quant}")

