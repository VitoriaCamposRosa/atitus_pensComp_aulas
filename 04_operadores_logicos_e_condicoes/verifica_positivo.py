def eh_positivo(numero): # Positivo
    if numero > 0: #Pode utilizar return numero > 0
        return True
    else:
        return False
   
def eh_negativo(numero):
    return not eh_positivo(numero)

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

print("Terminou com sucesso!")