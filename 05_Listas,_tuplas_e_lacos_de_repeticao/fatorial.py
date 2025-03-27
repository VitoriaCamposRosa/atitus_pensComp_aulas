def fatorial(numero):
    if numero == 0:
        return 1
    if numero == -1:
        return None
    for numero in range(6):
        print(numero, numero * fatorial (numero - 1))
        return numero
    
def test():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120
    assert fatorial(-1) is None

print("Terminou com sucesso!")