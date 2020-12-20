import pytest
from Lesson07.ex02 import Coat, Suit


@pytest.mark.parametrize("name, height, expected_result", [("suit model 1", 150, 300.3),
                                                          ("suit model 2", 160, 320.3),
                                                          ("suit model 3", 170, 340.3)])
def test_suit_fabric_consumption(name, height, expected_result):
    my_suit = Suit(name, height)
    assert expected_result == my_suit.fabric_consumption


@pytest.mark.parametrize("name, width, expected_result", [("coat model 1", 28, 5.115384615384615),
                                                          ("coat model 2", 46, 7.576923076923077),
                                                          ("coat model 3", 52, 8.5)])
def test_coat_fabric_consumption(name, width, expected_result):
    my_coat = Coat(name, width)
    assert expected_result == my_coat.fabric_consumption


@pytest.mark.parametrize("clothes_type, name, size, expected_exeption", [("Suit", "suit model 1", "38", TypeError),
                                                          ("Coat", "coat model 2", "52", TypeError)])
def test_clothes_exeptions(clothes_type, name, size, expected_exeption):
    with pytest.raises(expected_exeption):
        if clothes_type == "Suit":
            my_clothes = Suit(name, size)
        else:
            my_clothes = Coat(name, size)
        print(my_clothes.fabric_consumption)
