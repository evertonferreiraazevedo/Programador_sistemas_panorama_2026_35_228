alunos_matriculados = {  "Carlos": 12, "Ana": 18,  "Mariana": 5,  "Pedro": 0}

while True:
    nome_aluno = input("Digite o nome do aluno (ou 'sair' para encerrar): ").strip()
    if nome_aluno.lower() == 'sair':
        print("Encerrando sistema da catraca.")
        break
    if nome_aluno in alunos_matriculados:
        print("\nAluno localizado!")
        print(f"Histórico atual: {alunos_matriculados[nome_aluno]} dias de treino este mês.")
        alunos_matriculados[nome_aluno] += 1
        print(f"Presença registrada! Novo total: {alunos_matriculados[nome_aluno]} dias.")
    else:
        print(f"\nAVISO: O aluno '{nome_aluno}' não possui matrícula ativa nesta unidade.")
