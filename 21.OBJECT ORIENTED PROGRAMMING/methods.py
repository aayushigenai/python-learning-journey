# methods are functions that belong to objects.

class Student():

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("a new student added to dataset")

    # declaring a method
    def hello(self):
        print("hello",self.name)

    def get_marks(self):
        return self.marks    

s1=Student("aayushi",98)
print(s1.name)      

#calling  a method
s1.hello()
print(s1.get_marks())