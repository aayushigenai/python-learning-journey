#example of inheritance

class Car:

    @staticmethod
    def start():
        print("car has started.")

    @staticmethod
    def stop():
        print("car has stopped.")

class ToyotaCar(Car):                 #class ToyotaCar inherites the property of class Car.

    def __init__(self,name):
        self.name=name

c1=ToyotaCar("fortuner")
print(c1.name)
c2=ToyotaCar("innova")
print(c1.start())     
print(c1.stop())   
