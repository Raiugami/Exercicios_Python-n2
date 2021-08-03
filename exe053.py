frase = str(input("Informe uma frase: ")).strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += (junto[letra])

print(junto, inverso)
if inverso == junto:
    print("temos um palíndromo!")
else:
    print("Não temos um palindromo!")
