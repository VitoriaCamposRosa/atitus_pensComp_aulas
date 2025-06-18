def busca_simples(lista: list, valor: int) -> bool:
    for val in lista:
        if val == valor:
            return True
    return False


lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
valor = 7

print(busca_simples(lista_ordenada, valor)) 
