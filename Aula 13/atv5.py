# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
import random
idades = []
alturas = []
for i in range(30):
    print(f"Aluno {i+1}")
    idade = int(input("Idade: "))
    # idade = random.randint(5, 30)
    altura = float(input("Altura (em metros): "))
    # altura = random.uniform(1.30, 2.00)
    idades.append(idade)
    alturas.append(altura)
media_altura = sum(alturas) / len(alturas)
contador = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_altura:
        contador = contador + 1
print(f"Média de altura geral: {media_altura:.2f}m")
print(f"Alunos com mais de 13 anos abaixo da média: {contador}")
