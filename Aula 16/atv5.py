def palindromo(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]

print(palindromo("arara"))