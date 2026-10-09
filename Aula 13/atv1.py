lista_notas = []
for i in range(4):
    nota = float(input(f"Digite a  {i+1}º nota: "))
    lista_notas.append(nota)
    
for i in range(4):
    print(f"Nota {i+1} - {lista_notas[i]}")
    
print(f"A média das notas é: {sum(lista_notas)/len(lista_notas)}")