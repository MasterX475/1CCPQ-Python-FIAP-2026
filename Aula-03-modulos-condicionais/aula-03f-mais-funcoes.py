def boas_vindas(nome):
    print(f"Olá {nome}, seja bem-vindo!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)


def soma(num1, num2):
    soma = num1 + num2
    return soma

resultado_soma = soma(1,7)
print(resultado_soma)