# lista_frutas = ["Banana", "Maça", "Melancia"]
#
# print(lista_frutas[0])
# print(lista_frutas[1])
# print(lista_frutas[2])
#
# lista_frutas.append("Laranja")
# print(lista_frutas)
# print()
#
# for i in range(len(lista_frutas)):
#     print(lista_frutas[i])
#
# print()
#
# for i in lista_frutas:
#     print(i)
#


nomes = ["Ana", "Maria", "Enzo", "Leo"]

for i in range(len(nomes)):
    for j in range(i + 1, len(nomes)):
        if (i != j): print(f"{nomes[i]} - {nomes[j]}")