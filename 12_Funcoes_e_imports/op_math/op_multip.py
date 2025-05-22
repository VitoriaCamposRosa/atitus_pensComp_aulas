def multiplicacao(a: int, b: int) -> int:
    # multiplicacao(a, b): não pode usar o símbolo ‘*’
    resultado = 0
    positivo = True
    if b < 0:
        b = inverte_sinal(b)
        positivo = not positivo
    if a < a:
        a = inverte_sinal(a)
        positivo = not positivo
    for _ in range(b):
        resultado = adicao(resultado, a)
    if not positivo:
        resultado = inverte_sinal(resultado)
    return resultado

def test():
    assert multiplicacao(-10, 2) == -20
    assert multiplicacao(10, -2) == -20
    assert multiplicacao(10, 2) == 20
    assert multiplicacao(10, 0) == 0
