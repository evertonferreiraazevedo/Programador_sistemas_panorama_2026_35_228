
lista_numeros = [10, 5, 20, 10, 30, 5, 40, 50, 20, 10, 60, 70, 5, 80, 90, 100, 50]

lista_palavras = ["maçã", "banana", "laranja", "maçã", "uva",
                  "banana", "abacaxi", "melancia", "laranja", "morango",
                  "uva", "pera", "maçã", "abacate", "banana"
]

##################FUNCOES###########################
# tamanho_lista = len(lista_numeros)
# print(tamanho_lista)
# for i in range(len(lista_numeros)):
# print(len(lista_numeros))
# print(len(lista_palavras))
# print(sum(lista_numeros))
# # print(sum(lista_palavras)) #GERA UM ERRO
# print(min(lista_numeros))
# print(min(lista_palavras))
# print(max(lista_numeros))
# print(max(lista_palavras))
# print(sorted(lista_numeros))
# print(sorted(lista_palavras))
##################FUNCOES###########################


##################METODOS###########################
##################Add elementos###########################
# print(lista_numeros)
# lista_numeros.append(66)
# print(lista_numeros)
# lista_numeros.insert(0, 33)
# lista_numeros.insert(len(lista_numeros), 67)
# lista_numeros.extend([12, 76])
# print(lista_numeros)

##################excluir elementos###########################
# print(lista_palavras)
# lista_palavras.remove("laranja")
# print("\n\napos remover laranja", lista_palavras)
# var_retorno = lista_palavras.pop(5)
# print("\n\nElemento removido com pop do indice 5" ,var_retorno)
# print("\n\napos remover indice 5", lista_palavras)
# lista_palavras.clear()
# print("\n\napos remover TUDO",lista_palavras)

##################buscar elementos###########################
# print(lista_numeros.index(5))
# print(lista_numeros.count(5))

lista_decrescente = sorted(lista_palavras, reverse=True)
print(lista_decrescente)

lista_numeros.sort()
lista_numeros.reverse()
print(lista_numeros)