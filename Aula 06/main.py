nota = float(input("Nota do aluno: "))
freq = float(input("frequencia do aluno: "))
if (nota >= 7) and (freq >= 75):
    print("Aprovado")
else:
    print("Reprovado")
###########################################
convt = str(input("Convite: "))
vip = str(input("Conhece o Neymar?: "))
if (convt == "s") or (vip == "s"):
    print("Bem vindo a festa do nJr")
else:
    print("Dorme que passa")
###########################################
chovendo = True
if not chovendo:
    print("Praia")
else:
    print("Agarradinho")