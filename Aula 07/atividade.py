# carteira = input("Tem carteira? ")
# carro = input("Tem carro? ")
# condCarteira = carteira == "sim"
# condCarro = carro == "sim"
# if condCarteira and condCarro:
#     print("Papocaaa")
# else:
#     print("UBER")
######################################################
idade = int(input("Tem idade suficiente? "))
titulo = input("Tem titulo? ")
if idade >= 16 and titulo == "sim":
    print("Voto consciente!")
else:
    print("Vai pagar multa!")
######################################################
valor = int(input("Valor da compra: "))
vip = input("És vip? ")
if valor >= 100 or vip == "sim":
    print("Desconto: ", (valor*0.9))
else:
    print("Lascou")