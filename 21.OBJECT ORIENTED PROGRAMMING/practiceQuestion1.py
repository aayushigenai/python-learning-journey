# create student class  that takes name and marks of 3 subjcets as arguments in 
# constructor . Then create  a method to print the average.

class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getAverage(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hey",self.name,"your average score of 3 subjects is :",sum/3)    



s1=Student("aayushi",[80,80,90])
s1.getAverage()

s1.name="sumit"
s1.getAverage()
