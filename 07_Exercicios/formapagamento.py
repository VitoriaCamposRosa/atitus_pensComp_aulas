def forma_pagamento(valor, forma_pgto):
    if forma_pgto not in [1, 2, 3, 4]:
        return "Opção inválida. Por favor, escolha uma das opções listadas."
    else:
        if forma_pgto == 1:
            resultado = valor - (valor * (15 / 100))
            return f"Valor com desconto de 15%: R${resultado:.2f}"
        elif forma_pgto == 2:
            resultado = valor - (valor * (10 / 100))
            return f"Valor com desconto de 10%: R${resultado:.2f}"
        elif forma_pgto == 3:
            return f"Parcelado em 2x sem juros. Valor total: R${valor}"
        elif forma_pgto == 4:
            resultado = valor + (valor * (10 / 100))
            return f"Valor com acréscimo de 10%: R${resultado:.2f}"

def test():
    assert calcula_valor_final(1000, 1) == "Valor com desconto de 15%: R$850.00"
    assert calcula_valor_final(1000, 2) == "Valor com desconto de 10%: R$900.00"
    assert calcula_valor_final(1000, 3) == "Parcelado em 2x sem juros. Valor total: R$1000.00"
    assert calcula_valor_final(1000, 4) == "Valor com acréscimo de 10%: R$1100.00"
    assert calcula_valor_final(1000, 5) == "Opção inválida. Por favor, escolha uma das opções listadas."
