import os
import json

dicionario_animais = {}
if os.path.exists("animais.json"):
    with open("animais.json", "r") as arquivo:
        dicionario_animais = json.load(arquivo)


def criar_arquivo():
    try:
        if os.path.exists("animais.json"):
            print("\nArquivo 'animais.json' já existe!")
            return
        else:                
            with open("animais.json", "w") as arquivo:
                json.dump(dicionario_animais, arquivo, indent=4)
            print("\nArquivo 'animais.json' criado com sucesso!")
    except Exception as e:
        print(f"\nErro ao criar o arquivo: {e}")
def ler_arquivo():
    try:
        with open("animais.json", "r") as arquivo:
            conteudo = json.load(arquivo)
            for animal, idade in conteudo.items():
                print(f"Animal: {animal}, Idade: {idade}")
    except Exception as e:
        print(f"\nErro ao ler o arquivo: {e}")
        
def adicionar_animal():
    nome_animal = input("Digite o nome do animal: ")
    idade_animal = int(input("Digiite a idade do Bichano: "))
    dicionario_animais[nome_animal] = idade_animal
    with open("animais.json", "w") as arquivo:
        json.dump(dicionario_animais, arquivo, indent=4)
    
    
opcao = ""
while opcao != "0":
    print("\n======= MENU DO ARQUIVO JSON=======")
    print("1. Criar arquivo inicial")
    print("2. Ler conteúdo do arquivo")
    print("3. Adicionar animal ao final")
    print("0. Sair do programa")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        criar_arquivo()
    elif opcao == "2":
        ler_arquivo()
    elif opcao == "3":
        adicionar_animal()
    elif opcao == "0":
        print("\nSaindo do sistema...")
    else:
        print("\nOpção Inválida - Escolha um número do menu.")


