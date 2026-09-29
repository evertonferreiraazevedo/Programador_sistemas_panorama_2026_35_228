# numero = 10
# lista_numeros = [33,24,3,47,5,665]
# print(numero)
# print(lista_numeros)
# print(lista_numeros[0])
# print(lista_numeros[5])
# print(lista_numeros[2] + lista_numeros[3])
# print(lista_numeros[10])

# coisas = [1,"everton", 0.5, True]
# print(coisas[1])
# print(coisas[-1])
# print(coisas[0:2])
# print(coisas[-3:-1])
# letras = ['a', 'b', 'c', 'd', 'e']
# letras[0] = 'z'
# print(letras)
# letras[1:3] = ['x', 'y']
# print(letras)
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# print("Tamanho da lista:", len(lista)) # Saída: Tamanho da lista: 10
# print("Soma dos elementos:", sum(lista)) # Saída: Soma dos elementos: 39
# print("Menor elemento:", min(lista)) # Saída: Menor elemento: 1
# print("Maior elemento:", max(lista)) # Saída: Maior elemento: 9
# print("Lista ordenada:", sorted(lista)) # Saída: Lista ordenada: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

lista_palavras = ["banana", "abacaxi", "laranja", "uva", "maçã"]
# print(len(lista_palavras))
# # print(sum(lista_palavras)) ERRO
# print(min(lista_palavras))
# print(max(lista_palavras))
# print(sorted(lista_palavras))
cores = ["preto", "branco"]
# cores.append("roxo")
# print(cores)
# cores.append("rosa")
# print(cores)
# cores.insert(0, "roxo")
# print(cores)
# cores.insert(0, "vermelho")
# print(cores)
# cores.insert(3, "ciano")
# print(cores)
# cores.extend(["roxo", "vermelho", "ciano"])
# print(cores)

lista_compras=[]
for i in range(3):
    lista_compras.append(input("Digite o produto: "))
# print('Lista: ', lista_compras)
for i in range(len(lista_compras)):
    print(lista_compras[i])