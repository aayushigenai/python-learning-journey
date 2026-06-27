class Student:

    def __init__(self,name,marks):                            #constructor
        self.name=name
        self.marks=marks
        print("a new student added to database.")

s1=Student("aayushi",96)
print(s1.name,s1.marks)    

s2=Student("Yushi",88)
print(s2.name,s2.marks)
