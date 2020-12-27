import pytest

from Lesson08.ex02 import DivisionToZero, division


@pytest.mark.parametrize("dividend, divisor, expected_result", [(3.2, 15, 0.21333333333333335),
                                                                (8, 4, 2),
                                                                (33, 11, 3)])
def test_division(dividend, divisor, expected_result):
    assert division(dividend, divisor) == expected_result


@pytest.mark.parametrize("dividend, divisor, expected_result", [(3.2, 0, DivisionToZero)])
def test_division_error(dividend, divisor, expected_result):
    with pytest.raises(expected_result):
        division(dividend, divisor)
