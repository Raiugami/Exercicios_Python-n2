valor = float(input("Informe o valor da casa: "))
salario = float(input("Informe o seu salario: "))
parcela = int(input("Informe em quantos anos deseja pagar: "))

valormensal = valor / (parcela * 12)
print("O valor da parcela é de: R$ {:.2f}".format(valormensal))

if valormensal > salario * 0.30:
    print("A mensalidade é mais que 30% do seu salario. Empréstimo negado!")
else:
    print("Emprestimo liberado! :D ")
