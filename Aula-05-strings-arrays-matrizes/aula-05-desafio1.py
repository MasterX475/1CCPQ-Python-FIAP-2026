import random

qnt_numeros = int(input("Quantos números quer gerar? "))

numeros = []

for i in range(qnt_numeros):
    numeros.append(random.randint(0, 9))

print(numeros)