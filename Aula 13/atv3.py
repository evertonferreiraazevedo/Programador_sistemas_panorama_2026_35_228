# Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias_alunos = []
for aluno in range(10):
    print(f"Notas do {aluno + 1}º Aluno")
    lista_notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        lista_notas.append(nota)
    media = sum(lista_notas) / len(lista_notas)
    medias_alunos.append(media)
alunos_aprovados = 0
for media in medias_alunos:
    if media >= 7.0:
        alunos_aprovados += 1
print(f"Alunos com média >= 7: {alunos_aprovados}")

##########################################################

medias = []
while len(medias) < 10:
    print(f"\nAluno {len(medias) + 1}")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    n4 = float(input("Nota 4: "))
    medias.append((n1 + n2 + n3 + n4) / 4)
aprovados = 0
for m in medias:
    if m >= 7.0:
        aprovados += 1
print(f"Alunos com média >= 7.0: {aprovados}")
