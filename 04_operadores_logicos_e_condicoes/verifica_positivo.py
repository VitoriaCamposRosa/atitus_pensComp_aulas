def eh_positivo(numero):
    pass


def eh_negativo(numero):
    pass

def test():
    assert eh_positivo(1)
    assert eh_positivo(2)
    assert eh_positivo(10)
    assert not eh_positivo(0)
    assert not eh_positivo(-1)
    assert not eh_positivo(-10)

    assert eh_negativo(-1)
    assert eh_negativo(-2)
    assert eh_negativo(-10)
    assert not eh_negativo(0)
    assert not eh_negativo(1)
    assert not eh_negativo(10)
