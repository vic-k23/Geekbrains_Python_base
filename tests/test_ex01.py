from Lesson07.ex01 import Matrix
import pytest


@pytest.mark.parametrize("mtx1, mtx2, mtx_expected", [([1, 2, 3], [3, 2, 1], "[4, 4, 4]"),
                                                      ([[3, 5, 8], [2, 15, 12]],
                                                       [[7, 5, 2], [8, 15, 16]],
                                                       "[10, 10, 10]\n[10, 30, 28]\n"),
                                                      ([[23, -9], [13, 81], [0, -5]],
                                                       [[-13, 5], [17, -9], [200, 45]],
                                                       "[10, -4]\n[30, 72]\n[200, 40]\n")])
def test_matrix_addition(mtx1, mtx2, mtx_expected):
    m1 = Matrix(mtx1)
    m2 = Matrix(mtx2)
    assert mtx_expected == str(m1 + m2)


@pytest.mark.parametrize("mtx1, mtx2, expected_exeption", [([1, 2, 3], "[3, 2, 1]", TypeError),
                                                      ([[3, 5, 8], [2, 15, 12]],
                                                       [[7, 5], [8, 15, 16]],
                                                       ValueError),
                                                      ([[23, -9], [13, 81], [0, -5]],
                                                       [[-13, 5, 33], [0, 17, -9], [12, 200, 45]],
                                                       ValueError),
                                                           ([[3, 5, 8], [2, 15, 12]],
                                                            [[7, 5, "0"], [8, 15, 16]],
                                                            TypeError)])
def test_matrix_errors(mtx1, mtx2, expected_exeption):
    with pytest.raises(expected_exeption):
        m1 = Matrix(mtx1)
        m2 = Matrix(mtx2)
        m1 + m2
