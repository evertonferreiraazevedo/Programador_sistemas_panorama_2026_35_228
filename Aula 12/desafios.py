# lista_numeros = [32,15,78,32,13,240,15,78,9,1]
# for i in range(len(lista_numeros)):
#     if lista_numeros[i] % 2 == 0:
#         lista_numeros[i] = "ZERO"
# print(lista_numeros)

lista_numeros = []
lista_pares = []
lista_impares = []

for i in range(20):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)
    
for i in range(20):
    if lista_numeros[i] % 2 == 0:
        lista_pares.append(lista_numeros[i])
    else:
        lista_impares.append(lista_numeros[i])
        
print(f"""
      Numeros: {lista_numeros}
      pares: {lista_pares}
      impares: {lista_impares}""")
