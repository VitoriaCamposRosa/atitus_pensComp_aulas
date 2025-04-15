def jogo_descobre_senha(senha_secreta, tentativas_usuario):
    tentativas = 0
    for tentativa in tentativas_usuario:
        if tentativa < 1 or tentativa > 10:
            continue
        tentativas += 1
        if tentativa == senha_secreta:
            return tentativas  
    return -1  

def test_jogo_descobre_senha():
    assert jogo_descobre_senha(6, [6]) == 1
    assert jogo_descobre_senha(6, [0, 11, 3, 6]) == 2  
    assert jogo_descobre_senha(6, [1, 2, 3, 4, 5]) == -1
    assert jogo_descobre_senha(6, [1, 2, 3, 4, 5, 6]) == 6