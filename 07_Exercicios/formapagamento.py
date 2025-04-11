valor = int(input("Digite um valor: "))
print("O valor escolhido foi:", valor)
print()
forma_pgto = int(input("Escolha uma forma de Pagamento! 1 - para PIX, 2 - Para À Vista, 3 - Parcelado em 2x sem juros, 4 - Parcelado em 3x ou mais com juros"))

if forma_pagto not in [1, 2, 3, 4]:
    print("Opção inválida. Por favor, escolha uma das opções listadas.")
else:
    if forma_pagto == 1:
        resultado = valor - (valor * (15 / 100))
        print(f"Valor com desconto de 15%: R${resultado:.2f}")
    elif forma_pagto == 2:
        resultado = valor - (valor * (10 / 100))
        print(f"Valor com desconto de 10%: R${resultado:.2f}")
    elif forma_pagto == 3:
        print(f"Parcelado em 2x sem juros. Valor total: R${valor}")
    elif forma_pagto == 4:
        resultado = valor + (valor * (10 / 100))
        print(f"Valor com acréscimo de 10%: R${resultado:.2f}")
