import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


# Inicializa uma lista para armazenar as cartas (deck)
carta_std = {
        "nome": "",
        "codigo": "",
        "raridade": "?",  # Valor padrão
        "tipo": "?",            # Valor padrão
        "foil": 'false',
        "preco min": 0.0,  # Valor padrão
        "preco med": 0.0,  # Valor padrão
        "preco max": 0.0,  # Valor padrão
    }

#Função responsável pela modificações no arquivo json do deck selecionado
def gerenciador_deck(nome_deck):
    while True:
        print ("\nEscolha uma opção:")
        print ("(1) - Criar novo deck")
        print ("(2) - Gerenciar cartas do deck existente")
        print ("(3) - Excluir deck existente")
        print ("(4) - Sair do gerenciador de decks")
        
        opcao = input("Digite o número da opção desejada: ")
        
        #Caso selecione criiar novo deck
        if opcao == "1":
            criar_deck(input("Digite o nome do deck que deseja criar: "))
        #Caso selecione modificar deck existente
        elif opcao == "2":
            print ("\nEscolha uma opção:")
            print ("(1) - Adicionar carta ao deck")
            print ("(2) - Excluir carta do deck")
            print ("(3) - Sair do gerenciador de cartas")
            
            opc = input("Digite o número da opção desejada: ")
            
            while True:
                #Caso escolha adicionar novo item dentro do arquivo
                if opc == "1":
                    adicionar_carta()
                #Caso escolha excluir um item de dentro do arquivo
                elif opc == "2":
                    nome = input("Digite o nome da carta: ")
                    codigo = input("Digite o código da carta: ")
                    foil = input("O item é foil? (True/False): ").strip().lower() == 'true'
                    deletar_carta(nome, codigo, foil, nome_deck)
                #Caso escolha sair do gerenciador de itens do arquivo
                elif opc == "3":
                    break
                #Caso escolha opção inexistente
                else:
                    print("Opção inválida. Digite novamente.")
        #Caso escolha excluir o arquivo JSON do respectivo deck
        elif opcao == "3":
            deletar_deck()
            
        #Caso escolha sair do gerenciador de arquivos
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Digite novamente.")
            
def deletar_carta(nome, codigo, foil, nome_deck):
    with open (nome_deck, "r") as f:
        deck = json.load(f)
        for carta in deck:
            if carta["nome"] == nome and carta["codigo"] == codigo and carta["foil"] == foil:
                deck.remove(carta)
        


def criar_deck(nome_deck):
    if not os.path.exists(nome_deck+".json"):
        with open(nome_deck+".json", "w") as deck_file:
            deck_file.write(json.dumps(carta_std,indent=8))
            print("Deck criado com sucesso!")
            #deck = json.load(deck_file)
    else:
        print("\nDeck existente!")
    
def adicionar_carta():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar carta a novo deck")
        print("2 - Adicionar carta a deck existente")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            nome_deck = input ("\nDigite o nome do novo deck: ")
            criar_deck(nome_deck)
            break
            
        elif opcao == '2':
            nome_deck = input ("\nDigite o nome do novo deck: ")
            #alterar_deck(nome_deck)
            break
        
        else:
            print("Opção inválida. Digite novamente.")
                        
    # Cria um dicionário representando a carta
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
    deck.append(carta)  # Adiciona o dicionário à lista
    json_object = json.dumps(deck, indent=8)


    with open("sample.json", "w") as deck1:
        deck1.write(json_object)
        print("\nCarta adicionada com sucesso!")

def ver_cartas():
    if not deck:
        print("\nNenhuma carta cadastrada.")
    else:
        print("\nCartas cadastradas:")
        for carta in deck:
            print(carta)

def buscar_info_carta(nome_carta):
    driver = webdriver.Chrome ()
    driver.get("https://www.ligapokemon.com.br/?view=home")

    try:
        # Localiza o campo de busca pelo ID
        campo_busca = driver.find_element(By.ID, "mainsearch")
        
        # Digite o nome da carta que você deseja buscar
        nome_da_carta = carta["nome"] +"(" + carta["codigo"] + ")" # Substitua pelo nome da carta que você quer buscar
        campo_busca.send_keys(nome_da_carta)
        
            # Aguarda um momento para garantir que a página carregou
        time.sleep(2)  # Ajuste o tempo conforme necessário

        # Localiza o botão e clica nele
        botao_fechar_campanha = driver.find_element(By.ID, "campanha-del-1")
        botao_fechar_campanha.click()
        
        # Aguarda um momento para garantir que a ação foi concluída
        time.sleep(1)  # Ajuste o tempo conforme necessário
        
        # Localiza o botão de busca e clica nele
        botao_busca = driver.find_element(By.CLASS_NAME, "blue-magnify-container")
        botao_busca.click()
        
        # Aguarda o carregamento da página de resultados (ajuste o tempo se necessário)
        time.sleep(3)

        # Identifica o preço da carta com base na condição de foil
        # Localiza os elementos que contêm informações sobre a raridade
        elementos = driver.find_elements(By.CSS_SELECTOR, ".container-price-mkp-item .container-extras")

        for elemento in elementos:
            # Verifica se o texto contém "Foil" ou "Normal"
            if "Foil" in elemento.text:
                if carta["foil"]:
                    # Captura o preço se for foil
                    preco_elemento = elemento.find_element(By.XPATH, "..//div[contains(@class, 'price-mkp')]//div[@class='min']//div[@class='price']")
                    carta["preco min"] = float(preco_elemento.text.replace("R$", "").replace(",", ".").strip())
                    preco_elemento = elemento.find_element(By.XPATH, "..//div[contains(@class, 'price-mkp')]//div[@class='medium']//div[@class='price']")
                    carta["preco med"] = float(preco_elemento.text.replace("R$", "").replace(",", ".").strip())
                    preco_elemento = elemento.find_element(By.XPATH, "..//div[contains(@class, 'price-mkp')]//div[@class='max']//div[@class='price']")
                    carta["preco max"] = float(preco_elemento.text.replace("R$", "").replace(",", ".").strip())
                    print(f"A carta é: Foil, Preço mínimo: R$ {carta['preco min']:.2f}")
                    print(f"A carta é: Foil, Preço médio: R$ {carta['preco med']:.2f}")
                    print(f"A carta é: Foil, Preço máximo: R$ {carta['preco max']:.2f}")
                    
            elif "Normal" in elemento.text:
                if not carta["foil"]:
                    # Captura o preço se for normal
                    preco_elemento = elemento.find_element(By.XPATH, "..//div[contains(@class, 'price-mkp')]//div[@class='min']//div[@class='price']")
                    carta["preco min"] = float(preco_elemento.text.replace("R$", "").replace(",", ".").strip())
                    preco_elemento = elemento.find_element(By.XPATH, "..//div[contains(@class, 'price-mkp')]//div[@class='medium']//div[@class='price']")
                    carta["preco med"] = float(preco_elemento.text.replace("R$", "").replace(",", ".").strip())
                    preco_elemento = elemento.find_element(By.XPATH, "..//div[contains(@class, 'price-mkp')]//div[@class='max']//div[@class='price']")
                    carta["preco max"] = float(preco_elemento.text.replace("R$", "").replace(",", ".").strip())
                    print(f"A carta é: Normal, Preço mínimo: R$ {carta['preco min']:.2f}")
                    print(f"A carta é: Normal, Preço médio: R$ {carta['preco med']:.2f}")
                    print(f"A carta é: Normal, Preço máximo: R$ {carta['preco max']:.2f}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")    

    # Fecha o driver
    driver.quit()   

    try:
        # Localiza o campo de busca pelo ID
        campo_busca = driver.find_element(By.ID, "mainsearch")
        
        # Digite o nome da carta que você deseja buscar
        nome_da_carta = "Terapagos EX (128/142)"  # Substitua pelo nome da carta que você quer buscar
        campo_busca.send_keys(nome_da_carta)
        
            # Aguarda um momento para garantir que a página carregou
        time.sleep(2)  # Ajuste o tempo conforme necessário

        # Localiza o botão e clica nele
        botao_fechar_campanha = driver.find_element(By.ID, "campanha-del-1")
        botao_fechar_campanha.click()
        
        # Aguarda um momento para garantir que a ação foi concluída
        time.sleep(1)  # Ajuste o tempo conforme necessário
        
        # Localiza o botão de busca e clica nele
        botao_busca = driver.find_element(By.CLASS_NAME, "blue-magnify-container")
        botao_busca.click()
        
        # Aguarda o carregamento da página de resultados (ajuste o tempo se necessário)
        time.sleep(3)

        # Aqui você pode adicionar código para processar os resultados da busca, se necessário

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Fecha o driver
    try:
        # Localiza o elemento <a> dentro do <span> com id "details-screen-rarity"
        rarity = driver.find_element(By.XPATH, "//span[@id='details-screen-rarity']/a")
        
        # Acessa o texto do elemento
        print(f"O texto encontrado é: {rarity.text}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
    driver.quit()

    for carta in deck:
        if carta["nome"].lower() == nome_carta.lower():
            print(f"\nPreço da carta '{nome_carta}': R$ {carta['preco']:.2f}")
            return
    print("\nCarta não encontrada.")

def buscar_preco_deck():
    print("\nPara buscar o preço de um deck, por favor, forneça os nomes das cartas, separados por vírgula:")
    nomes_cartas = input().split(',')
    total_preco = 0
    for nome in nomes_cartas:
        nome = nome.strip()
        for carta in deck:
            if carta["nome"].lower() == nome.lower():
                total_preco += carta["preco"]
                break
        else:
            print(f"Carta '{nome}' não encontrada.")
    print(f"\nPreço total do deck: R$ {total_preco:.2f}")

# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Editar decks")
    print("2. Ver cartas")
    print("3. Buscar informações da carta")
    print("4. Buscar preço de deck")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        adicionar_carta()
    elif opcao == '2':
        ver_cartas()
    elif opcao == '3':
        nome_carta = input("Digite o nome da carta que deseja buscar: ")
        buscar_info_carta(carta['nome' == nome_carta] for carta in deck)
    elif opcao == '4':
        buscar_preco_deck()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

'''json_object = json.dumps(dictionary, indent=6)


with open("sample.json", "w") as outfile:
    outfile.write(json_object)'''