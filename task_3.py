class Airplane:
    def __init__(self, model, max_passengers, current_passengers=0):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __add__(self, num_passengers):
        if self.current_passengers + num_passengers <= self.max_passengers:
            self.current_passengers += num_passengers
        else:
            print("Невозможно добавить больше пассажиров")
    
    def __sub__(self, num_passengers):
        if self.current_passengers - num_passengers >= 0:
            self.current_passengers -= num_passengers
        else:
            print("Невозможно убавить пассажиров")

    def __iadd__(self, num_passengers):
        self.__add__(num_passengers)
        return self

    def __isub__(self, num_passengers):
        self.__sub__(num_passengers)
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers


plane1 = Airplane("Boeing 747", 500)
plane2 = Airplane("Airbus A380", 600)

print(plane1 == plane2)  

plane1 += 200
print(plane1.current_passengers) 

plane1 -= 100
print(plane1.current_passengers)  

print(plane1 > plane2)  
print(plane1 < plane2)  
