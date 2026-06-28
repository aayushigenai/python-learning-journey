#example of using property decor.

class Student:

    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property                      #treats the function percentage as a property of class student.
    def percentage(self):
            return str((self.phy+self.chem+self.math)/3)+"%"
    

s1= Student(98,99,98)
print(s1.percentage)
s1.phy=99
print(s1.percentage)    
