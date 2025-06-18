import os
import re
import shutil 

def limpa_nome_pasta(nome: str) -> str:
    disciplina = nome.lower().strip()
    disciplina = disciplina.replace(" ", "_")
    acentos = {'ã':'a', 'á':'a', 'â':'a', 'à':'a', 'é':'e', 'ê':'e', 'í':'i', 'ó':'o', 'ô':'o', 'õ':'o', 'ú':'u', 'ç':'c'}
    for acento, sem_acento in acentos.items():
        disciplina = disciplina.replace(acento, sem_acento)
    return disciplina

def test_limpa_nome_pasta(): 
    assert limpa_nome_pasta('Ciência da Computação') == 'ciencia_da_computacao'
    assert limpa_nome_pasta('Administração') == 'administracao'

def cria_pasta_curso(nome_curso: str) -> None:
    pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print(f"A pasta '{pasta}' foi criada com sucesso.")
    else:
        print(f"A pasta '{pasta}' já existe.")

def test_cria_pasta_curso():
    nome_teste = "Teste"
    pasta_esperada = "teste"

    cria_pasta_curso(nome_teste)

    assert os.path.exists(pasta_esperada), "Falha: pasta não foi criada"

    try:
        os.rmdir(pasta_esperada)
    except:
        pass

def cria_alunos(alunos: list, nome_curso: str) -> None:
    pasta = limpa_nome_pasta(nome_curso)
    if not os.path.exists(pasta):
        os.mkdir(pasta)

    caminho_arquivo = os.path.join(pasta, "alunos.txt")
    with open(caminho_arquivo, 'w') as f:
        for aluno in alunos:
            f.write(f"{aluno}\n")

def test_cria_alunos():
    alunos_teste = ["Ana Silva", "João Santos", "Maria Oliveira"]
    curso_teste = "Ciência da Computação"

    cria_alunos(alunos_teste, curso_teste)

    pasta_esperada = "ciencia_da_computacao"
    assert os.path.exists(pasta_esperada), "Falha: pasta do curso não foi criada"

    arquivo_esperado = os.path.join(pasta_esperada, "alunos.txt")
    assert os.path.exists(arquivo_esperado), "Falha: arquivo de alunos não foi criado"

    try:
        os.remove(arquivo_esperado)
        shutil.rmtree(pasta_esperada)
    except:
        pass

def converte_alunos_em_lista(alunos_com_virgula: str) -> list:
    nomes_limpos = []

    if len(alunos_com_virgula) == 0:
        return nomes_limpos

    for nome in alunos_com_virgula.split(","):
        if nome.strip():
            nomes_limpos.append(nome.strip())
    return nomes_limpos

def test_converte_alunos_em_lista():
    assert converte_alunos_em_lista("Ana, João, Maria") == ["Ana", "João", "Maria"]
    assert converte_alunos_em_lista("  Ana ,João , Maria ") == ["Ana", "João", "Maria"]
    assert converte_alunos_em_lista("Ana,, João,,") == ["Ana", "João"]
    assert converte_alunos_em_lista("") == []
