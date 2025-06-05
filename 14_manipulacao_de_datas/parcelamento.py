from datetime import date


def parcelamento(valor, parcelas, dt_venda):
    valor_base = valor // parcelas
    resto = valor % parcelas

    parcelas_lista = []
    for i in range(parcelas):
        ano = data_venda.ano
        mes = data_venda.mes + i
        while mes > 12:
            mes -= 12
            ano += 1
        dia = dt_venda.dia
        ultimo_dia_mes = calendar.monthrange(ano, mes)[1]
        if dia > ultimo_dia_mes:
            dia = ultimo_dia_mes
        dt_parcela = date(ano, mes, dia)

        valor_parcela = valor_base
        if i == parcelas - 1:
            valor_parcela += resto
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
    assert parcelamento(100, 3, data_venda) == [
        [25, data_venda],
        [25, date(2025, 2, 28)],
        [25, date(2025, 3, 31)],
        [25, date(2025, 4, 30)]
    ]
    assert parcelamento(100, 6, data_venda) == [
        [16, data_venda],
        [16, date(2025, 2, 28)],
        [17, date(2025, 3, 31)],
        [17, date(2025, 4, 30)],
        [17, date(2025, 5, 31)],
        [17, date(2025, 6, 30)]
    ]
