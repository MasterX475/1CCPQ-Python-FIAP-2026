tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla)
print(tupla[5])

print(type(tupla))

tupla2 = tuple("Robson")
print(tupla2)
print(tupla2[3:6])

t = "r",
print(t + tupla2[1:6])

# atribuição com tuplas
a = 5
b = 10
print(f"a: {a}, b: {b}")

temp = a
a = b
b = temp
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

email = "1234emailreal@gmail.com"
usuario, dominio = email.split("@")
print(usuario)
print(dominio)