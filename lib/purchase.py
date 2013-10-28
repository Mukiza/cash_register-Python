class Purchase(object):

    RECEIPT_HEADER = {'header': "Items\nNo.\t\tItem(s)\t\tQauntity\t\tCost\n"}

    def __init__(self, items):
        self.items = items
        self.duplicate_list = []

    def as_string(self):
        items_as_string = self.RECEIPT_HEADER['header']
        for item in self.items:
            if item.price:
                items_as_string += self.get_cost_for(item)
        items_as_string += "\tTotal: %d" % self.get_total()
        return items_as_string

    def __format(self, count, item):
        return "%s. %s %d\n" % (count, item.name, item.price)

    def exists_times(self, item):
        return self.items.count(item)

    def duplicate(self):
        return self.items.copy()

    def get_cost_for(self, item):
        times_exists = self.exists_times(item)
        item.price = int(item.price) * times_exists
        return self.__format(times_exists, item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += int(item.price)
        return total