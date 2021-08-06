cont = 1
totalg = 0
maismil = 0
prodbar = ''
barato = 0

while True:
    prod = str(input(f"Informe o nome do {cont}º produto: ")).strip().capitalize()
    preco = float(input(f"Informe o preço do {cont}º produto: R$"))

    if cont == 1 or preco < barato:
        barato = preco
        prodbar = prod

    totalg += preco

    if preco > 1000:
        maismil = maismil + 1

    escolha = str(input(" Deseja continuar? [S/N] ")).upper().strip()
    if escolha == 'N':
        break

    cont = cont + 1

print('='*25)
print(f" O preço total é R${totalg:.2f}")
print(f"A quantidade de produtos que custam mais de R$1000 é: {maismil}")
print(f" O produto mais barato é {prodbar} que custa {barato:.2f}")
print('='*25)
