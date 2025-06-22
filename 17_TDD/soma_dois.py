def soma_dois(lista: list, alvo: int) -> list:
    if len(lista) < 2:
        return None 

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                return [i, j]
    return None

def test():
    assert soma_dois([2, 7, 11, 15], 9) == [0, 1]  # l[0]+l[1] == 9
    assert soma_dois([3, 2, 4], 6) == [1, 2]
    assert soma_dois([3, 3], 6) == [0, 1]
    assert soma_dois([], 6) is None
    assert soma_dois([1], 6) is None
    assert soma_dois([1, 2], 6) is None
