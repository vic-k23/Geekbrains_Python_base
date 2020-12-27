import pytest

from Lesson08.ex07 import Complex


@pytest.mark.parametrize("a, b, c, d, expected_result", [(2, 3, 8, 7, Complex(10, 10)),
                                                         (4, -5, -3, 6, Complex(1, 1)),
                                                         (8, 8, 10, -8, Complex(18, 0))])
def test_complex_add(a, b, c, d, expected_result):
    n1 = Complex(a, b)
    n2 = Complex(c, d)
    assert n1 + n2 == expected_result


@pytest.mark.parametrize("a, b, c, d, expected_result", [(2, 3, 8, 7, Complex(-5, 38)),
                                                         (4, -5, -3, 6, Complex(18, 39)),
                                                         (8, 8, 10, -8, Complex(144, 16))])
def test_complex_mul(a, b, c, d, expected_result):
    n1 = Complex(a, b)
    n2 = Complex(c, d)
    assert n1 * n2 == expected_result
