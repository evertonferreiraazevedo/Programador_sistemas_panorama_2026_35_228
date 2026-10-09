# Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
vetor1 = []
vetor2 = []
vetor3 = []
print("Elementos do Primeiro Vetor")
for i in range(10):
    elemento = int(input(f"Elemento {i+1}: "))
    vetor1.append(elemento)
print("Elementos do Segundo Vetor")
for i in range(10):
    elemento = int(input(f"Elemento {i+1}: "))
    vetor2.append(elemento)
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(f"Vetor Intercalado: {vetor3}")
