def busca_binaria(lista: list, valor: int) -> bool:
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return True
        elif valor < lista[meio]:
            fim = meio - 1
        else: 
            inicio = meio + 1
    return False

def test():
    assert busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 7)
    assert not busca_binaria([1, 3, 5, 7, 9, 11, 13, 15], 8)
