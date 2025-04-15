def tres_valores(x, y, z): 
    if (y * z) > x:
        return x
    elif (x + y) > z:
        return y
    elif (z - y) > x:
        return z
    else:
        return x + y + z

def test():
    assert tres_valores(1, 2, 3) == 1  
    assert tres_valores(10, 1, 5) == 1 
    assert tres_valores(2, 1, 5) == 5   
    assert tres_valores(1, 1, 1) == 3 
