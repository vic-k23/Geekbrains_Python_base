import pytest

from Lesson08.ex03 import DigitValidatorError, DigitValidator


@pytest.mark.parametrize("lst, expected_result", [([1, 2, 3, 4, 5], True),
                                                  ([23, 23, 23, 23], True)])
def test_validate_list(lst, expected_result):
    assert DigitValidator.validate_list(lst) == expected_result


@pytest.mark.parametrize("lst, expected_result", [([1, 2, "3", 4, 5], DigitValidatorError),
                                                  (13, TypeError),
                                                  ([1, 2, False, 4, 5], DigitValidatorError),
                                                  ([1, 2, "asd", 4, 5], DigitValidatorError)])
def test_validate_list_raises_ex(lst, expected_result):
    with pytest.raises(expected_result):
        assert DigitValidator.validate_list(lst)


@pytest.mark.parametrize("element, expected_result", [(23, 23),
                                                        ([23, 23, 23, 23], False),
                                                        ("A", False),
                                                        ("23", 23),
                                                        (13.4, 13.4),
                                                      ("18.5", 18.5),
                                                      (-1, -1),
                                                      ("-1", -1),
                                                      ("18.5.456,45.fgv", 18.5),
                                                      ("192.168.0.1", 192.168)])
def test_validate_digit(element, expected_result):
    assert DigitValidator.validate_digit(element) == expected_result
