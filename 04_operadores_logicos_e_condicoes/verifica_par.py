def eh_par(numero):
    return numero % 2 == 0

def eh_impar(numero):
    # Preencher
    # Use a função anterior
    pass

def test():
    assert eh_par(0)
    assert eh_par(2)
    assert eh_par(4)
    assert not eh_par(1)
    assert not eh_par(3)

    assert eh_impar(1)
    assert eh_impar(3)
    assert eh_impar(5)
    assert not eh_impar(0)
    assert not eh_impar(2)
