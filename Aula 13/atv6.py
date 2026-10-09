# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []

for m in meses:
    temperaturas.append(float(input(f"Temperatura de {m}: ")))

media_anual = sum(temperaturas) / 12
print(f"Média anual: {media_anual:.1f}°C\nAcima da média:")

for i in range(12):
    if temperaturas[i] > media_anual:
        print(f"{i+1} - {meses[i]}: {temperaturas[i]}°C")
