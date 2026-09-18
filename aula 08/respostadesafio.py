print("--- SISTEMA DE POUSO FORÇADO ---")
combustivel = float(input("Digite a porcentagem de combustível (0-100): "))
atmosfera_respiravel = input(
    "A atmosfera do planeta é respirável? (sim/nao): ").strip().lower()
traje_integridade = float(
    input("Digite a porcentagem de integridade do traje: "))
atmosfera_respiravel = atmosfera_respiravel == "sim"
if combustivel >= 15 and (atmosfera_respiravel or traje_integridade == 100):
    print("Iniciando Protocolo de Pouso")
if not (combustivel >= 15 and (atmosfera_respiravel or traje_integridade == 100)):
    print("Pouso Abortado: Risco de Morte")

##############################################################################################################
# --- PARTE 2: ROTA DE FUGA ---
print("\n--- SISTEMA DE NAVEGAÇÃO DE FUGA ---")
opcao_escolhida = int(input(
    "Escolha sua rota de fuga [1 para Ponte Leste / 2 para Túnel Subterrâneo]: "))
# Processamento se o usuário escolher a Opção 1 (Ponte Leste)
if opcao_escolhida == 1:
    veiculo_blindado = input("Você possui um veículo blindado? (sim/nao): ").strip().lower()
    ponte_intacta = input("A ponte está intacta? (sim/nao): ").strip().lower()
    veiculo_blindado = veiculo_blindado == "sim"
    ponte_intacta = ponte_intacta == "sim"
    if veiculo_blindado and ponte_intacta:
        print("Sucesso: Fuga concluída pela Ponte Leste!")
    if not (veiculo_blindado and ponte_intacta):
        print("Fracasso: Condições insuficientes para atravessar a Ponte Leste.")
# Processamento se o usuário escolher a Opção 2 (Túnel Subterrâneo)
if opcao_escolhida == 2:
    mascaras_de_gas = input("Você possui máscaras de gás? (sim/nao): ").strip().lower()
    cartao_acesso = input("Você possui o cartão de acesso? (sim/nao): ").strip().lower()
    mascaras_de_gas = mascaras_de_gas == "sim"
    cartao_acesso = cartao_acesso == "sim"
    if mascaras_de_gas and cartao_acesso:
        print("Sucesso: Fuga concluída pelo Túnel Subterrâneo!")
    if not (mascaras_de_gas and cartao_acesso):
        print("Fracasso: Condições insuficientes para atravessar o Túnel Subterrâneo.")
# Caso o usuário digite um caminho inválido
if opcao_escolhida != 1 and opcao_escolhida != 2:
    print("Erro: Rota desconhecida. O grupo foi capturado!")
