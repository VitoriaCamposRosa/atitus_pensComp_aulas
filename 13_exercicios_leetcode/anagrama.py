def sao_anagramas(palavra1: str, palavra2: str) -> bool:
    contador_palavra1 = {}
    contador_palavra2 = {}

    if len(palavra1) != len(palavra2):
        return False

    for letra1 in palavra1.lower(): 
        if letra1 in contador_palavra1:
            contador_palavra1[letra1] += 1
        else:
            contador_palavra1[letra1] = 1

    for letra2 in palavra2.lower():
        if letra2 in contador_palavra2:
            contador_palavra2[letra2] += 1
        else:
            contador_palavra2[letra2] = 1 

    if contador_palavra1 == contador_palavra2:
        return True

def test():
    assert sao_anagramas("amor", "roma")
    assert sao_anagramas("iracema", "america")
    assert sao_anagramas("estudo", "duetos")

    assert not sao_anagramas("banana", "anana")
    assert not sao_anagramas("banana", "")
    assert not sao_anagramas("banana", "abc")
