import pytest
from unittest.mock import MagicMock
from ..burger import Burger
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestBurger:
    def test_set_buns_single_bun(self):
        bun = Bun('test bun', 10.0)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun
        
    def test_add_ingredient_append_to_list(self):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 100.0)
        burger = Burger()
        burger.add_ingredient(ing)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing

    def test_remove_ingredient_by_index(self):
        ing_1 = Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 100.0)
        ing_2 = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot souce', 50.0)
        burger = Burger()
        burger.add_ingredient(ing_1)
        burger.add_ingredient(ing_2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients)==1
        assert burger.ingredients[0] == ing_2

    def test_move_ingredient_change_order(self):
        burger = Burger()
        ings = [
            Ingredient(INGREDIENT_TYPE_FILLING, 'cutlet', 100.0),
            Ingredient(INGREDIENT_TYPE_SAUCE, 'hot souce', 50.0),
            Ingredient(INGREDIENT_TYPE_FILLING, 'dinosaur', 200.0),
        ]
        for ing in ings:
            burger.add_ingredient(ing)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [
            ings[1], 
            ings[2],
            ings[0],
        ]
    
    @pytest.mark.parametrize(
            'bun_price, ing_prices, expected_price',
            [
                (10, [], 20.0),
                (10, [20], 40),
                (0, [10, 20, 30], 60.0),
                (100.5, [10.5, 20.5], 232.0)
            ]
    )
    def test_get_price_burger(self, bun_price, ing_prices, expected_price):
        bun = Bun('test bun', bun_price)
        burger = Burger()
        burger.set_buns(bun)
        for price in ing_prices:
            burger.add_ingredient(Ingredient(
                INGREDIENT_TYPE_FILLING, 
                'test ingredient', 
                price
            ))
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        bun = Bun('black bun', 100)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        burger.add_ingredient(Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100))
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        assert lines[0] == '(==== black bun ====)'
        assert lines[1] == '= sauce hot sauce ='
        assert lines[2] == '= filling cutlet ='
        assert lines[3] == '(==== black bun ====)'
        assert lines[4] == ''
        assert lines[5] == 'Price: 400'

    def test_burger_mocked_database(self):
        mock_bun = MagicMock()
        mock_bun.get_name.return_value = 'mocked bun'
        mock_bun.get_price.return_value = 50.0
        
        mock_ingredient = MagicMock()
        mock_ingredient.get_price.return_value = 100.0
        mock_ingredient.get_name.return_value = 'mocked cutlet'
        mock_ingredient.get_type.return_value = 'FILLING'

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 200.0
        receipt = burger.get_receipt()
        assert '(==== mocked bun ====)' in receipt
        assert '= filling mocked cutlet =' in receipt
        mock_bun.get_name.assert_called()
        mock_bun.get_price.assert_called()
        mock_ingredient.get_price.assert_called()
        mock_ingredient.get_name.assert_called()
        mock_ingredient.get_type.assert_called()