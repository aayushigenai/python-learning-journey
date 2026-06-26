# __init__function

class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("new student in database.")           # constructor got invoked as object was created.

s1= Student("aayushi")
print(s1.name)        


class Car:

    def __init__(self,color):                #self=s1(object)
        self.carColor=color
        print("new car color in database.")

s1=Car("blue")
print(s1.carColor)     


class Office:

    def __init__(self,manager):
        self.managername=manager
        print("manager name in the database")

s1=Office("Aayushi Bhatt")
print(s1.managername)               