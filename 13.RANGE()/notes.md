# Range Function in Python

## Topics Covered

* range() Function
* Types of range()
* Using range() with for Loop
* Printing Even Numbers
* Practice Questions

---

## 1. range() Function

The `range()` function is used to generate a sequence of numbers.

### Syntax

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### Three Ways of Writing range()

```python
range(5)       # range(stop)
range(2,5)     # range(start, stop)
range(2,5,2)   # range(start, stop, step)
```

---

## 2. Using range() with for Loop

### Example

```python
for i in range(5):
    print(i)
```

### Output

```text
0
1
2
3
4
```

---

## 3. Printing Even Numbers from 1 to 100

### Example

```python
even = range(2,101,2)

for i in even:
    print(i)
```

### Output

```text
2
4
6
8
10
...
100
```

---

## 4. Practice Questions

### Question 1

Print numbers from 1 to 100 using `for` and `range()`.

### Solution

```python
seq = range(1,101)

for i in seq:
    print(i)
```

### Output

```text
1
2
3
...
100
```

---

### Question 2

Print numbers from 100 to 1 using `for` and `range()`.

### Solution

```python
seq = range(100,0,-1)

for i in seq:
    print(i)
```

### Output

```text
100
99
98
...
1
```

---

### Question 3

Print the multiplication table of a number using `range()`.

### Solution

```python
n = int(input("Enter the number :"))

seq = range(1,11,1)

for i in seq:
    print(n*i)
```

### Sample Output

```text
Enter the number : 5

5
10
15
20
25
30
35
40
45
50
```

---

## Key Learnings

* `range()` generates a sequence of numbers.
* `range(stop)` starts from 0 by default.
* `range(start, stop)` allows custom starting value.
* `range(start, stop, step)` allows custom increments.
* Negative step values can be used for reverse counting.
* `range()` is commonly used with `for` loops.

---

## Files Created

* range function.py
* practice question 1.py
* practice question 2.py
* practice question3.py

---

## Date Learned

23 June 2026

---