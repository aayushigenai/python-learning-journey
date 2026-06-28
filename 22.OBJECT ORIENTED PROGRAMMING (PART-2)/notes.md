# Object-Oriented Programming in Python (Part-2)

## Topics Covered

* Changing Class Attributes
* Class Methods (`@classmethod`)
* Property Decorator (`@property`)
* `super()` Method
* Multiple Inheritance
* Polymorphism (Implicit Operator Overloading)
* Practice Question 1 – Circle Class
* Practice Question 2 – Employee & Engineer Inheritance
* Practice Question 3 – Operator Overloading (`__gt__`)

---

## 1. Changing Class Attributes

Class attributes belong to the class itself rather than individual objects. They can be modified using the class name inside a method.

### Program

```python
class Person:

    name = "anonymous"

    def changeName(self, name):
        Person.name = name

p1 = Person()

p1.changeName("aayushi bhatt")

print(p1.name)
print(Person.name)
```

### Output

```text
aayushi bhatt
aayushi bhatt
```

### Explanation

* `name` is a class attribute.
* `Person.name` changes the value for the entire class.
* Every object of the class now reflects the updated value.

---

## 2. Class Methods (`@classmethod`)

A class method is used to modify class attributes using `cls` instead of the class name.

### Program

```python
class Person:

    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

c1 = Person()

c1.changeName("aayushi bhatt")

print(c1.name)
print(Person.name)
```

### Output

```text
aayushi bhatt
aayushi bhatt
```

### Explanation

* `@classmethod` passes the class as the first argument (`cls`).
* It is the recommended way to modify class attributes.
* The updated value is shared by all objects of the class.

---

## 3. Property Decorator (`@property`)

The `@property` decorator allows a method to be accessed like an attribute.

### Program

```python
class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

s1 = Student(98, 99, 98)

print(s1.percentage)

s1.phy = 99

print(s1.percentage)
```

### Output

```text
98.33333333333333%
98.66666666666667%
```

### Explanation

* `percentage` behaves like an attribute instead of a method.
* The percentage is calculated dynamically.
* Whenever marks change, the percentage updates automatically.

---

## 4. `super()` Method

The `super()` function is used to call the constructor or methods of the parent class.

### Program

```python
class Car:

    def __init__(self, type):
        self.type = type

class ToyotaCar(Car):

    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

c1 = ToyotaCar("Fortuner", "electric")

print(c1.name)
print(c1.type)
```

### Output

```text
Fortuner
electric
```

### Explanation

* `super().__init__()` calls the constructor of the parent class.
* Parent attributes are initialized without rewriting the same code.
* This promotes code reuse.

---

## 5. Multiple Inheritance

Multiple inheritance allows a class to inherit properties from more than one parent class.

### Program

```python
class A:
    varA = "welcome to class A."

class B:
    varB = "welcome to class B."

class C(A, B):
    varC = "welcome to class C."

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
```

### Output

```text
welcome to class C.
welcome to class B.
welcome to class A.
```

### Explanation

* Class `C` inherits from both `A` and `B`.
* It can access attributes from both parent classes.

---

## 6. Polymorphism (Implicit Operator Overloading)

The same operator behaves differently depending on the data type.

### Program

```python
print(2 + 3)

print("aayushi" + "bhatt")

print([1,2,3,4,5] + [6,7,8,9,10])
```

### Output

```text
5
aayushibhatt
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Explanation

* `+` performs addition for integers.
* `+` concatenates strings.
* `+` combines lists.
* This is an example of polymorphism through operator overloading.

---

## 7. Practice Question 1

### Create a Circle class that calculates the area and perimeter.

### Program

```python
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)

print(c1.Area())
print(c1.perimeter())
```

### Output

```text
1386.0
132.0
```

### Explanation

* Area is calculated using πr².
* Perimeter is calculated using 2πr.

---

## 8. Practice Question 2

### Create an Employee class and an Engineer class using inheritance.

### Program

```python
class Employee:

    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role :", self.role)
        print("department :", self.department)
        print("salary :", self.salary)

class Engineer(Employee):

    def __init__(self, name, age):
        self.name = name
        self.age = age

        super().__init__("engineer", "Tech", "70,000")

e1 = Engineer("Rahul", 23)

e1.showDetails()
```

### Output

```text
role : engineer
department : Tech
salary : 70,000
```

### Explanation

* `Engineer` inherits from `Employee`.
* `super()` initializes the parent class attributes.
* The child class can directly use the parent's methods.

---

## 9. Practice Question 3

### Create an Order class and overload the `>` operator.

### Program

```python
class Order:

    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price

o1 = Order("chips", 60)
o2 = Order("kurkure", 50)

print(o1 > o2)
```

### Output

```text
True
```

### Explanation

* `__gt__()` overloads the greater-than (`>`) operator.
* Two objects are compared based on their prices.
* Since `60 > 50`, the comparison returns `True`.

---

# Key Learnings

* Class attributes belong to the class and are shared among all objects.
* `@classmethod` is the preferred way to modify class attributes.
* `@property` allows methods to behave like attributes.
* `super()` accesses constructors and methods of the parent class.
* Multiple inheritance allows one class to inherit from multiple parent classes.
* Polymorphism enables the same operator to perform different operations.
* Magic methods like `__gt__()` implement operator overloading.
* Inheritance improves code reusability and organization.
* OOP principles make programs modular, reusable, and easier to maintain.

---

# Files Created

* changingClassAttribute.py
* classMethod.py
* property.py
* super()Method.py
* MultipleInheritance.py
* polymorphismImplicitOverloading.py
* practiceQuestion1.py
* practiceQuestion2.py
* practiceQuestion3.py

---

# Date Learned

**28 June 2026**