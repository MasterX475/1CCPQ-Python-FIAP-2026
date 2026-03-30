idade = int(input("Qual a sua idade? "))

if idade < 0:
    print("Coloque algo válido!")
elif idade < 16:
    print("Não pode votar")
elif idade < 18:
    print("Voto opcional")
elif idade < 60:
    print("Voto obrigatório")
elif idade < 120:
    print("Voto opcional")
else:
    print("Coloque algo válido")