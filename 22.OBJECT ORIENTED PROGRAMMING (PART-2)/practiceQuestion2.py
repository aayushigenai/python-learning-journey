#define an employee class with attributes role, department and salary.
# This class also has a showDetails() method.
#create an engineer class that inherits properties from Employe and has additional 
# attributes: name and age.

class employee:

    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print("role :",self.role)
        print("department :",self.department)
        print("salary :",self.salary)
        

class Engineer(employee):

    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","Tech","70,000")


e1 = Engineer("Rahul","23")
e1.showDetails()            
