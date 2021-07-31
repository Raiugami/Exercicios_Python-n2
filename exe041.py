anonasc = int(input("Informe o ano de nascimento: "))
idade = 2021 - anonasc
if idade <= 9:
    print("Atleta Mirim!")
elif idade <= 14:
    print("Atleta Infantil!")
elif idade <= 19:
    print("Atleta Junior!")
elif idade <= 25:
    print("Atleta Senior!")
else:
    print("Atleta Master!")
