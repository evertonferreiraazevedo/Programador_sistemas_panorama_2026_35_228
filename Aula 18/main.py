def printar_pessoa(pessoa):
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Cidade Natal: {pessoa['cidade_natal']}")
    print(f"Profissão: {pessoa['profissao']}")
    if "email" in pessoa:
        print(f"Email: {pessoa['email']}")
    if "telefone" in pessoa:
        print(f"Telefone: {pessoa['telefone']}")

def gerenciar_pessoa():
    # Questão 1: Criando o dicionário
    pessoa = {
        "nome": "Everton Azeveo",
        "idade": 31,
        "cidade_natal": "Fortaleza",
        "profissao": "Instrutor de TI",
    }

    # Questão 2: Acessando e imprimindo valores
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")

    # Questão 3: Modificando um item
    pessoa["profissao"] = "Aposentado"
    print(f"Profissão Modificada: ")
    printar_pessoa(pessoa)

    # Questão 4: Adicionando informações extras
    pessoa["email"] = "eumesmo@email.com"
    pessoa["telefone"] = "(85) 99999-1111"
    print(f"Contatos Adicionados")
    printar_pessoa(pessoa)

    # Questão 5: Removendo um item
    del pessoa["telefone"]
    print(f"Telefone Removido")
    printar_pessoa(pessoa)

def gerenciar_amigos():
    # Questão 6: Criando o dicionário e usando o loop para listar
    amigos = {
        "Ana": 25,
        "Bruno": 30,
        "Camila": 22,
        "Diego": 27
    }
    print("Lista de Amigos ")
    for nome, idade in amigos.items():
        print(f"Amigo(a): {nome} | Idade: {idade} anos")

    # Questão 7: Verificando se o amigo existe
    busca = input("Digite o nome de um amigo para buscar: ")
    if busca in amigos:
        print(f"Resultado: {busca} está na lista e tem {amigos[busca]} anos.")
    else:
        print(f"Resultado: {busca} não foi encontrado.")

    # Questão 8: Contando os amigos
    print(f"Total de amigos no dicionário: {len(amigos)}")

gerenciar_pessoa()
gerenciar_amigos()
