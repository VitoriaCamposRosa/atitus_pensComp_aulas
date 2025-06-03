import os
import time
import sys

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")

def espera():
    time.sleep(0.5)

def desenha_tela(altura, largura, x, y, colisoes):
    limpa_tela()
    for i in range(altura):
        for j in range(largura):
            if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
                print("#", end="")
            elif i == y and j == x:
                print("A", end="")
            else:
                print(".", end="")
        print()
    print(f"Colisões: {colisoes}")

def dvd_animation(max_colisoes=5):
    altura = 10
    largura = 20
    x = 1
    y = 1
    colisoes = 0
    direcao_x = 1
    direcao_y = 1

    while True:
        desenha_tela(altura, largura, x, y, colisoes)
        espera()

        x += direcao_x
        y += direcao_y

        if x == 0 or x == largura - 1:
            direcao_x *= -1
            colisoes += 1
        if y == 0 or y == altura - 1:
            direcao_y *= -1
            colisoes += 1

        if colisoes >= max_colisoes:
            print("Número máximo de colisões atingido. Encerrando...")
            sys.exit(0)  

def test_dvd_animation():
    try:
        dvd_animation(max_colisoes=1)  
    except SystemExit as e:
        assert e.code == 0
    else:
        assert False, "dvd_animation não terminou com sys.exit como esperado"