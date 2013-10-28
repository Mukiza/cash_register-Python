from unittest import TestCase
from lib.item import Item
from hamcrest import assert_that, is_, is_not, instance_of, equal_to


class ItemsTest(TestCase):

    def test_is_instance(self):
        item = Item(name='apple', price=2000)
        assert_that(item, is_(instance_of(Item)))

    def test_is_not_instance(self):
        assert_that(False, is_not(instance_of(Item)))

    def test_is_equal(self):
        item = Item(name='apple', price=2000)
        item2 = Item(name='apple', price=2000)
        assert_that(item2, is_(equal_to(item)))

    def test_not_equal(self):
        apple = Item(name='apple', price=2000)
        mango = Item(name='Mango', price=4000)
        assert_that(apple, is_not(equal_to(mango)))
