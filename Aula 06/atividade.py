nota = float(input("DIgite uma nota: "))
if nota <= 7:
    print("Reprovado")
else:
    print("Aprovado")
    
####################################################
turno = input("M, V ou N? ")
if turno ==  "M":
    print("Bom dia!")
elif turno ==  "V":
    print("Boa Tarde!")
elif turno ==  "N":
    print("Boa noite!")
else: 
    print("Invalido")

    
####################################################
numero = int(input("Digite um numero: "))
if not numero % 2 == 0:
    print("impar")
else:
    print("par")
####################################################
qntd = float(input("Quanto Kg de peixe"))
if qntd > 50 :
    print(f"Multado em {(qntd-50)*4}")
else:
    print("Sem multas")