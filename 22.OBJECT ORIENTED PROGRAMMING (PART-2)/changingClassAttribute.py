class Person:

    name="anonmyous"

    def changeName(self,name):
        Person.name=name

p1=Person()
p1.changeName("aayushi bhatt")
print(p1.name)
print(Person.name)       

