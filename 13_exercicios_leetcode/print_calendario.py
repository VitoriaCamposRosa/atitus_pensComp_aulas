def imprimir_calendario_mes(dia_inicial: int, total_dias: int):
    dias_da_semana = ["Do", "Se", "Te", "Qu", "Qu", "Se", "Sá"]
    cabecalho = "."join(dias_da_semana)

    dias = ["."] * dia_inicial
    dias += [str(dia) for dia in range(1, total_dias + 1)]

    calendario = [cabecalho]

    for in range(0, len(dias), 7):
        semana = dias[i:i+7]
        semana_formatada = [f"{dia:>2}".replace(" ", ".") for dia in semana]
        calendario.append(".".join(semana_formatada))
    
    return calendario

def test():
    assert imprimir_calendario_mes(0, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá",
        ".1..2..3..4..5..6..7",
        ".8..9.10.11.12.13.14",
        "15.16.17.18.19.20.21",
        "22.23.24.25.26.27.28",
        "29.30.31",
    ]

    assert imprimir_calendario_mes(1, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá"
        "....1..2..3..4..5..6"
        ".7..8..9.10.11.12.13"
        "14.15.16.17.18.19.20"
        "21.22.23.24.25.26.27"
        "28.29.30.31"
    ]

    assert imprimir_calendario_mes(2, 31) == [
        "Do.Se.Te.Qu.Qu.Se.Sá"
        ".......1..2..3..4..5"
        ".6..7..8..9.10.11.12"
        "13.14.15.16.17.18.19"
        "20.21.22.23.24.25.26"
        "27.28.29.30.31"
    ]
