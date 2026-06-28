# class methods 

class Person:
    name="anonymous"
    #decorator
    @classmethod              # class method used for changing the class atribute in normal method.
    def changeName(cls,name):
        cls.name=name

c1=Person       
c1.changeName("aayushi bhatt")
print(c1.name)
print(Person.name)             #orignal value of class name changed using @classmethod

