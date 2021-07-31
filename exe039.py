import datetime
anonasc = int(input("Informe o seu ano de nascimento: "))
idade = datetime.date.today().year - anonasc

if idade == 17:
    print("É hora de se alistar ao serviço militar.")
elif idade < 17:
    print("Ainda não é hora de se alistar. Resta {} anos para você se alistar.".format(17-idade))
elif idade > 17:
    print("Você já deveria ter se alistado ao serviço militar! Esta {} anos atrasado".format((idade-17)))
