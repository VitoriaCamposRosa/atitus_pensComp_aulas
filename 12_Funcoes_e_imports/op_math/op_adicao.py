def adicao(valor1: int, valor2: int) -> int:
    # soma(a, b): apenas pode fazer ‘soma(x, 1)’ (sem somar a e b)
    resultado = valor1
    if valor2 >= 0:
        for _ in range(valor2):
            resultado += 1
    else: 
        for _ in range(-valor2):
            resultado -= 1
    return resultado

def test():
    assert adicao(1, 2) == 3
    assert adicao(1, 0) == 1
    assert adicao(-1, -2) == -3
