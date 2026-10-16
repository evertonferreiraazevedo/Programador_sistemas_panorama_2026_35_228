import os

dicionario_animais = {}

def criar_arquivo():
    # Verifica se o arquivo já existe para não apagar o conteúdo anterior
    try:
        if os.path.exists("animais.txt"):
            print("\nAviso - O arquivo já existe!")
        else:
            arquivo = open("animais.txt", "w", encoding="utf-8")
            arquivo.close()
            print("\nSucesso - Arquivo criado com o conteúdo inicial!")
    except Exception as e:
        print(f"\nErro ao criar o arquivo: {e}")

def ler_arquivo():
    try:
        arquivo = open("animais.txt", "r", encoding="utf-8")
        conteudo = arquivo.read()
        print(type(conteudo))
        arquivo.close()
    except Exception as e:
        print(f"\nErro ao ler o arquivo: {e}")
        
def adicionar_animais():
    animais = input("\nDigite o nome de um animais para adicionar: ")
    idade = input("Digite a idade do animais: ")
    dicionario_animais[animais] = idade
    try:
        arquivo = open("animais.txt", "w", encoding="utf-8")
        arquivo.write(str(dicionario_animais) + "\n")
    except Exception as e:
        print(f"\nErro ao adicionar animais: {e}")
        return
    print(f"[Sucesso] '{animais}' foi adicionado ao arquivo!")
    
opcao = ""
while opcao != "0":
    print("\n======= MENU DO ARQUIVO TXT=======")
    print("1. Criar arquivo inicial")
    print("2. Ler conteúdo do arquivo")
    print("3. Adicionar animais ao final")
    print("0. Sair do programa")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        criar_arquivo()
    elif opcao == "2":
        ler_arquivo()
    elif opcao == "3":
        adicionar_animais()
    elif opcao == "0":
        print("\nSaindo do sistema...")
    else:
        print("\nOpção Inválida - Escolha um número do menu.")


