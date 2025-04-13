# print("Bem vindo ao Jogo Descobre Senha! Será que você consegue advinhar?")
# print()

# senha_secreta = 6
# tentativas = 0

# while True:
#     descobre_senha = int(input("Digite um número de 1 a 10 que você supõe que é a senha: "))
#     print()

#     if descobre_senha < 1 or descobre_senha > 10:
#         print("É um número de 1 a 10. Digite um novo número")
#     else:
#         tentativas += 1
#         if descobre_senha == senha_secreta:
#             print("Parabéns! Você descobriu a senha na primeira tentativa.")
#             break
#         else: 
#             print("Ah não, está incorreto.Tente novamente")
#             print()
#             while descobre_senha != senha_secreta: 
#                 tentativas += 1
#                 descobre_senha = int(input("Tente adivinhar a senha: "))
#                 print()
#             print("Parabéns! Você descobriu a senha.. O número de tentativas foram ", tentativas)
#             break