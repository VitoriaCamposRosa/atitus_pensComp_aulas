from datetime import date
import calendar

def parcelamento(valor, parcelas, dt_venda):
    valor_base = valor // parcelas
    resto = valor % parcelas

    parcelas_lista = []
    for i in range(parcelas):
        year = dt_venda.year
        month = dt_venda.month + i
        while month > 12:
            month -= 12
            year += 1
        day = dt_venda.day
        ultimo_dia_mes = calendar.monthrange(year, month)[1]
        if day > ultimo_dia_mes:
            day = ultimo_dia_mes
        dt_parcela = date(year, month, day)

        if i == parcelas - 1:
            valor_parcela = valor_base + resto
        else:
            valor_parcela = valor_base

        parcelas_lista.append([valor_parcela, dt_parcela])

    return parcelas_lista

data_venda = date(2025, 1, 31)

def test():
    assert parcelamento(100, 1, data_venda) == [[100, data_venda]]
    assert parcelamento(100, 2, data_venda) == [
        [50, data_venda],
        [50, date(2025, 2, 28)]
    ]
    assert parcelamento(100, 3, data_venda) == [
        [33, data_venda],
        [33, date(2025, 2, 28)],
        [34, date(2025, 3, 31)]
    ]
    assert parcelamento(100, 4, data_venda) == [
        [25, data_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ]
    assert parcelamento(100, 6, data_venda) == [
        [16, data_venda],
        [16, date(2025, 2, 28)],
        [16, date(2025, 3, 31)],
        [16, date(2025, 4, 30)],
        [16, date(2025, 5, 31)],
        [20, date(2025, 6, 30)]
    ]
