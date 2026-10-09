# # nome_dicionario = {"Alice": 25, "Bob": 30, "Charlie": 35}
# dic_everton = {"Nome": "Everton",
#                "idade": 31,
#                "altura": 1.75,
#                "peso": 75,
#                "profissao": "Engenheiro de Software",}
# lista = ["Everton", 31, 1.75, 75, "Engenheiro de Software"]
# # print(dic_everton)
# # print(lista)

# print(f"Nome: {lista[0]}")
# print(f"Nome: {dic_everton['Nome']}")

# frutas = {'maça': 5, 'banana': 3, 'laranja': 7}
# print(frutas)
# frutas['maça'] = 10  # Atualiza o valor da chave 'maça'
# frutas['uva'] = 4  # Adiciona uma nova chave 'uva'
# print(frutas)
# del frutas['banana']  # Remove a chave 'banana'
# print(frutas)

# chaves = frutas.keys()  # Obtém as chaves do dicionário
# valores = frutas.values()  # Obtém os valores do dicionário
# duplas = frutas.items()  # Obtém as duplas (chave, valor) do dicionário
# print(chaves)
# print(valores)
# print(duplas)

dicionario_alunos = {
    "everton": 10,
    "joao": 8,
    "maria": 9,
    "ana": 7,
}
# for i in dicionario_alunos:
#     print(i, " : ",dicionario_alunos[i]) 
for chave, valor in dicionario_alunos.items():
    print(chave, " : ", valor)