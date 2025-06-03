def numero_positivo_u_d_c(num): 
    if num < 0 or num > 999:
        return "Número inválido"

    unidade = num % 10 
    dezena = (num // 10) % 10
    centena = (num // 100) % 10

    resultado = { 
        "unidade": unidade
    }

    if dezena != 0 or centena != 0:
        resultado["dezena"] = dezena
    if centena != 0: 
        resultado["centena"] = centena 
 
    return resultado
 
def test():
    assert numero_positivo_u_d_c(5) == {"unidade": 5}
    assert numero_positivo_u_d_c(42) == {"unidade": 2, "dezena": 4}
    assert numero_positivo_u_d_c(123) == {"unidade": 3, "dezena": 2, "centena": 1}
    assert numero_positivo_u_d_c(0) == {"unidade": 0}
    assert numero_positivo_u_d_c(999) == {"unidade": 9, "dezena": 9, "centena": 9}
    assert numero_positivo_u_d_c(-1) == "Número inválido"
    assert numero_positivo_u_d_c(1000) == "Número inválido"

