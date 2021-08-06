cont = n = 0
while True:
    n = int(input("Informe um numero: "))
    if n < 0:
        break
    print("="*20)
    while cont < 10:
        cont = cont + 1
        print(f"{n} x {cont} = {n*cont}")
    print("="*20)
    cont = 0
print("FIM")
