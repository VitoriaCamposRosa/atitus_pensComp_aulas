def dois_valores(x, y):   #Dois valores
    soma = x + y

    if soma % 2 == 0: 
        return x 
    else:
        return y

def test():  
    assert dois_valores(2, 4) == 2  
    assert dois_valores(3, 4) == 4  
    assert dois_valores(0, 0) == 0  
    assert dois_valores(-1, 2) == 2 
