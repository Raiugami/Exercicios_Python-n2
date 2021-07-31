numero = int(input("Informe um numero: "))
escolha = int(input(''' Qual conversão voce deseja?

[1] Binário
[2] Octal 
[3] Hexadecimal 

informe : '''))

if escolha == 1:
    conversao = format(numero, "b")
    print("O numero {} convertido para binario é: {}".format(numero, conversao))

elif escolha == 2:
    conversao = format(numero, "o")
    print("O numero {} convertido para octal é: {}".format(numero, conversao))


elif escolha == 3:
    conversao = format(numero, "x")
    print("O numero {} convertido para hexadecimal é: {}".format(numero, conversao))

