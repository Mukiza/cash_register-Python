from lib.purchase import Purchase
from lib.printer import Printer
from lib.cash_register import CashRegister
from unittest import TestCase
from mockito import mock, when, verify


class CashRegisterTest(TestCase):

    def test_prints_purchase(self):
        fake_printer = mock(Printer)
        fake_purchase = mock(Purchase)

        when(fake_purchase).as_string().thenReturn("Some purchase")

        cash_register = CashRegister(fake_printer)
        cash_register.process(fake_purchase)
        verify(fake_printer).print_("Some purchase")