def descobre_senha_secreta():
    print("Bem vindo ao Jogo Descobre Senha! Será que você consegue advinhar?")
    print()

    senha_secreta = 6
    tentativas = 0

    while True:
        try:
            descobre_senha = int(input("Digite um número de 1 a 10 que você supõe que é a senha: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro de 1 a 10.")
            print()
            continue

        if descobre_senha < 1 or descobre_senha > 10:
            print("É um número de 1 a 10. Digite um novo número")
            print()
            continue

        tentativas += 1

        if descobre_senha == senha_secreta:
            if tentativas == 1:
                print("Parabéns! Você descobriu a senha na primeira tentativa.")
            else:
                print(f"Parabéns! Você descobriu a senha. O número de tentativas foi {tentativas}.")
            break
        else:
            print("Ah não, está incorreto. Tente novamente")
            print()

descobre_senha_secreta()