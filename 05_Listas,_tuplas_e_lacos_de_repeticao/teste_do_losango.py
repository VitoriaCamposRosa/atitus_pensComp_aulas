from losango import desenha_losango  # Importa a função do arquivo original

def test_losango():
    esperado = (
        "  *\n"
        " ***\n"
        "*****\n"
        " ***\n"
        "  *"
    )
    assert desenha_losango(5) == esperado

def test_losango_valor_invalido():
    assert desenha_losango(2) == "Por favor, digite um número ímpar maior ou igual a 3."