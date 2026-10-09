def soma_imposto(taxa_imposto, custo):
    return custo * (1 + taxa_imposto / 100)

print(f"""
      Valor do produto R$100,00
      Valor com imposto (10%):
      R${soma_imposto(10, 100):.2f}
      """)