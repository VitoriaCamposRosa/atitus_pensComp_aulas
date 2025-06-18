from datetime import date
import calendar

def parcelamento(valor, parcelas, dt_venda):
    resultado = []
    valor_parcela = valor // parcelas
    resto = valor % parcelas

    for i in range(parcelas):

        valor_final = valor_parcela + (resto if i == parcelas - 1 else 0)

        if i == 0:
            data_vencimento = dt_venda
        else:
            ano = dt_venda.year
            mes = dt_venda.month + i

            while mes > 12:
                mes -= 12
                ano += 1

                _, ultimo_dia = calendar.monthrange(ano, mes)
            data_vencimento = date(ano, mes, ultimo_dia)
        
        resultado.append([valor_final, data_vencimento])

    return resultado

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
