def numero_positivo_u_d_c(): 
    num = int(input("Digite um número positivo de até três digitos")) #cent, dez e uni
    print("O número escolhido foi: ", num)

    if num < 0 or num > 999:
        print("Número inválido")

    unidade = num % 10 
    dezena = (num / 10) % 10
    centena = (num / 100) % 10

    print("Unidade: ", unidade)
    if dezena != 0 or centena != 0:
        print("Dezena: ", dezena)
    if centena != 0:
        print("Centena: ", centena)

