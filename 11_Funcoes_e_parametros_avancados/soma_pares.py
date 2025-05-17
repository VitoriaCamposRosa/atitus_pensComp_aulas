def soma_pares(numeros: list, alvo: int) -> bool:
    vistos = set()
    for n in numeros:
        complemento = alvo - n
        if complement in vistos:
            return True
        vistos.add(n)
    return False

def test():
    assert not soma_pares([1, 2], 4)
    assert not soma_pares([8], 1)
    assert not soma_pares([8], 10)
    assert soma_pares([3, 4, 6], 9)
    assert soma_pares([3, 4, 6], 7)
