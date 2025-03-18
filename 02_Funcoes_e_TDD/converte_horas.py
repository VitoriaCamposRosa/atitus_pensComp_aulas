def hora_para_minuto(valor):
    return valor * 60

def minuto_para_segundo(valor):
    return valor * 60


def hora_para_segundo(valor):
    return valor * 60 * 60


assert hora_para_minuto(0) == 0
assert hora_para_minuto(1) == 60
assert hora_para_minuto(2) == 120

assert minuto_para_segundo(0) == 0
assert minuto_para_segundo(1) == 60
assert minuto_para_segundo(2) == 120

assert hora_para_segundo(0) == 0
assert hora_para_segundo(1) == 3600  # 1 * 60 * 60
assert hora_para_segundo(2) == 7200  # 2 * 60 * 60

print("Terminou com sucesso!")
