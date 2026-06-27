# constructor that has parameters more than self are called as parameterized constructors.

class Student():

    def __init__(self,name,marks):      #parameterized constructor
        self.name=name
        self.marks=marks
        print("new student added to database.")

s1=Student("aayushi",98)
print(s1.name,s1.marks) 

s2=Student("yushi",88)
print(s1.name,s1.marks)