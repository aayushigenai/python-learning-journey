# super() method example . how to inherit properties directly from the constructor of parent class.


class Car:

    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("car has started.")

    @staticmethod
    def stop():
        print("car has stopped.")

class ToyotaCar(Car):

    def __init__(self, name,type):
        self.name=name
        super().__init__(type)

c1=ToyotaCar("Fortuner","electric")        
print(c1.name)
print(c1.type)                

        