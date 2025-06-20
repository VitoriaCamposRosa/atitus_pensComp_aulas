IDADE_PARA_MAIORIDADE = 18


def verifica_maioridade(idade: int) -> bool:
    return idade >= IDADE_PARA_MAIORIDADE

def verifica_email(email: str) -> bool:
    if not email:
        return False

    if email.count('@') != 1:
        return False

    partes = email.split('@')
    nome, dominio = partes[0], partes[1]

    if not nome or not dominio:
        return False

    if '.' not in dominio:
        return False

    if email.startswith('.') or email.endswith('.'):
        return False

    caracteres_validos = (
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '0123456789'
        '._'
    )

    for char in email:
        if char not in caracteres_validos and char != '@':
            return False 

    return True

def solicita_nome() -> str | None:
    nome = entrada.strip()
    return solicita_nome(entrada)

def test_verifica_maioridade():
    assert not verifica_maioridade(-1)
    assert not verifica_maioridade(0)
    assert not verifica_maioridade(1)
    assert not verifica_maioridade(17)
    assert verifica_maioridade(18)
    assert verifica_maioridade(20)
    assert verifica_maioridade(100)

def test_verifica_email():
    assert not verifica_email('')
    assert not verifica_email('@')
    assert not verifica_email('@@')
    assert not verifica_email('abc@@abc.com')
    assert not verifica_email('abc@abc.edu')
    assert not verifica_email('a_b_c@a_b_c.com.com')
    assert not verifica_email('a_b_c@a_b_c.com.com.com')

    assert verifica_email('ABC@a_b_c.com')
    assert verifica_email('ABC@ABC.com')
    assert verifica_email('AbC@1BC.com')
    assert verifica_email('abc@abc.com')
    assert verifica_email('a23@123.com')
    assert verifica_email('a_b_c@a_b_c.com')

def test_solicita_nome():
    assert solicita_nome("João") == "João"
    assert solicita_nome("  Maria  ") == "Maria" 
    assert solicita_nome("") is None 
    assert solicita_nome("   ") is None
