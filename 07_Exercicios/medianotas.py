def media_notas():
    nota1 = int(input("Digite a primeira nota: ")) #Medias
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print(f"Aluno aprovado com média {media:.2f}")
    else:
        print(f"Aluno reprovado com média {media:.2f}")