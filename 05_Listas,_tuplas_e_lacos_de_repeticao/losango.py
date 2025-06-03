def desenha_losango(altura):
    if altura < 3 or altura % 2 == 0:
        return "Por favor, digite um número ímpar maior ou igual a 3."

    linhas = []
    for i in range(altura // 2 + 1):
        espacos = " " * (altura // 2 - i)
        asteriscos = "*" * (2 * i + 1)
        linhas.append(espacos + asteriscos)

    for i in range(altura // 2 - 1, -1, -1):
        espacos = " " * (altura // 2 - i)
        asteriscos = "*" * (2 * i + 1)
        linhas.append(espacos + asteriscos)

    return "\n".join(linhas)

altura = int(input("Digite um valor ímpar para a altura do losango: "))
print(desenha_losango(altura))