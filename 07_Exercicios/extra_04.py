def calcula_classe_social(salarios, salario_minimo):
    if not salarios:
        return None
    
    remuneracao_total = sum(salarios)

    salarios_minimos_per_capita = remuneracao_per_capita / salario_minimo

    if salarios_minimos_per_capita > 15:
        return "A"
    elif 5 <= salarios_minimos_per_capita <= 15:
        return "B"
    elif 3 <= salarios_minimos_per_capita < 5:
        return "C"
    elif 1 <= salarios_minimos_per_capita < 3:
        return "D"
    else:
        return "E"

def test():
    assert calcula_classe_social([], 1000) is None
    assert calcula_classe_social([1000], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([500], 1000) == "E"
    assert calcula_classe_social([1000, 0], 900) == "E"
    assert calcula_classe_social([1000], 900) == "D"
    assert calcula_classe_social([10000, 15000], 1000) == "B"
    assert calcula_classe_social([20000, 25000], 1000) == "A"
    assert calcula_classe_social([20000, 0, 0, 0, 0], 1000) == "C"
