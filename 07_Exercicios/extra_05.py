def status_aluno(notas):
    pass

def test():
    assert status_aluno([10, 10, 10, 10])
    assert status_aluno([10, None, 10, 10])

    assert not status_aluno([10, 5, None, 5])
    assert not status_aluno([5, 5, 5, 5])
    assert not status_aluno([0, 0, 0, 0])
