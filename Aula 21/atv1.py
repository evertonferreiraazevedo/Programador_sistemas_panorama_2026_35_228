def contar_vogais(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        vogais = "aeiouAEIOU"
        contador = 0
        for letra in conteudo:
            if letra in vogais:
                contador += 1  
        print(f"O arquivo '{nome_arquivo}' contem {contador} vogais.") 
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' nao foi encontrado.")

def exibir_menu():
    while True:
        print("====== MENU PRINCIPAL ======")
        print("1 - Contar vogais de um arquivo")
        print("2 - Sair do programa")
        print("============================")
        
        opcao = input("Escolha uma opcao (1 ou 2): ")
        
        if opcao == "1":
            arquivo_usuario = input("Digite o nome do arquivo txt: ")
            contar_vogais(arquivo_usuario)
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida!")

exibir_menu()
