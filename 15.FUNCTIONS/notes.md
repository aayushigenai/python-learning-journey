# Functions in Python

## Topics Covered

* Function Declaration
* Function Parameters
* Return Statement
* Functions Without Return
* Built-in Functions
* User-Defined Functions
* Default Parameters
* Practice Questions

---

## 1. Function Declaration

A function is a block of reusable code that performs a specific task.

### Syntax

```python
def function_name(parameters):
    # code
```

### Example

```python
def calc_sum(x, y):
    sum = x + y
    return sum

sum1 = calc_sum(25, 25)

print(sum1)
```

### Output

```text
50
```

---

## 2. Function With Return Value

Functions can return values using the `return` keyword.

### Example

```python
def calc_sum(x, y):
    sum = x + y
    return sum

result = calc_sum(25, 25)

print(result)
```

### Output

```text
50
```

---

## 3. Function Without Return Value

If a function does not return anything, Python automatically returns `None`.

### Example

```python
def print_hello():
    print("hello")

print_hello()

output = print_hello()

print(output)
```

### Output

```text
hello
hello
None
```

---

## 4. Function to Calculate Average

### Example

```python
def Average_OfThreeNum(a, b, c):
    sum = a + b + c
    average = sum / 3
    return average

avg = Average_OfThreeNum(20, 20, 20)

print(avg)
```

### Output

```text
20.0
```

---

## 5. Built-in Functions

Built-in functions are functions already provided by Python.

### Examples

```python
print()
len()
range()
type()
```

### Example Program

```python
def calc_sum(x, y):
    sum = x + y
    return sum

sum1 = calc_sum(25, 25)

print(sum1)
```

### Output

```text
50
```

---

## 6. User-Defined Functions

Functions created by programmers are called user-defined functions.

### Example

```python
def calc_sum(x, y):
    sum = x + y
    return sum

sum1 = calc_sum(25, 25)

print(sum1)
```

### Output

```text
50
```

---

## 7. Default Parameters

Default parameters allow a function to use predefined values if arguments are not supplied.

### Example 1

```python
def prod_calc(a=4, b=4):
    product = a * b
    print(product)
    return product

prod_calc()
```

### Output

```text
16
```

### Example 2

```python
def cal_sum(a, b=4):
    sum = a + b
    print(sum)
    return sum

cal_sum(10)
```

### Output

```text
14
```

---

## 8. Practice Questions

### Question 1

Write a function to print the length of a list.

### Solution

```python
def cal_len(list):
    length = len(list)
    print(length)
    return length

cal_len(list=[2, 3, 4, 5, 6, 7, 8])
```

### Output

```text
7
```

---

### Question 2

Write a function to print all elements of a list in a single line.

### Solution

```python
def print_elements(list):
    for ele in list:
        print(ele, end=" ")
    return list

print_elements(list=[1,2,3,4,5,6,7,8,9,10])
```

### Output

```text
1 2 3 4 5 6 7 8 9 10
```

---

### Question 3

Write a function to find the factorial of a number.

### Solution

```python
def fact_function(n):
    fact = 1
    i = 1

    while(i <= n):
        fact *= i
        i += 1

    print(fact)
    return fact

fact_function(5)
```

### Output

```text
120
```

---

### Question 4

Write a function to convert USD to INR.

### Solution

```python
def USD_to_INR(x):
    inr_value = x * 83

    print(inr_value)
    return inr_value

USD_to_INR(73)
```

### Output

```text
6059
```

---

## Key Learnings

* Functions help avoid code repetition.
* Functions are declared using the `def` keyword.
* Parameters allow data to be passed into functions.
* `return` sends a value back to the caller.
* Functions without a return statement return `None`.
* Python provides many built-in functions like `print()`, `len()`, `range()`, and `type()`.
* User-defined functions are created by programmers.
* Default parameters provide fallback values when arguments are not passed.
* Functions can be used to solve practical problems such as finding factorials, list operations, and currency conversion.

---

## Files Created

* declarationFUNCTION.py
* averageOfThreeNumbers.py
* Built-in-Function.py
* User-Defined-Functions.py
* default_Parameter.py
* practiceQuestion.py
* practiceQuestion1.py
* practiceQuestion2.py
* practiceQuestion3.py
* practiceQuestion4.py

---

## Date Learned

24 June 2026