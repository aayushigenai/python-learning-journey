#used to delte obejcts and object properties as well.

class Student:

    def __init__(self,name):
        self.name=name


s1=Student("aayushi")
print(s1.name)
del s1            #statement for deleting object.
print(s1)        # error as already object as been delted.