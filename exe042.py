a = float(input("informe o lado A do triangulo: "))
b = float(input("informe o lado B do triangulo: "))
c = float(input("informe o lado C do triangulo: "))

if b-c < a < b + c and a-c < b < a+c and a-b < c < a+b:
    print("Pode formar um triangulo!")
    if a == b and a == c:
        print("Equilátero")
    elif a == b or b == c or c == a:
        print("Isósceles")
    else:
        print("Escaleno")
else:
    print("Não pode formar um triangulo!")
