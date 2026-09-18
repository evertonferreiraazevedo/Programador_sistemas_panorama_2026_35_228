# rico = "não"
# while not rico == "sim":
#     print("Trabalhe!")
#     rico = input("Está rico ?")

# senha_correta = "1234"
# senha_digitada = input("Digite sua senha: ")
# tentativa = 1
# while senha_digitada != senha_correta:
#     senha_digitada = input("Senha incorreta, digite novamente: ")
#     tentativa +=  1
#     if tentativa == 3:
#         break
# print("Bem vindo!")
senha_correta = "1234"
tentativa = 1
while tentativa <= 3:
    senha_digitada = input(f"Digite sua senha (Tentativa {tentativa}/3): ")
    if senha_digitada == senha_correta:
        print("Bem vindo! Acesso concedido.")
        break
    else:
        print("Senha incorreta!")
        tentativa += 1
else:
    print("Acesso bloqueado! Você excedeu as 3 tentativas.")
