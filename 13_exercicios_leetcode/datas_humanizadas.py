MINUTO = 60
HORA = 60 * MINUTO


def data_humanizada(duracao: int) -> str:
    if duracao < MINUTO:
        return f"{duracao} segundos"
    elif duracao == MINUTO:
        return "1 minuto"
    elif duracao < HORA:
        minutos = duracao // MINUTO
        segundos = duracao % MINUTO
        if segundos == 0:
            return f"{minutos} minutos"
        else: 
            return f"{minutos} minutos {segundos} segundos"
    else:
        horas = duracao // HORA
        resto = duracao % HORA
        minutos = resto // MINUTO
        segundos = resto % MINUTO
        partes = []
        partes.append(f"{horas} {'hora' if horas == 1 else 'horas'}")
        if minutos > 0:
            partes.append(f"{minutos} {'minuto' if minutos == 1 else 'minutos'}")
        if segundos > 0:
            partes.append(f"{segundos} segundos")
        return " ".join(partes)

def test():
    assert data_humanizada(10) == "10 segundos"
    assert data_humanizada(1 * MINUTO) == "1 minuto"
    assert data_humanizada(2 * MINUTO) == "2 minutos"
    assert data_humanizada(2 * MINUTO + 20) == "2 minutos 20 segundos"
    assert data_humanizada(2 * HORA + 3 * MINUTO + 20) == "2 horas 3 minutos 20 segundos"
