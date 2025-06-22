from ..op_factorial import factorial


def test_factorial_none():
    assert factorial(None) is None


# Falha pq 'bool' é interpretado como subclasse de int
def test_factorial_bool():
    assert factorial(True) is None
    assert factorial(False) is None


def test_factorial_string():
    assert factorial("") is None
    assert factorial("abc") is None
    assert factorial("7") is None


def test_factorial_float():
    assert factorial(1.5) is None
    assert factorial(-1.5) is None


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positives():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24


def test_factorial_negatives():
    assert factorial(-10) is None
    assert factorial(-1) is None
