print("Bem vindo ao Jogo Descobre Senha! Será que você consegue advinhar?")
print()

senha_secreta = 6
tentativas = 1

descobre_senha = int(input("Digite um número de 1 a 10 que você supõe que é a senha: "))
print()


if descobre_senha < 0 or descobre_senha > 10:
     print("É um número de 1 a 10. Digite um novo número")
     return None
else:
    print("Muito bem! Vamos verificar se está correto")
    print()

while descobre_senha != segredo: 
    print("Ah não, está incorreto.Tente novamente")
    print()
    tentativas += 1
    descobre_senha = int(input("Tente adivinhar a senha: "))
    print()

print("Parabéns! Você descobriu a senha.. O número de tentativas foram ", tentativas)

