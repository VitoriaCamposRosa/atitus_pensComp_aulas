def media_notas(nota1, nota2, nota3, nota4): 
    media = (nota1 + nota2 + nota3 + nota4) / 4 

    if media >= 7:
        return f"Aluno aprovado com média {media:.2f}"
    else:
        return f"Aluno reprovado com média {media:.2f}"

def test():
    assert media_notas(7, 7, 7, 7) == "Aluno aprovado com média 7.00"
    assert media_notas(6, 7, 8, 7) == "Aluno aprovado com média 7.00" 
    assert media_notas(5, 6, 6, 6) == "Aluno reprovado com média 5.75"
    assert media_notas(0, 0, 0, 0) == "Aluno reprovado com média 0.00" 