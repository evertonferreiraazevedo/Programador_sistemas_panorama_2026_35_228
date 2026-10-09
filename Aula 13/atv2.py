# Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_letras = []
consoates = 0
for i in range(10):
    letra = input("Digite um letra: ")
    lista_letras.append(letra)
    if letra not in "aeiouAEIOU":
        consoates += 1
        
print(lista_letras)        
for i in lista_letras:
    if i not in "aeiouAEIOU":
        print(i)
print("Total de consoates: ", consoates)


