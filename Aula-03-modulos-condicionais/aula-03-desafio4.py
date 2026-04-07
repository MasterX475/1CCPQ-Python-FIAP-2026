nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media_final = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Media final: {media_final:.2f}")

if media_final >= 7:
    print("Aprovado")
elif media_final >= 5:
    print("Em Recuperação")
else:
    print("Reprovado")