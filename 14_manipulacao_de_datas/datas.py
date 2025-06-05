from datetime import date, timedelta
import calendar

# Crie método que recebe uma string (mm-dd-aaaa) e retorna uma data
def str_to_date(date_str):
    try:
        dd, mm, yyyy = date_str.split('-') 
        dd = int(dd)
        mm = int(dd)
        yyyy = int(yyyy)
        return date(year=yyyy, month=mm, day=dd)
    except (ValueError, TypeError):
        return None

def test_str_to_date():
    assert str_to_date('10-01-2025') == date(day=10, month=1, year=2025)
    assert str_to_date('10-99-2025') is None


# O nome do dia da semana (“sábado”, “domingo”, …)
def nome_dia_semana(data):
    dias_da_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    return dias_da_semana[data.weekday()] 

def test_nome_dia_semana():
    assert nome_dia_semana(date(year=2025, month=1, day=1)) == 'quarta-feira'
    assert nome_dia_semana(date(year=2025, month=1, day=2)) == 'quinta-feira'


# Quantos dias faltam para o final de semana
def dias_para_finde(data):
    hoje = data.weekday()
    if hoje <= 5:
        return 5 - hoje
    else:
        return 6

def test_dias_para_finde():
    assert dias_para_finde(date(year=2025, month=1, day=1)) == 3
    assert dias_para_finde(date(year=2025, month=1, day=2)) == 2


# Quantos dias existem entre a data e hoje
def delta_dias(data_a, data_b):
    diff = (data_b - data_a).days
    if abs(diff) == 1:
        return 0
    return diff

def test_delta_dias():
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2026, month=1, day=2)) == 366
    assert delta_dias(date(year=2026, month=1, day=1), date(year=2025, month=1, day=2)) == -365
    assert delta_dias(date(year=2025, month=1, day=1), date(year=2025, month=1, day=2)) == 0


# O mesmo dia no próximo mês (ou o anterior próximo)
def proximo_mes(data_a):
    year = data_a.year
    month = data_a.month + 1
    if month > 12:
        month = 1
        year += 1
    day = data_a.day
    ultimo_dia_mes = calendar.monthrange(year, month)[1]
    if day > ultimo_dia_mes:
        day = ultimo_dia_mes
    return date(year=year, month=month, day=day)

def test_proximo_mes():
    assert proximo_mes(date(year=2025, month=1, day=1)) == date(year=2025, month=2, day=1)
    assert proximo_mes(date(year=2025, month=1, day=29)) == date(year=2025, month=2, day=28)
    assert proximo_mes(date(year=2024, month=1, day=29)) == date(year=2024, month=2, day=29)
    assert proximo_mes(date(year=2025, month=1, day=30)) == date(year=2025, month=2, day=28)


# 1 se esta data está no futuro, -1 se no passado ou 0 se for hoje.
def data_futuro(data: date) -> str:
    hoje = date.today()
    if data > hoje:
        return 1
    elif data < hoje:
        return -1
    else:
        return 0

def test_data_futuro():
    assert data_futuro(date(day=1, month=1, year=2099)) == 1
    assert data_futuro(date(day=1, month=1, year=1999)) == -1
    assert data_futuro(date.today()) == 0
