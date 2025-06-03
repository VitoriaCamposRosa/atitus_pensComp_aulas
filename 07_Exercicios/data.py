def avalia_data(dia, mes, ano): 
    if dia <= 0 or dia > 31: 
        return "Dia inválido"
    elif mes <= 0 or mes > 12:
        return "Mês inválido"
    elif ano < 1000:
        return "Ano inválido"
    else:
        return "Todas as condições estão válidas" 

def test():   
    assert avalia_data(32, 1, 2020) == "Dia inválido" 
    assert avalia_data(10, 13, 2020) == "Mês inválido"
    assert avalia_data(10, 10, 999) == "Ano inválido"
    assert avalia_data(10, 10, 2020) == "Todas as condições estão válidas"



   

