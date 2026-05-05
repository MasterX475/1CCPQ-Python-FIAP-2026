texto = "Fiap Paulista"

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])

tamanho = len(texto)
print(tamanho)

for i in range(tamanho):
    print(f"texto[{i}] = {texto[i]}")

for c in texto:
    print(c)