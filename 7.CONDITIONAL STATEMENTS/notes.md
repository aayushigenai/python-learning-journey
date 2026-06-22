# Conditional Statements in Python

## Topics Covered

* if Statement
* if-else Statement
* if-elif-else Statement
* Nested if Statement
* Practice Questions

---

## Introduction

Conditional statements are used to make decisions in a program. They allow Python to execute different blocks of code based on whether a condition is `True` or `False`.

---

## 1. if Statement

The `if` statement executes a block of code only when the given condition is true.

### Example

```python
age = 18

if(age >= 18):
    print("CAN VOTE")
```

### Output

```text
CAN VOTE
```

### Key Learning

* The code inside the `if` block runs only when the condition is `True`.
* Indentation is mandatory in Python.

---

## 2. if-else Statement

The `else` block executes when the condition in the `if` statement is false.

### Example

```python
age = 18

if(age >= 18):
    print("CAN VOTE")
else:
    print("CAN NOT VOTE")
```

### Output

```text
CAN VOTE
```

### Key Learning

* `if` handles the true case.
* `else` handles the false case.

---

## 3. if-elif-else Statement

Used when multiple conditions need to be checked.

### Example

```python
light = "green"

if(light == "yellow"):
    print("wait")
elif(light == "green"):
    print("go")
elif(light == "red"):
    print("stop")
else:
    print("light is broken")

print("end of code")
```

### Output

```text
go
end of code
```

### Key Learning

* `elif` means "else if".
* Python checks conditions from top to bottom.
* Once a condition becomes true, remaining conditions are skipped.

---

## 4. Nested if Statement

An `if` statement inside another `if` statement is called a nested if statement.

### Example

```python
age = 34

if(age >= 18):
    if(age >= 80):
        print("can not drive.")
    else:
        print("can drive")
else:
    print("can not drive.")
```

### Output

```text
can drive
```

### Key Learning

* Nested conditions help solve complex decision-making problems.
* Inner `if` statements are executed only if the outer condition is true.

---

## 5. Example Program - Student Grade System

### Example

```python
marks = int(input("enter the marks of the student: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of student is:", grade)
```

### Sample Output

```text
enter the marks of the student: 85
grade of student is: B
```

### Key Learning

* Multiple conditions can be checked using `elif`.
* Logical operators such as `and` can combine conditions.

---

## Practice Questions

### Question 1

Write a program to check whether a number is even or odd.

```python
number = int(input("enter the number : "))

if(number % 2 == 0):
    print("even number")
else:
    print("odd number")
```

### Sample Output

```text
enter the number : 10
even number
```

---

### Question 2

Write a program to find the greatest of three numbers entered by the user.

```python
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))

if(num1 > num2 and num1 > num3):
    print("greatest number is:", num1)
elif(num2 > num3):
    print("greatest number is:", num2)
else:
    print("greatest number is:", num3)
```

### Sample Output

```text
enter the first number: 100
enter the second number: 500
enter the third number: 1000

greatest number is: 1000
```

---

### Question 3

Write a program to check whether a number is a multiple of 7 or not.

```python
num = int(input("enter the number :"))

if(num % 7 == 0):
    print("number is multiple of seven.")
else:
    print("number is not multiple of seven.")
```

### Sample Output

```text
enter the number : 49
number is multiple of seven.
```

---

## Key Learnings

* Conditional statements help programs make decisions.
* `if` executes code when a condition is true.
* `if-else` handles both true and false conditions.
* `if-elif-else` is useful for multiple conditions.
* Nested `if` statements allow complex decision-making.
* Logical operators (`and`, `or`, `not`) can be used in conditions.
* Indentation is very important in Python.

---

## Files Created

* if-elseStatemnet.py
* if-ilif-elseStatement.py
* nestingStatement.py
* exampleForConditionalStatemnet.py
* practiceQuestions1.py
* practiceQuestion2.py
* practiceQuestion3.py

---

## Date Learned

21 June 2026