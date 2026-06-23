# Pass Statement in Python

## Topics Covered

* pass Statement
* Using pass with Loops
* Practice Questions

---

## 1. pass Statement

The `pass` statement is a null statement in Python.

It does nothing when executed and is used as a placeholder for future code.

### Syntax

```python
pass
```

### Example

```python
for el in range(1,10):
    pass

print("work is done")
```

### Output

```text
work is done
```

### Explanation

```python
for el in range(1,10):
    pass
```

The loop runs from 1 to 9, but since `pass` does nothing, no action is performed inside the loop.

After the loop finishes, the next statement executes normally.

---

## 2. Practice Questions

### Question 1

Write a program to find the sum of the first n natural numbers using a `while` loop.

### Solution

```python
n = int(input("Enter the first n numbers :"))

i = 1
sum = 0

while(i <= n):
    sum += i
    i += 1

print(sum)
```

### Sample Output

```text
Enter the first n numbers : 5

15
```

### Explanation

```text
1 + 2 + 3 + 4 + 5 = 15
```

---

### Question 2

Write a program to find the factorial of a number.

### Solution

```python
n = int(input("Enter the number :"))

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
```

### Sample Output

```text
Enter the number : 4

24
```

### Explanation

```text
4! = 4 × 3 × 2 × 1
   = 24
```

---

## Key Learnings

* `pass` is a placeholder statement.
* `pass` allows writing empty loops, functions, classes, and conditions without errors.
* The program continues execution after a `pass` statement.
* A `while` loop can be used to calculate the sum of natural numbers.
* A `for` loop with `range()` can be used to calculate factorials.

---

## Files Created

* declaration.py
* practice question1.py
* practice question2.py

---

## Date Learned

23 June 2026

---