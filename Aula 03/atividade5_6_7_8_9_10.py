peso = float(input("Peso: "))
altura = float(input("Altura: "))
imc = peso / altura ** 2
print(f"IMC: {imc:.2f}")

##############################################
sal_hora = float(input("Valor R$ hora? "))
horas_trabalhadas = float(input("Horas trabalhadas mês? "))
salario_bruto = sal_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Imposto de Renda (11%): R$ {ir:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

###############################################

valor_pizza = float(input("Valor pizza? "))
pizzas_vendidas = float(input("Pizzas vendidas? "))
faturamento_bruto = valor_pizza * pizzas_vendidas
custo_fixos = faturamento_bruto * 0.3
custo_variavel = faturamento_bruto * 0.2
faturamento_liquido = faturamento_bruto - custo_fixos - custo_variavel
print(f"Fat bruto: R$ {faturamento_bruto:.2f}")
print(f"fat líquido: R$ {faturamento_liquido:.2f}")
# ###############################################

temp_celsius = float(input("Digite a temperatura em Celsius: "))
temp_fahrenheit = (temp_celsius * 9/5) + 32
print(f"Temperatura em Fahrenheit: {temp_fahrenheit:.2f} °F")

################################################

valor_metros = float(input("Valor em metros: "))
valor_centimetros = valor_metros * 100
valor_milimetros = valor_metros * 1000
print(f"Valor em centímetros: {valor_centimetros:.2f} cm")
print(f"Valor em milímetros: {valor_milimetros:.2f} mm")

###############################################

valor_base = float(input("base do retângulo: "))
valor_altura = float(input("Altura do retângulo: "))
perimetro = 2 * (valor_base + valor_altura)
area = valor_base * valor_altura
print(f"Perímetro do retângulo: {perimetro:.2f}")
print(f"Área do retângulo: {area:.2f}")

################################################

idade_anos = int(input("Idade em anos: "))
idade_dias = idade_anos * 365
print(f"Sua idade em dias é: {idade_dias} dias")
