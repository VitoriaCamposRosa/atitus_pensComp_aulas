def limpa_tela():
    import os

    os.system("cls" if os.name == "nt" else "clear")  # Limpa o console


def espera():
    import time

    time.sleep(0.5)  # Espera meio segundo (500ms)


def desenha_tela():
    altura = 6
    largura = 12


desenha_tela()
