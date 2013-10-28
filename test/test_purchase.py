from lib.purchase import Purchase
from lib.item import Item
from unittest import TestCase
from hamcrest import assert_that, is_


class PurchaseTest(TestCase):

    def setUp(self):
        self.items = [
            Item(name='Soda', price=100),
            Item(name='Soda', price=100),
            Item(name='beer', price=500),
            Item(name='beer', price=500),
            Item(name='beer', price=500),
            Item(name='Rum', price=10500)
        ]
        self.purchase = Purchase(self.items)
        self.header = Purchase.RECEIPT_HEADER['header']

    def test_purchase(self):
        items = [
            Item(name='beer', price=500),
            Item(name='Rum', price=10500),
            Item(name='Whisky', price=90000)
        ]

        purchase_as_string = self.header + \
            "1. beer 500\n1. Rum 10500\n1. Whisky 90000\n\tTotal: 101000"
        purchase = Purchase(items)
        assert_that(purchase.as_string(), is_(purchase_as_string))

    def test_purchase_with_un_priced_item(self):
        items = [
            Item(name='beer', price=500),
            Item(name='Whisky', price=0),
            Item(name='Rum', price=10500)
        ]

        purchase_as_string = self.header + \
            "1. beer 500\n1. Rum 10500\n\tTotal: 11000"
        purchase = Purchase(items)
        assert_that(purchase.as_string(), is_(purchase_as_string))

    def test_purchase_with_identical_items(self):
        items = [
            Item(name='beer', price=500),
            Item(name='Soda', price=100),
            Item(name='Soda', price=100),
            Item(name='Rum', price=10500)
        ]

        purchase_as_string = self.header + "1. beer 500\n2. Soda 200\n3. Rum" \
            " 10500\n\tTotal: 11300"
        purchase = Purchase(items)
        assert_that(purchase.as_string(), is_(purchase_as_string))

    def test_purchase_returns_count_of_times_an_items_exists(self):
        soda = Item(name='Soda', price=100)
        items = [
            Item(name='Soda', price=100),
            soda,
            Item(name='beer', price=500),
            Item(name='Rum', price=10500)
        ]

        purchase = Purchase(items)
        assert_that(purchase.exists_times(soda), is_(2))

    def test_get_total_for_purchase(self):
        assert_that(self.purchase.get_total(), is_(12200))

    def test_duplicates_the_list_of_items(self):
        items = [
            Item(name='Soda', price=100),
            Item(name='beer', price=500),
            Item(name='Rum', price=10500)
        ]
        purchase = Purchase(items)
        copy_items = purchase.duplicate()
        assert_that(copy_items[0], is_(items[0]))
        assert_that(copy_items[1], is_(items[1]))
        assert_that(copy_items[2], is_(items[2]))
        assert_that(len(items), is_(len(purchase.duplicate())))

    def test_return_count_of_item_and_total_cost(self):
        item_1_reciept = '2. Soda 200\n'
        item_2_reciept = '1. Rum 10500\n'
        item_3_reciept = '3. beer 1500\n'
        assert_that(
            item_1_reciept, is_(self.purchase.get_cost_for(self.items[0])))
        assert_that(
            item_2_reciept, is_(self.purchase.get_cost_for(self.items[5])))
        assert_that(
            item_3_reciept, is_(self.purchase.get_cost_for(self.items[3])))
