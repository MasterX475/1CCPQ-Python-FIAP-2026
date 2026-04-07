num = int(input("Coloque um número: "))

resto = num%2
if resto == 0:
    print(f"{num} é par")
else:
    print(f"{num} é impar")