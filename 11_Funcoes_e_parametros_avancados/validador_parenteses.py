def validador_parenteses(entrada: str) -> bool:
    contador = 0
    for char in entrada:
        if char == '(':
            contador += 1
        elif char == ')':
            contador -= 1
            if contador < 0:
                return False
        else: 
            return False
    return contador == 0


def test():
    # Valores válidos
    assert validador_parenteses("()")
    assert validador_parenteses("()()")
    assert validador_parenteses("(())")
    assert validador_parenteses("(()()())")
    assert validador_parenteses("(((())()))")

    # Valores inválidos
    assert validador_parenteses(")")
    assert validador_parenteses("(")
    assert validador_parenteses("()(")
    assert validador_parenteses("()()())")
    assert validador_parenteses("(((())())")
