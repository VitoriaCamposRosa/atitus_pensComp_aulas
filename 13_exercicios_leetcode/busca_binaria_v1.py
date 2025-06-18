def busca_binaria(lista: list, valor: int) -> bool:
    for elemento in lista:
        if elemento == valor:
            return True
    return False

def test():
    assert busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 7) 
    assert not busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 8)
