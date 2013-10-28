class CashRegister(object):

    def __init__(self, printer):
        self.printer = printer

    def process(self, purchase):
        self.printer.print_(purchase.as_string())