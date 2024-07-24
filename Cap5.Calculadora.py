def multiplicar():
    nr1 = float(input("Digite o primeiro número: "))
    nr2 = float(input("Digite o segundo número: "))
    return nr1 * nr2

def dividir():
    nr1 = float(input("Digite o primeiro número: "))
    nr2 = float(input("Digite o segundo número: "))
    return nr1/nr2

def subtrair():
    nr1 = float(input("Digite o primeiro número: "))
    nr2 = float(input("Digite o segundo número: "))
    return nr1 - nr2

def soma():
    nr1 = float(input("Digite o primeiro número: "))
    nr2 = float(input("Digite o segundo número: "))
    return nr1 + nr2

conta = input("1. Somar \n2. Subtrair \n3. Dividir \n4. Multiplicar\n")
if conta == "1":
    print(soma())
elif conta == "2":
    print(subtrair())
elif conta== "3":
    print(dividir())
elif conta == "4":
    print(multiplicar())
else:
    print("Inválido")