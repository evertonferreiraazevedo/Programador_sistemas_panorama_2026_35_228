# 

# for i in range(10):
#     print(i)
#     print("FIM")

# num1 = int(input("Digite o primeiro numero: "))
# num2 = int(input("Digite o segundo numero: "))
# for i in range(num1, num2+1):
#     print(i)


#questao 1 
# for i in range (21):
#     if i % 2 != 0 : 
#         print(i)
        
#questa 2 
# numero = int(input("Digite um numero: "))
# soma = 0
# for i in range(1, numero+1):
#     soma += i
# print(f"A soma total é {soma} ")

#questao 3 
# numero = int(input("Digite um numero: "))
# for i in range(11):
#     print(numero * i)

# questao 4
# numero = int(input("Digite um numero: "))
# fat = 1
# for i in range(1, numero+1):
#     fat *= i
    
# print(f"O fatorial de {numero} é {fat} ")

#questao 5
# for i in range(10, 0, -1):
#     print(i)
    
#questao 6
# soma_pares = 0
# for numero in range(2, 51, 2):
#     soma_pares += numero
#     print(soma_pares)
# print(f"A soma de todos os números pares de 1 a 50 é: {soma_pares}")

#questao 7
# palavra = input("Digite uma palavra: ")
# for letra in palavra:
#     print(letra)    
    
# questao 8    
# frase = input("Digite uma frase: ")
# contador = 0
# for letra in frase:
#     if letra != " " and letra not in "aeiouAEIOU" :
#         contador += 1
# print(f"A quantidade de caracteres é: {contador}")



#questao 9
# a = 0
# b = 1
# for i in range(10):
#     print(a)
#     termo_atual = a
#     a = b
#     b = termo_atual + b

# questao 10
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
for i in range(expoente):
    resultado = resultado * base

print("Resultado:", resultado)
