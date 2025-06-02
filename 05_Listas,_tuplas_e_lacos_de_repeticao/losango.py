def desenha_losango(altura):
    if altura < 3 or altura % 2 == 0:
        print("Por favor, digite um número ímpar maior ou igual a 3.")
        return 

    for i in range(altura // 2 + 1):
        espacos = " " * (altura // 2 - i)  
        asteriscos = "*" * (2 * i + 1)     
        print(espacos + asteriscos)

    for i in range(altura // 2 - 1, -1, -1): 
        espacos = " " * (altura // 2 - i)
        asteriscos = "*" * (2 * i + 1)
        print(espacos + asteriscos)

altura = int(input("Digite um valor ímpar para a altura do losango: "))
desenha_losango(altura)
