import json

def ler_historico(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
        return None

def calcular_tempo_usuario(dados, nome_usuario):
    try:
        tempo_total_segundos = 0
        for item in dados:
            if item.get("usuario") == nome_usuario:
                tempo_total_segundos += item.get("duracao_segundos", 0)
        
        return tempo_total_segundos / 60
    except Exception as e:
        print(f"Erro ao processar os dados do usuário: {e}")
        return 0

def salvar_relatorio(caminho_saida, relatorio):
    try:
        with open(caminho_saida, "w", encoding="utf-8") as arquivo_saida:
            json.dump(relatorio, arquivo_saida, indent=4, ensure_ascii=False)
        print(f"Relatório gerado com sucesso em '{caminho_saida}'!")
        return True
    except Exception as e:
        print(f"Erro ao salvar o relatório: {e}")
        return False

def gerar_relatorio(pessoa):
    arquivo_entrada = "musicas.json"
    arquivo_saida = "relatorio_"+pessoa+".json"
    usuario_alvo = pessoa

    dados = ler_historico(arquivo_entrada)
    if dados is None:
        return

    tempo_minutos = calcular_tempo_usuario(dados, usuario_alvo)

    relatorio = {
        "usuario": usuario_alvo,
        "tempo_total_minutos": tempo_minutos
    }

    salvar_relatorio(arquivo_saida, relatorio)

# Executa o programa diretamente
pessoa = input("Digite o nome da pessoa para gerar o relatorio: ")
gerar_relatorio(pessoa)
