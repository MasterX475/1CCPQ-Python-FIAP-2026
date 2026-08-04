endpoint = ["/criar", "/entrar", "/recarregar"]

status = [[200, 300, 403, 404, 230],
          [305, 207, 503, 298, 231],
          [404, 403, 222, 340, 593]]

endpointErro = [-1,-1]
endpointErroSeguido = []

for i in range(0, len(endpoint)):
    quantidadeSucesso = 0
    quantidadeErro = 0
    erroSeguido = 0
    adicionado = False

    for numStatus in status[i]:

        if numStatus >= 200 and numStatus < 300:
            print("Sucesso")
            quantidadeSucesso += 1
            erroSeguido = 0
        else:
            print("Erro")
            quantidadeErro += 1
            erroSeguido += 1

        if erroSeguido == 2 and not adicionado:
            endpointErroSeguido.append(endpoint[i])
            adicionado = True


    if quantidadeErro > endpointErro[1]:
        endpointErro[0] = i
        endpointErro[1] = quantidadeErro

    porcentagemSucesso = (quantidadeSucesso/len(status[i])) * 100
    print(porcentagemSucesso)

    if (adicionado):
        print("Crítico")
    elif porcentagemSucesso < 80:
        print("Instável")
    else:
        print("Estável")

    print("/////////////////////////////////////////////////////////")

print("\nO mais defeituoso é:")
print(endpoint[endpointErro[0]])

print("\nTeve 2 ou mais erros seguidos em:")
print(endpointErroSeguido)