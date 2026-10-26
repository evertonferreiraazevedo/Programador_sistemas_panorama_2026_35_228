import json


def carregar_json():
    #Abre o arquivo com segurança contra arquivos corrompidos ou inexistentes.
    try:
        with open("alunos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # Garante que o JSON tem o formato de dicionário e contém a lista de alunos
            if isinstance(dados, dict) and isinstance(dados.get("alunos"), list ):
                return dados
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro crítico: Arquivo não encontrado ou JSON corrompido.")

    return None


def encontrar_problemas(aluno, ids_ja_vistos):
    #Analisa o aluno e devolve uma lista com todos os erros encontrados nele.
    erros = []

    # Erro 1: O registro inteiro não é um objeto/dicionário
    if not isinstance(aluno, dict):
        return ["Registro corrompido (não é um objeto)."]

    id_aluno = aluno.get("id")
    nome = aluno.get("nome")
    notas = aluno.get("notas")
    ativo = aluno.get("ativo")

    # Erro 2: Problemas com o ID (não é número, é booleano ou está duplicado)
    if not isinstance(id_aluno, int) or isinstance(id_aluno, bool):
        erros.append("ID inválido.")
    elif id_aluno in ids_ja_vistos:
        erros.append(f"ID duplicado: {id_aluno}.")

    # Erro 3: Nome ausente ou vazio
    if not isinstance(nome, str) or not nome.strip():
        erros.append("Nome ausente ou vazio.")

    # Erro 4: Problemas com o campo 'ativo'
    if not isinstance(ativo, bool):
        erros.append("Campo 'ativo' deve ser True ou False.")

    # Erro 5: Problemas estruturais nas notas
    if not isinstance(notas, list):
        erros.append("Campo 'notas' ausente ou inválido.")
    elif len(notas) == 0:
        erros.append("Aluno não possui notas cadastradas.")
    else:
        # Erro 6: Problemas em alguma nota específica da lista
        for nota in notas:
            if not isinstance(nota, (int, float)) or isinstance(nota, bool):
                erros.append(f"Nota inválida (não numérica): {nota}.")
                break  # Para na primeira nota ruim

            if nota < 0 or nota > 10:
                erros.append(
                    f"Nota fora do intervalo permitido (0 a 10): {nota}."
                )
                break

    return erros


def processar_turma(lista_alunos):
    ids_ja_vistos = set()
    registros_finais = []
    medias_validas = []

    aprovados = 0
    reprovados = 0

    for aluno in lista_alunos:
        erros = encontrar_problemas(aluno, ids_ja_vistos)

        # Se o ID for válido, guardamos para rastrear duplicatas no próximo aluno
        if (isinstance(aluno, dict) and isinstance(aluno.get("id"), int) and not isinstance(aluno.get("id"), bool) ):
            ids_ja_vistos.add(aluno["id"])

        # 2. Se NÃO houver erros, calcula a média e define o resultado
        if len(erros) == 0:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            medias_validas.append(media)

            if media >= 7:
                resultado = "Aprovado"
                aprovados += 1
            else:
                resultado = "Reprovado"
                reprovados += 1
        else:
            # Se houver qualquer erro no aluno, ele não é avaliado
            media = None
            resultado = "Não avaliado"

        # 3. Descobre o nome do aluno por extenso
        if isinstance(aluno, dict):
            nome_aluno = aluno.get("nome", "Desconhecido")
        else:
            nome_aluno = "Registro Inválido"

        # 4. Formata a média para exibir no terminal
        if media is not None:
            media_texto = f"{media:.2f}"
        else:
            media_texto = "N/A"

        print(
            f"Aluno: {nome_aluno} | Média: {media_texto} | Status: {resultado}"
        )
        for erro in erros:
            print(f"  └─ Motivo: {erro}")

        # 5. Descobre o ID com segurança (sem resumo)
        if isinstance(aluno, dict):
            id_final = aluno.get("id")
        else:
            id_final = None

        # 6. Arredonda a média se ela existir
        if media is not None:
            media_final = round(media, 2)
        else:
            media_final = None

        # 7. Monta o dicionário de dados limpos do aluno
        dados_do_aluno = {
            "id": id_final,
            "nome": nome_aluno,
            "media": media_final,
            "resultado": resultado,
            "problemas": erros,
        }

        registros_finais.append(dados_do_aluno)

    # 8. Faz as contas gerais do fim do relatório
    if medias_validas:
        media_geral = sum(medias_validas) / len(medias_validas)
    else:
        media_geral = 0

    return {
        "total_registros": len(lista_alunos),
        "total_validos": len(medias_validas),
        "aprovados": aprovados,
        "reprovados": reprovados,
        "media_geral": round(media_geral, 2),
        "registros": registros_finais,
    }


def salvar_relatorio(relatorio):
    with open("relatorio.json", "w", encoding="utf-8") as arquivo:
        json.dump(relatorio, arquivo, indent=4, ensure_ascii=False)
    print("\nRelatório final gerado com sucesso!")



dados_json = carregar_json()

if dados_json:
    if dados_json.get("turma"):
        nome_turma = dados_json.get("turma")
    else:
        nome_turma = "Sem Nome"

    print(f"Processando Turma: {nome_turma}")

    relatorio = processar_turma(dados_json["alunos"])
    salvar_relatorio(relatorio)




############################################################################################

# import json

# def carregar_dados():
#     try:
#         with open("alunos.json", "r", encoding="utf-8") as arquivo:
#             return json.load(arquivo)

#     except FileNotFoundError:
#         print("Erro: arquivo alunos.json não encontrado.")

#     except json.JSONDecodeError:
#         print("Erro: arquivo JSON inválido.")

#     return None

# def validar_aluno(aluno, ids_encontrados):
#     problemas = []

#     if not isinstance(aluno, dict):
#         return ["Registro inválido."], None

#     aluno_id = aluno.get("id")
#     nome = aluno.get("nome")
#     notas = aluno.get("notas")
#     ativo = aluno.get("ativo")

#     # Validar ID
#     if not isinstance(aluno_id, int) or isinstance(aluno_id, bool):
#         problemas.append("ID inválido.")
#     elif aluno_id in ids_encontrados:
#         problemas.append(f"ID duplicado: {aluno_id}.")
#     else:
#         ids_encontrados.add(aluno_id)

#     # Validar nome
#     if not isinstance(nome, str) or not nome.strip():
#         problemas.append("Nome ausente ou vazio.")

#     # Validar notas
#     if not isinstance(notas, list):
#         problemas.append("Campo 'notas' ausente ou inválido.")
#         return problemas, None

#     if len(notas) == 0:
#         problemas.append("Aluno sem notas.")
#         return problemas, None

#     for nota in notas:
#         if not isinstance(nota, (int, float)) or isinstance(nota, bool):
#             problemas.append(f"Nota não numérica: {nota!r}.")
#             return problemas, None

#         if nota < 0 or nota > 10:
#             problemas.append(f"Nota fora do intervalo: {nota}.")
#             return problemas, None

#     # Validar situação
#     if not isinstance(ativo, bool):
#         problemas.append("Campo 'ativo' deve ser booleano.")

#     media = sum(notas) / len(notas)

#     return problemas, media

# def calcular_resultado(media):
#     if media is None:
#         return "Não avaliado"

#     if media >= 7:
#         return "Aprovado"

#     return "Reprovado"

# def processar_alunos(alunos):
#     ids_encontrados = set()
#     medias_validas = []
#     registros = []
#     aprovados = 0
#     reprovados = 0

#     for indice, aluno in enumerate(alunos, start=1):
#         problemas, media = validar_aluno(
#             aluno, ids_encontrados
#         )

#         # Não contabilizar registros com ID duplicado
#         if (
#             isinstance(aluno, dict)
#             and isinstance(aluno.get("id"), int)
#             and not isinstance(aluno.get("id"), bool)
#         ):
#             quantidade_ids = sum(
#                 1 for registro in registros
#                 if registro.get("id") == aluno["id"]
#             )

#             if quantidade_ids > 0:
#                 media = None
#                 problemas.append(
#                     "Registro não contabilizado por ID duplicado."
#                 )

#         resultado = calcular_resultado(media)

#         if media is not None:
#             medias_validas.append(media)

#             if resultado == "Aprovado":
#                 aprovados += 1
#             elif resultado == "Reprovado":
#                 reprovados += 1

#         nome = (
#             aluno.get("nome", "Não informado")
#             if isinstance(aluno, dict)
#             else "Registro inválido"
#         )

#         registro = {
#             "id": aluno.get("id") if isinstance(aluno, dict) else None,
#             "nome": nome,
#             "media": round(media, 2) if media is not None else None,
#             "resultado": resultado,
#             "problemas": problemas
#         }

#         registros.append(registro)

#         situacao = (
#             "Ativo" if aluno.get("ativo") is True
#             else "Inativo" if aluno.get("ativo") is False
#             else "Inválida"
#         ) if isinstance(aluno, dict) else "Inválida"

#         media_texto = (
#             f"{media:.2f}" if media is not None
#             else "Indisponível"
#         )

#         print(
#             f"{nome} | Média: {media_texto} | "
#             f"Situação: {situacao} | Resultado: {resultado}"
#         )

#         for problema in problemas:
#             print("  Problema:", problema)

#     media_geral = (
#         sum(medias_validas) / len(medias_validas)
#         if medias_validas else None
#     )

#     return {
#         "total_registros": len(alunos),
#         "total_medias_validas": len(medias_validas),
#         "media_geral": round(media_geral, 2) if media_geral is not None else None,
#         "aprovados": aprovados,
#         "reprovados": reprovados,
#         "registros": registros
#     }

# def salvar_relatorio(relatorio):
#     try:
#         with open("relatorio.json", "w", encoding="utf-8") as arquivo:
#             json.dump(
#                 relatorio,
#                 arquivo,
#                 ensure_ascii=False,
#                 indent=4
#             )

#         print("\nRelatório salvo com sucesso!")

#     except OSError as erro:
#         print("Erro ao salvar relatório:", erro)

# def main():
#     dados = carregar_dados()

#     if dados is None:
#         return

#     if not isinstance(dados, dict):
#         print("Erro: estrutura principal do JSON inválida.")
#         return

#     alunos = dados.get("alunos")

#     if not isinstance(alunos, list):
#         print("Erro: a chave 'alunos' deve conter uma lista.")
#         return

#     print("Turma:", dados.get("turma", "Não informada"))
#     print("-" * 50)

#     relatorio = processar_alunos(alunos)
#     relatorio["turma"] = dados.get("turma", "Não informada")

#     print("\n--- RESUMO ---")
#     print("Total de registros:", relatorio["total_registros"])
#     print("Médias válidas:", relatorio["total_medias_validas"])
#     print("Aprovados:", relatorio["aprovados"])
#     print("Reprovados:", relatorio["reprovados"])
#     print("Média geral:", relatorio["media_geral"])

#     salvar_relatorio(relatorio)

# main()