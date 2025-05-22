def formula(a, b):
    # Sem usar os operadores matemácios (+, -, /, *)
    # return ((a + b) * (a - b)) / 2
    # return divisao(multiplicacao(adicao(a, b), subtracao(a, b)), 2)
    soma = adicao(a, b)
    diferenca = subtracao(a, b)
    produto = multiplicacao(soma, diferenca)
    resultado = divisao(produto, 2)
    return resultado
