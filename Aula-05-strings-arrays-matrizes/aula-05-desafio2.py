qnt_alunos = int(input("Digite a quantidade de alunos: "))

medias = []
media_sala = 0

for i in range(qnt_alunos):
    nota1 = float(input(f"Digite a primeira nota do {i + 1} aluno: "))
    nota2 = float(input(f"Digite a segunda nota do {i + 1} aluno: "))
    nota3 = float(input(f"Digite a terceira nota do {i + 1} aluno: "))
    nota4 = float(input(f"Digite a quarta nota do {i + 1} aluno: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    medias.append(media)

print(medias)
print()

for i in medias:
    media_sala += i

media_sala = media_sala / qnt_alunos

print(media_sala)
print()

for i in range(len(medias)):
    if medias[i] < media_sala:
        print(f"Aluno {i + 1} Reprovado")
    elif medias[i] >= media_sala:
        print(f"Aluno {i + 1} Aprovado")
