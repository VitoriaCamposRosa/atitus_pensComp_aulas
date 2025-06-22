import pytest

IDADE_PARA_MAIORIDADE = 18
ANO_ATUAL = 2025

def verifica_maioridade(idade: int) -> bool:
    return idade >= IDADE_PARA_MAIORIDADE

def verifica_email(email: str) -> bool:
    if not email:
        return False

    if email.count('@') != 1:
        return False

    partes = email.split('@')
    if len(partes) != 2:
        return False

    nome, dominio = partes
    if not nome or not dominio:
        return False

    if not dominio.endswith('.com'):
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

def solicita_nome(nome: str) -> str | None:
    if not nome or not nome.strip():
        return None

    nome = nome.strip()
    partes = nome.split()

    if len(partes) < 2:
        return None

    return ' '.join(parte.capitalize() for parte in partes)

def cadastrar_responsavel(dados: dict, nome: str, ano_nascimento: str, email: str) -> bool:
    nome_valido = solicita_nome(nome)
    if nome_valido is None:
        return False

    try:
        idade = ANO_ATUAL - int(ano_nascimento)
    except ValueError:
        return False

    if not verifica_email(email):
        return False

    if not verifica_maioridade(idade):
        return False

    dados['responsavel'] = {
        'nome': nome_valido,
        'ano_nascimento': int(ano_nascimento),
        'email': email
    }
    return True

def cadastrar_contato_auxiliar(dados: dict, nome: str, ano_nascimento: str, email: str) -> bool:
    if not nome.strip():
        return True 
    
    nome_valido = solicita_nome(nome)
    if nome_valido is None:
        return False

    try:
        idade = ANO_ATUAL - int(ano_nascimento)
    except ValueError:
        return False

    if not verifica_email(email):
        return False

    if not verifica_maioridade(idade):
        return False

    dados['contato_auxiliar'] = {
        'nome': nome_valido,
        'ano_nascimento': int(ano_nascimento),
        'email': email
    }
    return True

def cadastrar_aluno(dados: dict, nome: str, ano_nascimento: str) -> bool:
    nome_valido = solicita_nome(nome)
    if nome_valido is None:
        return False

    try:
        idade = ANO_ATUAL - int(ano_nascimento)
    except ValueError:
        return False

    if verifica_maioridade(idade):
        return False

    dados['aluno'] = {
        'nome': nome_valido,
        'ano_nascimento': int(ano_nascimento)
    }
    return True

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
    assert solicita_nome('') is None
    assert solicita_nome('  ') is None
    assert solicita_nome('Nome') is None 
    assert solicita_nome('Nome Sobrenome') == 'Nome Sobrenome'
    assert solicita_nome('  nome  SOBRENOME  ') == 'Nome Sobrenome'
    assert solicita_nome('joão da silva') == 'João Da Silva'

def test_cadastrar_responsavel():
    dados = {}
    
    assert cadastrar_responsavel(dados, "Fulano de Tal", "1980", "fulano@email.com")
    assert dados['responsavel']['nome'] == "Fulano De Tal"
    assert dados['responsavel']['ano_nascimento'] == 1980
    assert dados['responsavel']['email'] == "fulano@email.com"
    
    dados = {}
    assert not cadastrar_responsavel(dados, "", "1980", "fulano@email.com")
    assert 'responsavel' not in dados
    
    dados = {}
    assert not cadastrar_responsavel(dados, "Fulano de Tal", "1980", "email-invalido")
    assert 'responsavel' not in dados

    dados = {}
    nascimento = ANO_ATUAL - 17 
    assert not cadastrar_responsavel(dados, "Fulano de Tal", str(nascimento), "fulano@email.com")
    assert 'responsavel' not in dados

def test_cadastrar_contato_auxiliar():
    dados = {}
    
    assert cadastrar_contato_auxiliar(dados, "", "", "")
    assert 'contato_auxiliar' not in dados
    
    assert cadastrar_contato_auxiliar(dados, "Beltrano Silva", "1975", "beltrano@email.com")
    assert dados['contato_auxiliar']['nome'] == "Beltrano Silva"
    assert dados['contato_auxiliar']['ano_nascimento'] == 1975
    assert dados['contato_auxiliar']['email'] == "beltrano@email.com"
    
    dados = {}
    assert not cadastrar_contato_auxiliar(dados, "Beltrano", "1975", "beltrano@email.com")
    assert 'contato_auxiliar' not in dados

def test_cadastrar_aluno():
    dados = {}
    
    assert cadastrar_aluno(dados, "Criança Silva", "2018")
    assert dados['aluno']['nome'] == "Criança Silva"
    assert dados['aluno']['ano_nascimento'] == 2018

    dados = {}
    nascimento = ANO_ATUAL - 18 
    assert not cadastrar_aluno(dados, "Adulto Silva", str(nascimento))
    assert 'aluno' not in dados

    dados = {}
    assert not cadastrar_aluno(dados, "", "2018")
    assert 'aluno' not in dados

