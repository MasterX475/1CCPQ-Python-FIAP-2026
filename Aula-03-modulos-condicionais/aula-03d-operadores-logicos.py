verifica_email = False
verifica_senha = True

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Pode entrar!")

if not verifica_login:
    print("Errou...")

logica_ou = False or True or False
print(not logica_ou)

