prontuarios_espera = {
    "João Oliveira": "Vermelho",
    "Beatriz Lima": "Amarelo",
    "Roberto Ribeiro": "Verde",
    "Juliana Neves": "Verde"
}

while True:
    nome_paciente = input("Digite o nome do paciente (ou 'sair' para encerrar): ").strip()
    if nome_paciente.lower() == 'sair':
        print("Encerrando consulta de prontuários.")
        break
    if nome_paciente in prontuarios_espera:
        cor_pulseira = prontuarios_espera[nome_paciente]
        print("\nPaciente encontrado na fila de espera!")
        print(f"Classificação de risco: Pulseira [{cor_pulseira}]")
    else:
        print(f"\nFicha médica não encontrada! O paciente '{nome_paciente}' precisa passar pela triagem inicial.")
