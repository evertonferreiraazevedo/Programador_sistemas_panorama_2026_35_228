def contar_vogais(string):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in string:
        if char in vogais:
            contador += 1
    return contador

print(contar_vogais("ola mundo"))