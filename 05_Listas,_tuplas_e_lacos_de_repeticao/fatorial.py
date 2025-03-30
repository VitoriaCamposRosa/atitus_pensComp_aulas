def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    if numero < 0:
        return None
    for numero < 0:
        return numero * fatorial(numero - 1)
    
def test():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120
    assert fatorial(-1) is None

print("Terminou com sucesso!")