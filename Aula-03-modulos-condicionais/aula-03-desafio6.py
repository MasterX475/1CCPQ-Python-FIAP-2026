num1 = float(input("Mê de o primeiro número: "))
num2 = float(input("Mê de o segundo número: "))
operacao = input("Escolha a operação desejada (+, -, *, /): ")

def operar():
    if operacao == "+":
        resultado = num1 + num2
        return resultado
    elif operacao == "-":
        resultado = num1 - num2
        return resultado
    elif operacao == "*":
        resultado = num1 * num2
        return resultado
    elif operacao == "/":
        resultado = num1 / num2
        return resultado
    else:
        return "Error"

print(operar())