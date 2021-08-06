while True:
    numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'quartorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    num = int(input("Informe um numero de 0 a 20: "))
    while num < 0 or num > 20:
        num = int(input("Numero invalido. Informe um numero de 0 a 20: "))

    print(f'O numero informado é: {numeros[num]}')
    break
