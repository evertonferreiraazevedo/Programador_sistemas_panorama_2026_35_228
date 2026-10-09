def listar():
    print("Lista de itens:")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
lista = []

print("###List System Ultimate### ")
opcao = ""
while opcao != "5":
    print("""
          1 - Add item
          2 - Visualizar Lista
          3 - Editar item
          4 - Remover item
          5 - Sair
          """)
    opcao = input("O que deseja fazer?")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista.append(item)
        print(f"Item '{item}' adicionado à lista.")
    elif opcao == "2":
        listar()
    elif opcao == "3":
        listar()
        indice = int(input("Digite o número do item que deseja editar: ")) - 1
        if 0 <= indice < len(lista):
            novo_item = input("Digite o novo valor para o item: ")
            lista[indice] = novo_item
            print(f"Item '{lista[indice]}' editado com sucesso.")
        else:
            print("Índice inválido.")
    elif opcao == "4":
        x
        indice = int(input("Digite o número do item que deseja remover: ")) - 1
        if 0 <= indice < len(lista):
            item_removido = lista.pop(indice)
            print(f"Item '{item_removido}' removido da lista.")
        else:
            print("Índice inválido.")
            
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
else:
    print("Programa encerrado.")