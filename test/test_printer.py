from lib.printer import Printer
from unittest import TestCase
from hamcrest import *


class PrinterTest(TestCase):

    def test_prints_receipt(self):
        printer = Printer()
        to_print = "Some Items"
        assert_that(printer.print_(to_print), is_(to_print))