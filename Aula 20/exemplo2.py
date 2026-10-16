try:
    with open('exemplo.txt', 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    # O arquivo será fechado automaticamente após este bloco
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")