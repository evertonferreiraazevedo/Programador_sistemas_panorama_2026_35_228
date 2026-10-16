def substituir_vogais(nome_entrada, nome_saida):
    try:
        with open(nome_entrada, "r", encoding="utf-8") as arquivo_in:
            conteudo = arquivo_in.read()
        vogais = "aeiouAEIOU"
        novo_conteudo = ""
        for caractere in conteudo:
            if caractere in vogais:
                novo_conteudo += "*"
            else:
                novo_conteudo += caractere 
        with open(nome_saida, "w", encoding="utf-8") as arquivo_out:
            arquivo_out.write(novo_conteudo)
        print(f"Arquivo gerado com sucesso: {nome_saida}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_entrada}' nao foi encontrado.")

def exibir_menu():
    while True:
        print("====== MENU PRINCIPAL ======")
        print("1 - Substituir vogais por '*'")
        print("2 - Sair do programa")
        print("============================")
        
        opcao = input("Escolha uma opcao (1 ou 2): ")
        
        if opcao == "1":
            arquivo_usuario = input("Digite o nome do arquivo de entrada txt: ")
            arquivo_destino = input("Digite o nome do novo arquivo de saida txt: ")
            substituir_vogais(arquivo_usuario, arquivo_destino)
        elif opcao == "2":
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida!")

exibir_menu()
