def meses_validos(mes):  
    if mes <= 0 or mes > 12:
        return "Mês inválido"
    else:
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
        return meses[mes - 1] 

def test(): 
    assert meses_validos(1) == "Janeiro"
    assert meses_validos(12) == "Dezembro"
    assert meses_validos(0) == "Mês inválido"
    assert meses_validos(13) == "Mês inválido"
    assert meses_validos(-5) == "Mês inválido"  

