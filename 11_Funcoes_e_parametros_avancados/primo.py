def eh_primo(numero: int) -> bool:  
    if numero <= 1:
        return False
    if numero % 2: 
        return True
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def test():
    assert not eh_primo(-1)
    assert not eh_primo(0)
    assert not eh_primo(1) 
    assert eh_primo(2)
    assert eh_primo(3)
    assert not eh_primo(4)
    assert eh_primo(5)

print("Pronto")
