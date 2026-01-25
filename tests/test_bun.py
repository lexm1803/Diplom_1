import pytest
from ..bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        'name, price', [
            ('black bun', 200),
            ('white bun', 200),
            ('red bun', 200),
            ('', 200)
        ]
    )
    def test_initialization_and_getters_by_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name()==name, f'Значение не соответствует {name}'

    @pytest.mark.parametrize(
        'name, price', [
            ('black bun', 100.00),
            ('black bun', 200),
            ('black bun', 300.5),
            ('black bun', 0)
        ]
    )
    def test_initialization_and_getters_by_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price()==price, f'Значение не соответствует {price}'
