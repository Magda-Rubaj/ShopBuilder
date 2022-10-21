import pytest


def test_categories_root_correct(root_category):
    assert root_category.level == 1
    assert root_category.parent == None


def test_lower_lvl_category_correct(lower_lvl_category):
    lower_lvl_category.set_level()
    assert lower_lvl_category.level == 2
    assert lower_lvl_category.parent is not None
