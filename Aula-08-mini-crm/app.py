from model import model_lead
import control

def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    stage = input("Etapa no funil: ")

    #Valida os dados
    #Depois é necessário modelar o lead com um dict
    #Usaremos o model

    print(model_lead(name,email,stage))

    #Com os dados modelados em dict
    #Agora é necessário enviar para o leads.json
    #Usaremos o control

    control.create_lead(model_lead(name,email,stage))

    # Desafio - Não recriar o json toda hora, apenas adicionar

    print("Lead adiconado")

def list_leads():
    leads = control.read_leads()
    for i, lead in enumerate(leads):
        print(f"{i} | {lead["name"]:<12} | {lead["email"]}")

    # Desafio - Formatar como tabela

def search_leads():
    query = input("Buscar por: ").strip().lower()
    search_results = control.read_leads_search(query)

    print(f"## | {"Nome":<12} | E-mail")
    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<12} | {lead["email"]}")

def export_leads():
    path_csv = control.export_csv()
    if path_csv == None:
        print("Não foi possível exportar para CSV")
    else:
        print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar lead")
        print("[2] Listar lead")
        print("[3] Buscar (nome/email)")
        print("[4] Exportar para CSV")
        print("[0] Sair")

        opt = input("Escolha uma opção: ")
        print("")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "3":
            search_leads()
        elif opt == "4":
            export_leads()

        elif opt == "0":
            print("Programa encerrado")
            break
        else:
            print("Opçao invalida")

if __name__ == "__main__":
    main()