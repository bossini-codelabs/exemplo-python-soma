from soma import soma


def test_inteiros():
    assert soma(2, 3) == 5


def test_negativos():
    assert soma(-4, 1) == -3


def test_decimais():
    assert abs(soma(0.1, 0.2) - 0.3) < 1e-9
