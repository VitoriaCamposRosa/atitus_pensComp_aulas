def somatorio(numero):
    if numero == -1:
        return None
    for numero in range(10):
        print(numero, numero * (numero + 1) / 2)
        return numero

def test():
    assert somatorio(-1) is None
    assert somatorio(0) == 0
    assert somatorio(1) == 1
    assert somatorio(2) == 3
    assert somatorio(3) == 6
    assert somatorio(4) == 10
    assert somatorio(5) == 15
    assert somatorio(6) == 21
    assert somatorio(7) == 28
    assert somatorio(8) == 36
    assert somatorio(9) == 45

print("Terminou com sucesso!")
