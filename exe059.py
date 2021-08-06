op = 0
while op != 5:
    top = 0
    op = int(input('''Escolha a opção:  
    
    [1] Soma
    [2] Subtração
    [3] Multiplicação
    [4] Divisão
    [5] Sair do Programa 
    
    Informe aqui: '''))

    if op == 1:
         n1 = int(input("Informe o primeiro numero:"))
         n2 = int(input("Informe o segundo numero: "))
         tot = n1 + n2
         print(tot)
    elif op == 2:
         n1 = int(input("Informe o primeiro numero:"))
         n2 = int(input("Informe o segundo numero: "))
         tot = n1 - n2
         print(tot)
    elif op == 3:
         n1 = int(input("Informe o primeiro numero:"))
         n2 = int(input("Informe o segundo numero: "))
         tot = n1 * n2
         print(tot)
    elif op == 4:
         n1 = int(input("Informe o primeiro numero:"))
         n2 = int(input("Informe o segundo numero: "))
         tot = n1 / n2
         print(tot)

print("Até mais")
