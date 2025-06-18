from datetime import date
import calendar

def parcelamento(valor, parcelas, dt_venda):
    resultado = []
    valor_base  = valor // parcelas
    resto = valor % parcelas

    for i in range(parcelas):

        valor_parcela = valor_base + (1 if i < resto else 0)

        if i == 0:
            data = dt_venda
        else:
            ano = dt_venda.year
            mes = dt_venda.month + i

            if mes > 12:
                mes -= 12
                ano += 1

            ultimo_dia = calendar.monthrange(ano, mes)[1]
            data = date(ano, mes, ultimo_dia)
        
        resultado.append([valor_parcela, data])

    return resultado

def test():
    assert parcelamento(100, 1, dt_venda) == [[100, dt_venda]]
    assert parcelamento(100, 2, dt_venda) == [
        [50, dt_venda],
        [50, date(2025, 2, 28)]
    ]
    assert parcelamento(100, 3, dt_venda) == [
        [33, dt_venda],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)]
    ]
    assert parcelamento(100, 4, dt_venda) == [
        [25, dt_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ]
    assert parcelamento(100, 6, dt_venda) == [
        [16, dt_venda],
        [16, date(2025, 2, 28)],
        [16, date(2025, 3, 31)],
        [16, date(2025, 4, 30)],
        [16, date(2025, 5, 31)],
        [20, date(2025, 6, 30)]
    ]
