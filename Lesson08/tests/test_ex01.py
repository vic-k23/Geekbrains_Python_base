import pytest

from Lesson08.ex01 import Date


@pytest.mark.parametrize("dt, expected_result", [("28-02-2004", {"day": 28, "month": 2, "year": 2004}),
                                                 ("23-12-1982", {"day": 23, "month": 12, "year": 1982})])
def test_decompose(dt, expected_result):
    assert expected_result == Date.decompose(dt)


@pytest.mark.parametrize("dt, expected_result", [("-1-12-1982", ValueError)])
def test_decompose_error(dt, expected_result):
    with pytest.raises(expected_result):
        Date.decompose(dt)


@pytest.mark.parametrize("dt, expected_result", [("28-02-2004", True),
                                                 ("23-12-1982", True),
                                                 ("33-12-1982", False),
                                                 ("30-13-1982", False)])
def test_validate(dt, expected_result):
    assert expected_result == Date.validate(dt)


@pytest.mark.parametrize("dt, expected_result", [("-1-12-1982", ValueError),
                                                 ("33-12--3000", ValueError)])
def test_validate_error(dt, expected_result):
    with pytest.raises(expected_result):
        Date.validate(dt)
