class Student():
    #class attribute (same for every object, declared only once)
    college_name="ABCD university"
    
    def __init__(self,name,marks):
        #object attribute (different for every object)
        self.name=name
        self.marks=marks
        print("new student added to dataset.")

s1=Student("aayushi",98)
print(s1.name,s1.marks)

#accesing class attribute directly
print(Student.college_name)

#object attribute is given higher priority than class attribute, if declared with same value. 