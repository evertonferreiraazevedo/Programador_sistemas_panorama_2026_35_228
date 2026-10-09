ingles_portugues = {
    'apple': 'maçã',
    'banana': 'banana',
    'orange': 'laranja',
    'grape': 'uva',
    'watermelon': 'melancia',
}
def traduzir_palavra(palavra):
    palavra = palavra.lower()
    if palavra in ingles_portugues:
        return ingles_portugues[palavra]
    else:
        print("Palavra não encontrada no dicionário.")
        opcap = input("Deseja add no dicionário? (s/n): ")
        if opcap.lower() == 's':
            traducao = input("Tradução em português: ")
            add_palavra(palavra, traducao)
            print(f"Palavra add ao dicionário.")
            return traducao
        else:
            return
        
        
        
        
        
        

def add_palavra(ingles, portugues):
    ingles_portugues[ingles] = portugues
    
while True:
    print("\nMenu:")
    print("1. Traduzir palavra")
    print("0. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        palavra = input("Digite a palavra em inglês: ")
        traducao = traduzir_palavra(palavra)
        print(f"Tradução: {traducao}")
    elif escolha == '0':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        