ANO_ATUAL = 2025 # Extra 0.0 

def saudacao(nome, sobrenome, ano_nascimento):
    if not (0 <= ano_nascimento < ANO_ATUAL):
        return None

    idade = (ANO_ATUAL - ano_nascimento) - 1
    return f"Olá, {nome} {sobrenome}. Bom dia! Você possui {idade} anos!"
 
def test():
    assert (
        saudacao("Matheus", "Jardim", 1991)
        == "Olá, Matheus Jardim. Bom dia! Você possui 33 anos!"
    )
    assert (
        saudacao("Thais", "Silva", 1990)
        == "Olá, Thais Silva. Bom dia! Você possui 34 anos!"
    )
    assert saudacao("Matheus", "Jardim", 0) is None
    assert saudacao("Matheus", "Jardim", 2050) is None
