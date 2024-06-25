
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __repr__(self):
        return str(self.radius)

circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)  
print(circle1 < circle2)   
print(circle1 + 2)         
print(circle2 - 3) 