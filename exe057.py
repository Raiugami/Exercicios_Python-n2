sexo = str(input("Informe o seu sexo, [M] ou [F]: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados invalidos. Informe o seu sexo, [M] ou [F]: ")).strip().upper()
print("O seu sexo é {}".format(sexo))
