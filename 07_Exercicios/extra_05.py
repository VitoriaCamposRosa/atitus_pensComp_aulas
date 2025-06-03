def status_aluno(notas): # Extra 05  
    notas_validas = [nota for nota in notas if nota is not None]

    if not notas_validas:
        return False

    media = sum(notas_validas) / len(notas_validas)

    return media >= 7
 
def test(): 
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])

    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])  
    assert not status_aluno([0, 0, 0, 0])  
