class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)
