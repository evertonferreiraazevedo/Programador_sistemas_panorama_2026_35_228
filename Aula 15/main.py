# def saudacao():
#     print("Ola voce!")
   
# saudacao()
# saudacao()
 
# def saudacao(nome):
#     print(f"Ola {nome}!")

# saudacao("Everton")
# saudacao("Mirela")
# nome_parametro = input("Digite seu nome: ")
# saudacao(nome_parametro)
 
# def motor_combustivel(combustivel):
#     print(f"Motor queimando {combustivel}!")
    
# abastecer = input("Digite o tipo de combustivel: ")
# motor_combustivel(abastecer)


# def somar_numeros(num1, num2):
#     print(num1 + num2)
    
# def subtracao_numeros(num1, num2):
#     print(num1 - num2)
    
# def multiplicacao_numeros(num1, num2):
#     print(num1 * num2)

# def divisao_numeros(num1, num2):
#     print(num1 / num2)

   
# opcao = input("""
#               Digite a operacao desejada 
#               1 -somar, 
#               2 -subtrair, 
#               3- multiplicar, 
#               4 -dividir): """)
# num1 = float(input("Digite o primeiro numero: "))   
# num2 = float(input("Digite o segundo numero: "))
# if opcao == "1":
#     somar_numeros(num1, num2)
# elif opcao == "2":
#     subtracao_numeros(num1, num2)
# elif opcao == "3":
#     multiplicacao_numeros(num1, num2)
# elif opcao == "4":
#     divisao_numeros(num1, num2) 
# else:
#     print("Operacao invalida!")


# def cozinhar(ingrediente, sal):
#     if sal == "sim":
#         return f"Cozinhando {ingrediente} com sal!"
#     else:
#         return f"Cozinhando {ingrediente} sem sal!"

# print(cozinhar("arroz", "sim"))
# print(cozinhar("feijao", "nao"))


# var_externa = "Variavel externa"
# def funcao_escopo():
#     print("Externa dentro da Funcao:", var_externa)
#     var_interna = "Variavel interna"
#     print("Interna dentro da Funcao:", var_interna)

# funcao_escopo()
# print("Externa fora da Funcao:", var_externa)
# # print("Interna fora da Funcao:", var_interna) # vai dar erro pois a variavel interna so existe dentro da funcao

# def funcao_escopo_retorno():
#     var_interna = "Variavel interna"
#     return var_interna

# var_retornada = funcao_escopo_retorno()
# print("Retornada fora da Funcao:", var_retornada)

def somar_numeros(num1, num2):
    return num1 + num2
    
def subtracao_numeros(num1, num2):
    return num1 - num2
    
def multiplicacao_numeros(num1, num2):
    return num1 * num2

def divisao_numeros(num1, num2):
    return num1 / num2

print(somar_numeros(10, 5))
print(subtracao_numeros(10, 5))
print(multiplicacao_numeros(10, 5))
print(divisao_numeros(10, 5))

