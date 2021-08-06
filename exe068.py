import random
n = 0
soma = 0
cont = 0
while True:
    lista = random.randrange(0, 10)
    n = int(input("Informe um valor: "))
    escolha = str(input("Par ou Impar? [P/I] ")).strip().upper()
    soma = n + lista
    if soma % 2 == 0:
        cont = +1
        print(f"Você escolhe {n} e o computador escolheu {lista}")
        print(f" a soma entre os valores é {soma} que é um valor par")
    else:
        print(f"Você escolhe {n} e o computador esoclheu {lista}")
        print(f"a soma entre os valores é {soma} que é um valor Impar")
        break

print(f"O numero de vitorias é: {cont}")
