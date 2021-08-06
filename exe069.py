cont = 1
maior18 = 0
homens = 0
mulheres = 0

while True:
    idade = int(input(f"Informe a idade da {cont}º pessoa: "))
    if idade > 18:
        maior18 = maior18 + 1
    sexo = str(input("informe o sexo da pessoa: [M/F] ")).upper().strip()
    if sexo == 'M':
        homens = homens + 1

    if idade <= 20 and sexo == 'F':
        mulheres = mulheres + 1

    escolha = str(input("Deseja continuar ? [S/N] ")).upper().strip()
    if escolha == "N":
        break
    cont = cont + 1

print('='*25)
print(f"A quantidade de pessoas com mais de 18 anos é: {maior18}")
print(f"A quantidade de homens cadastrados é : {homens}")
print(f"A quantidade de mulheres com menos de 20 anos é: {mulheres}")
print('='*25)
