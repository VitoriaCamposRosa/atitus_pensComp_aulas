def divisao(a: int, b: int) -> int | None:
    # divisao(a, b): não pode usar o símbolo ‘/’
    if b == 0:
        return None

    positivo = True
    if a < 0:
        a = inverte_sinal(a)
        positivo = not positivo 
    if b < 0:
        b = inverte_sinal(b)
        positivo = not positivo
     
    resultado = 0
    acumulado = 0
    while acumulado <= a: 
        acumulado = adicao(acumulado, b)
        if acumulado <= a:
            resultado = adicao(resultado, 1)

    if not positivo:
        resultado = inverte_sinal(resultado)

    return resultado
     
def test():
    assert divisao(-10, 2) == -5
    assert divisao(10, -2) == -5
    assert divisao(10, 2) == 5
    assert divisao(10, 0) is None
