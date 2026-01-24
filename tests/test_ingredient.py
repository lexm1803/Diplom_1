import pytest
from ..ingredient import Ingredient
from ..ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestIngredient:
    @pytest.mark.parametrize(
        'ing_type, name, price', [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 150.5),
            (INGREDIENT_TYPE_FILLING, '', 0)
        ]
    )
    def test_initialization_and_getters_ingredients(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type()==ing_type, f'Значение не соответствует {ing_type}'
        assert ingredient.get_name()==name, f'Значение не соответствует {name}'
        assert ingredient.get_price()==price, f'Значение не соответствует {price}'