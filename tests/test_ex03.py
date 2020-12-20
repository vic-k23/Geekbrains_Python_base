import pytest

from Lesson07.ex03 import Cell


@pytest.mark.parametrize("cell1, cell2, expected_result", [(3, 5, "********"),
                                                           (2, 2, "****"),
                                                           (8, 1, "*********")])
def test_add(cell1, cell2, expected_result):
    c1 = Cell(cell1)
    c2 = Cell(cell2)
    assert expected_result == str(c1 + c2)


@pytest.mark.parametrize("cell1, cell2, expected_result", [(3, 5, "**"),
                                                           (2, 3, "*"),
                                                           (8, 1, "*******")])
def test_sub(cell1, cell2, expected_result):
    c1 = Cell(cell1)
    c2 = Cell(cell2)
    assert expected_result == str(c1 - c2)


@pytest.mark.parametrize("cell1, cell2, expected_result", [(0, 5, ValueError),
                                                           (2, 2, ValueError),
                                                           (8, "1", TypeError)])
def test_sub_error(cell1, cell2, expected_result):
    with pytest.raises(expected_result):
        c1 = Cell(cell1)
        c2 = Cell(cell2)
        str(c1 - c2)


@pytest.mark.parametrize("cell1, cell2, expected_result", [(3, 5, "***************"),
                                                           (2, 2, "****"),
                                                           (8, 1, "********")])
def test_mul(cell1, cell2, expected_result):
    c1 = Cell(cell1)
    c2 = Cell(cell2)
    assert expected_result == str(c1 * c2)


@pytest.mark.parametrize("cell1, cell2, expected_result", [(33, 5, "******"),
                                                           (2, 2, "*"),
                                                           (8, 3, "**")])
def test_div(cell1, cell2, expected_result):
    c1 = Cell(cell1)
    c2 = Cell(cell2)
    assert expected_result == str(c1 / c2)


@pytest.mark.parametrize("cell1, cell2, expected_result", [(2, 3, ValueError),
                                                           (-1, 3, ValueError)])
def test_div_error(cell1, cell2, expected_result):
    with pytest.raises(expected_result):
        c1 = Cell(cell1)
        c2 = Cell(cell2)
        str(c1 / c2)


@pytest.mark.parametrize("cell, rl, expected_result", [(23, 5, "*****\n*****\n*****\n*****\n***"),
                                                       (4, 2, "**\n**"),
                                                       (3, 5, "***")])
def test_make_order(cell, rl, expected_result):
    c1 = Cell(cell)
    assert expected_result == c1.make_order(rl)
