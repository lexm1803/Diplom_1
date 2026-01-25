import pytest
from unittest.mock import MagicMock
from .burger import Burger


@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = 'mocked bun'
    bun.get_price.return_value = 50.0
    bun.get_name()
    bun.get_price()
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_price.return_value = 100.0
    ingredient.get_name.return_value = 'mocked cutlet'
    ingredient.get_type.return_value = 'FILLING'
    ingredient.get_price()
    ingredient.get_name()
    ingredient.get_type()
    return ingredient

@pytest.fixture
def burger():
    return Burger()