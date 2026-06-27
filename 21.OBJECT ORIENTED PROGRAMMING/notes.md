# Object-Oriented Programming (OOP) in Python

## Topics Covered

* Introduction to Object-Oriented Programming (OOP)
* Classes and Objects
* Constructors
* Default Constructor
* Parameterized Constructor
* Class Attributes
* Object Attributes
* Methods
* Static Methods
* Encapsulation
* Abstraction
* Practice Programs

---

## 1. What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **classes** and **objects**.

A **class** acts as a blueprint, while an **object** is an instance created from that blueprint.

Example:

* Class → Student
* Objects → Aayushi, Yushi

---

## 2. Class

A class is a blueprint for creating objects.

### Syntax

```python
class Student:
    name = "Aayushi"
```

### Example

```python
class Student:
    name = "Aayushi"

s1 = Student()

print(s1.name)
```

### Output

```text
Aayushi
```

---

## 3. Object

An object is an instance of a class that can access the class attributes and methods.

### Example

```python
class Car:
    color = "Blue"
    price = 700000

c1 = Car()

print(c1.color)
print(c1.price)
```

### Output

```text
Blue
700000
```

---

## 4. Constructor

A constructor is a special method that executes automatically whenever an object is created.

Python uses the `__init__()` method as a constructor.

### Example

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("A new student added to database.")

s1 = Student("Aayushi", 96)
```

### Output

```text
A new student added to database.
```

### Explanation

* Constructor runs automatically.
* It initializes object attributes.
* No need to call it manually.

---

## 5. Default Constructor

If no constructor is defined, Python automatically provides a default constructor.

### Example

```python
class Student:
    pass
```

or

```python
class Student:

    def __init__(self):
        pass
```

### Explanation

The default constructor initializes the object but performs no additional work.

---

## 6. Parameterized Constructor

A constructor that accepts parameters besides `self` is called a parameterized constructor.

### Example

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Aayushi", 98)
```

### Explanation

Values are supplied while creating the object, making every object unique.

---

## 7. Class Attributes

Class attributes belong to the class itself and are shared among all objects.

### Example

```python
class Student:

    college_name = "ABCD University"
```

Accessing the attribute:

```python
print(Student.college_name)
```

### Output

```text
ABCD University
```

---

## 8. Object Attributes

Object attributes belong to individual objects and are created using `self`.

### Example

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
```

Each object stores different values.

---

## 9. Priority of Attributes

If a class attribute and an object attribute have the same name, the object attribute gets higher priority.

### Example

```python
class Student:

    name = "Student"

    def __init__(self, name):
        self.name = name
```

`self.name` overrides `Student.name`.

---

## 10. Methods

Methods are functions defined inside a class.

### Example

```python
class Student:

    def hello(self):
        print("Hello", self.name)
```

Calling the method:

```python
s1.hello()
```

---

## 11. Returning Values from Methods

Methods can return values using the `return` statement.

### Example

```python
class Student:

    def get_marks(self):
        return self.marks
```

Calling the method:

```python
print(s1.get_marks())
```

### Output

```text
98
```

---

## 12. Static Methods

Static methods belong to the class rather than an object.

They are created using the `@staticmethod` decorator.

### Example

```python
class Student:

    @staticmethod
    def hello():
        print("Hello guys...")
```

Calling the method:

```python
Student.hello()
```

or

```python
s1.hello()
```

---

## 13. Encapsulation

Encapsulation is the process of binding data and methods together inside a single class.

### Example

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getAverage(self):
        total = sum(self.marks)
        print(total / 3)
```

### Explanation

The data (`name`, `marks`) and the method (`getAverage`) are packaged inside the same class.

---

## 14. Abstraction

Abstraction hides unnecessary implementation details and exposes only essential functionality.

### Example

```python
class Car:

    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")
```

Using the class:

```python
c1 = Car()
c1.start()
```

### Output

```text
Car Started
```

### Explanation

The user only calls `start()`, while the internal implementation remains hidden.

---

## 15. Practice Question 1

### Calculate the average marks of a student using a class.

### Concepts Used

* Constructor
* Object Attributes
* Methods
* Encapsulation

---

## 16. Practice Question 2

### Create a Bank Account class with debit and credit operations.

### Concepts Used

* Constructor
* Methods
* Object Attributes
* Encapsulation

Operations implemented:

* Debit
* Credit
* Get Balance

---

## Key Learnings

* OOP organizes code using classes and objects.
* Objects are instances of classes.
* Constructors initialize object data automatically.
* Default constructors are provided by Python if none are defined.
* Parameterized constructors initialize objects with custom values.
* Class attributes are shared across all objects.
* Object attributes are unique to each object.
* Object attributes have higher priority than class attributes when both have the same name.
* Methods define the behavior of objects.
* Static methods belong to the class and do not depend on object data.
* Encapsulation combines data and methods into a single unit.
* Abstraction hides implementation details while exposing only necessary functionality.

---

## Files Created

* creatingClasAndObj.py
* constructor.py
* exampleOfCreatingAConstructor.py
* defaultConstructor.py
* parameterizedConstructor.py
* classAttribute.py
* methods.py
* static methods.py
* encapsulation.py
* abstraction.py
* practiceQuestion1.py
* practiceQuestion2.py

---

## Date Learned

27 June 2026
