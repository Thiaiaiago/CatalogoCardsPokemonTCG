import json
filename = "./data/decks.json"

def escolhas():
    print ("M O D I F I C A D O R    D E     D E C K S")
    print ("Sistema de Gerenciamento de Cartas e Decks")
    print ("(1) Ver Cartas")
    print ("(2) Editar Decks")
    print ("(3) Sair")
    
def ver_decks():
    with open(filename, "r") as f:
        temp = json.load(f)
        for entry in temp:
            nome = entry["nome"]
            inicio = entry["inicio"]
            fim = entry["fim"]
            print(f"Nome: {nome}")
            print(f"Inicício: {inicio}")
            print(f"Fim: {fim}")
            print("\n\n")

def adicionar_cartas():
    item_data = {}
    with open(filename, "r") as f:
        temp = json.load(f)
    item_data["nome"] = input("Nome: ")
    item_data["inicio"] = input("Início: ")
    item_data["fim"] = input("Fim: ")
    temp.append(item_data)
    with open(filename, "w") as f:
        json.dump(temp, f, indent=4)
        
def gerenciar_decks():
    escolha = input("Digite 1 para modificar decks, 2 para criar, 3 para excluir um deck pu 4 para sair! ")
    while True:
        if escolha == "1":
            modificar_decks()
        elif escolha == "2":
            criar_decks()
            break
        elif escolha == "3":
            excluir_decks()
        elif escolha == "4":
            break
        else:
            print("Escolha um dos números especificados acima, por favor!")
        
#def modificar_decks():
    
def criar_decks():
    nome_deck = input("Digite o nome do deck que deseja criar: ")
    carta = {
        "nome": input("Digite o nome da carta: "),
        "codigo": input("Digite o código: "),
        "raridade": "?",  # Valor padrão
        "tipo": "?",            # Valor padrão
        "foil": input("O item é foil? (True/False): ").strip().lower() == 'true',
        "preco min": 0.0,  # Valor padrão
        "preco med": 0.0,  # Valor padrão
        "preco max": 0.0,  # Valor padrão
    }
    
    json_data = json.dumps(carta, indent=8)

    with open(nome_deck+".json", "w") as arquivo:
        arquivo.write(json_data)

    
#def excluir_decks():
    
    
while True:
    escolhas()
    escolha = input("\nEscolha um número: ")
    if escolha == "1":
        ver_decks()
    elif escolha == "2":
        gerenciar_decks()
        break
    elif escolha == "3":
        break
    else: 
        print("Escolha um dos números especificados acima, por favor!")
        