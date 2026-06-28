# example of single inheritance

class Car:

    @staticmethod
    def start():
        print("car is starting")

    @staticmethod
    def stop():
        print("car has stooped.")

class ToyotaCar(Car):


    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):

    def __init__(self,type):
        self.type=type


c1=Fortuner("disel")
print(c1.type)        
print(c1.start())
print(c1.stop())
