def real_para_dolar(valor, tx_conversao): #Extra 03  
    return valor / tx_conversao

def test():
    assert real_para_dolar(500, 5.20) == 96.15384615384615
    assert real_para_dolar(500, 1) == 500
    assert real_para_dolar(500, 6) == 83.33333333333333   
 