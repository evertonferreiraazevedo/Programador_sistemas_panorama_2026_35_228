def contar_caractere(nome_arquivo, caractere_procurado):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
        contador = 0
        for caractere in conteudo:
            if caractere == caractere_procurado:
                contador += 1     
        print(f"O caractere '{caractere_procurado}' aparece {contador} vezes no arquivo.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' nao foi encontrado.")
def exibir_menu():
    while True:
        print("====== MENU PRINCIPAL ======")
        print("1 - Contar caractere em um arquivo")
        print("2 - Sair do programa")
        print("============================")
        
        opcao = input("Escolha uma opcao (1 ou 2): ")
        
        if opcao == "1":
            arquivo_usuario = input("Digite o nome do arquivo txt: ")
            caractere_usuario = input("Digite o caractere que deseja buscar: ")
            contar_caractere(arquivo_usuario, caractere_usuario)
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida!")

exibir_menu()
