hmaior = 0
mmenor = 0
media = 0
somaida = 0

for c in range(1, 5):
    print(" ======== {} PESSOA ========".format(c))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().strip()
    somaida += idade
    if idade > hmaior and sexo == 'M':
        hmaior = idade
    if idade < 20 and sexo == "F":
        mmenor += 1

media = somaida / 4

print("A media de idade é igual a {}".format(float(media)))
print("O homem mais velho tem {} anos".format(hmaior))
print("O total de mulher com menos de 20 anos é igual a {}".format(mmenor))
