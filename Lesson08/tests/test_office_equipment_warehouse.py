import pytest

from Lesson08.ex04 import Stock, Printer, Scanner, Copier


@pytest.mark.parametrize("manufacturer, model, performance, interfaces, color, count, expected_result",
                         [("Kyocera", "Ecosys 2035dn", 10, ["USB", "Ethernet"], "white", 3, 3),
                          ("Hewlett Packard", "LaserJet P1000", 20, ["USB", "WiFi"], "black", 3, 3)])
def test_stock_count_equipment(manufacturer, model, performance, interfaces, color, count, expected_result):
    test_stock = Stock()
    test_copier = Copier(manufacturer, model, performance, interfaces, color)
    test_stock.push_equipment(test_copier, count)
    assert test_stock.count_equipment(Copier.stringify_me(manufacturer, model, performance, interfaces, color)) == expected_result


@pytest.mark.parametrize("manufacturer, model, performance, interfaces, color, count, expected_result",
                         [("Kyocera", "Ecosys 2035dn", 10, ["USB", "Ethernet"], "white", 3, {"Copier Kyocera/Ecosys 2035dn/10.0/['USB', 'Ethernet']/white": 3}),
                          ("Hewlett Packard", "LaserJet P1000", 20, ["USB", "WiFi"], "black", 3, {"Copier Hewlett Packard/LaserJet P1000/20.0/['USB', 'WiFi']/black": 3})])
def test_stock_count_equipment(manufacturer, model, performance, interfaces, color, count, expected_result):
    test_stock = Stock()
    test_copier = Copier(manufacturer, model, performance, interfaces, color)
    test_stock.push_equipment(test_copier, count)
    assert test_stock.equipment_list() == expected_result
