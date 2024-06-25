class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

flat1 = Flat(50, 100000)
flat2 = Flat(50, 120000)

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 > flat2)
print(flat1 < flat2)
print(flat1 >= flat2)
print(flat1 <= flat2)