preco = float(input("Informe o preço do produto: "))
met = int(input('''Escolha a opção de pagamento :

[1] A vista dinheiro/cheque 
[2] À vista no cartão
[3] 2x no cartão
[4] 3x no cartão 

Qual opção ?  '''))

if met == 1:
    print("O valor é R$ {:.2f}".format(preco - (preco * 0.10)))
elif met == 2:
    print("O valor é R$ {:.2f}".format(preco - (preco * 0.05)))
elif met == 3:
    print("O valor total é R$ {:.2f}, sendo duas parcelas de R$ {:.2f}".format(preco, preco / 2))
elif met == 4:
    parcela = int(input("Quantas parcelas? "))
    print("O valor total é R$ {:.2f}, sendo {} parcelas de R$ {:.2f}".format(preco + (preco * 0.20),parcela, (preco + (preco * 0.20)) / parcela))


