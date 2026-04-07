num1 = int(input("Mê de um número: "))
num2 = int(input("Mê de outro número: "))

if num1 > num2:
    dividendo = num1
    divisor = num2
else:
    dividendo = num2
    divisor = num1

if (dividendo % divisor) == 0:
    print("Os números são múltiplos")
else:
    print("Os números não são múltiplos")