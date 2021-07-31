n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2) / 2

if media < 5.0:
    print("Média {:.2f} = Reprovado".format(media))
elif media >= 5.0 and media <= 6.9:
    print("Média {:.2f} = Recuperação".format(media))
elif media > 6.9:
    print("Média {:.2f} = Aprovado".format(media))
