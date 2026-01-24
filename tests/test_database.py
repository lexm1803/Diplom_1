from ..database import Database
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestDatabase:
    def test_available_buns_returns_correct_list(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns)==3, 'Число элементов не совпадает с ожидаемым'
        assert isinstance(buns[2], Bun), 'Элемент не соответствует объекту "bun"'
        assert buns[0].get_name() == "black bun", 'Название не совпадает с ожидаемым'
        assert buns[0].get_price() == 100, 'Цена не совпадает с ожидаемым'
        assert buns[1].get_name() == "white bun", 'Название не совпадает с ожидаемым'
        assert buns[1].get_price() == 200, 'Цена не совпадает с ожидаемым'
        assert buns[2].get_name() == "red bun", 'Название не совпадает с ожидаемым'
        assert buns[2].get_price() == 300, 'Цена не совпадает с ожидаемым'

    def test_available_ingredients_returns_correct_list(self):
        db = Database()
        ings = db.available_ingredients()
        assert len(ings)==6, 'Число ингредиентов не совпадает с ожидаемым'
        assert isinstance(ings[0], Ingredient), 'Элемент не соответствует объекту "ingredient"'
        assert isinstance(ings[3], Ingredient), 'Элемент не соответствует объекту "ingredient"'
        assert isinstance(ings[5], Ingredient), 'Элемент не соответствует объекту "ingredient"'
        assert ings[0].get_type() == INGREDIENT_TYPE_SAUCE, 'Элемент не соответствует ожидаемому типу (соус)'
        assert ings[0].get_name() == "hot sauce", 'Название соуса не соответствует ожидаемому'
        assert ings[0].get_price() == 100, 'Цена соуса не соответствует ожидаемой'
        assert ings[3].get_type() == INGREDIENT_TYPE_FILLING, 'Элемент не соответствует ожидаемому типу (начинка)'
        assert ings[3].get_name() == "cutlet", 'Название начинки не соответствует ожидаемому'
        assert ings[3].get_price() == 100, 'Цена начинки не соответствует ожидаемой'
        assert ings[5].get_type() == INGREDIENT_TYPE_FILLING, 'Элемент не соответствует ожидаемому типу (начинка)'
        assert ings[5].get_name() == "sausage", 'Название начинки не соответствует ожидаемому'
        assert ings[5].get_price() == 300, 'Цена начинки не соответствует ожидаемой'