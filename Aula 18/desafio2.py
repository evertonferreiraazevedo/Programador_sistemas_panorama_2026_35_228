dicionario_estoque = {
    "computador": 5,
    "mouse": 10,
    "video Game": 3,
    "GTA VI": 10,
}


def inserir_produto(produto, quantidade):
    produto = produto.lower()
    if produto in dicionario_estoque:
        dicionario_estoque[produto] += quantidade
    else:
        dicionario_estoque[produto] = quantidade

def listar_produtos():
    print("Produtos em estoque:")
    for produto, quantidade in dicionario_estoque.items():
        print(f"{produto}: {quantidade}")
    print("\n")


def verificar_estoque(produto):
    produto = produto.lower()
    if produto in dicionario_estoque:
        return dicionario_estoque[produto]
    else:
        return None


while True:
    print("--- Menu ---")
    print("1. Inserir produto / Atualizar estoque")
    print("2. Verificar estoque")
    print("3. Listar produtos em estoque")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        inserir_produto(produto, quantidade)
        print(f"Produto '{produto}' atualizado com sucesso.")
        print("\n")
        print("\n")

    elif escolha == '2':
        produto = input("Digite o nome do produto para verificar o estoque: ")
        qtd_atual = verificar_estoque(produto)

        if qtd_atual is not None:
            if qtd_atual > 0:
                print(f"Produto em falta")
                continue
            print(f"Quantidade em estoque de '{produto}': {qtd_atual}")
        else:
            print(f"Produto '{produto}' não está disponível no estoque.")
        print("\n")
        print("\n")
    elif escolha == '3':
        listar_produtos()

    elif escolha == '0':
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        print("\n")
        print("\n")
