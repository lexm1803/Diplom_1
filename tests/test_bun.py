import pytest
from ..bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        'name, price', [
            ('black bun', 100.00),
            ('white bun', 200),
            ('red bun', 300.5),
            ('', 0)
        ]
    )
    def test_initialization_and_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name()==name, f'Значение не соответствует {name}'
        assert bun.get_price()==price, f'Значение не соответствует {price}'
