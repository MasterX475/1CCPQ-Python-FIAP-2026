def VerificarNota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota


nota1 = float(input("Digite a primeira nota: "))
nota1 = VerificarNota(nota1)

nota2 = float(input("Digite a segunda nota: "))
nota2 = VerificarNota(nota2)

media = (nota1 + nota2) / 2
print(media)

