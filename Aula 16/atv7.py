def valor_pagamento(valor, atraso):
    if atraso > 0:
        multa = valor * 0.03
        juros = valor * 0.01 * atraso
        return valor + multa + juros
    else:
        return valor
    
principal = float(input("Digite o valor da prestação: "))
dias_atraso = int(input("Digite o número de dias em atraso: "))

total_a_pagar = valor_pagamento(principal, dias_atraso)

print(f"Valor a ser pago: R$ {total_a_pagar:.2f}")