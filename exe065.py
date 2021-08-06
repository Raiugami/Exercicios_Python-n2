cont = media = maior = menor = 0
resp = 'S'
while resp == 'S':
    num = int(input("Informe um numero: "))
    media = media + num
    cont += 1
    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Deseja continuar? [S] ou [N] ")).upper().strip()
media = media / cont
print(f"O maior numero digitado foi {maior}")
print(f"O menor numero digitado foi {menor}")
print(f"A média é igual á: {media}")
