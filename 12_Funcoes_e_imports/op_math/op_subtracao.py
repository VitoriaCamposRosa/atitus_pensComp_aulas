def subtracao(valor1: int, valor2: int) -> int:
    # subtracao(a, b): não pode usar o símbolo ‘-’
    return adicao(valor1, inverte_sinal(valor2)) 

def test():
    assert subtracao(-10, 2) == -12
    assert subtracao(10, -2) == 12
    assert subtracao(-10, -2) == -14
    assert subtracao(10, 2) == 8
    assert subtracao(10, 0) == 10   
 