# example of multiple inheritance.

class A:
    varA= "welcome to class A."

class B:
    varB=" welcome to class B."

class C(A,B) :                 # child class C inherited properties from parents B and A.
    varC="welcome to class C."

c1= C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
