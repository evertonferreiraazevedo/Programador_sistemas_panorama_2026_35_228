import os

def criar_arquivo():
    # Verifica se o arquivo já existe para não apagar o conteúdo anterior
    try:
        if os.path.exists("meu_arquivo.txt"):
            print("\nAviso - O arquivo já existe!")
        else:
            arquivo = open("meu_arquivo.txt", "w", encoding="utf-8")
            arquivo.close()
            print("\nSucesso - Arquivo criado com o conteúdo inicial!")
    except Exception as e:
        print(f"\nErro ao criar o arquivo: {e}")

def ler_arquivo():
    try:
        arquivo = open("meu_arquivo.txt", "r", encoding="utf-8")
        conteudo = arquivo.read()
        print(conteudo)
        arquivo.close()
    except Exception as e:
        print(f"\nErro ao ler o arquivo: {e}")
        
def adicionar_animal():
    animal = input("\nDigite o nome de um animal para adicionar: ")
    try:
        arquivo = open("meu_arquivo.txt", "a", encoding="utf-8")
        arquivo.write(animal + "\n")
    except Exception as e:
        print(f"\nErro ao adicionar animal: {e}")
        return
    print(f"[Sucesso] '{animal}' foi adicionado ao arquivo!")
    
opcao = ""
while opcao != "0":
    print("\n======= MENU DO ARQUIVO =======")
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


