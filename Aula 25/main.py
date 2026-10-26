import sqlite3
conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

def criar_banco():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Alunos (
                    ID INTEGER PRIMARY KEY,
                    Nome TEXT NOT NULL,
                    Idade INTEGER,
                    Curso TEXT) ''')
    # Confirmar a transação
    conexao.commit()

def inserir_dados():
    nome = input("Nome: ")
    idade = int(input("idade: "))
    disciplina = input("Curso: ")
    cursor.execute('''
        INSERT INTO Alunos (NOME, IDADE, CURSO) VALUES(?,?,?);''',
                   (nome, idade, disciplina))

    conexao.commit()

def consultar_dados():
    pass

def deletar_dados():
    pass

criar_banco()
while True:
    opcao = input("1 - Add, 2 - Consultar, 3 - Del")

    if opcao == "1":
        inserir_dados()
    elif opcao == "2":
        consultar_dados()
    elif opcao == "3":
        deletar_dados()
    else:
        print("opcao invalida")
