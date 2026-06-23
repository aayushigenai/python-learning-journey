# Python Loops

## Introduction
Loops are used to execute a block of code repeatedly. Python provides two main types of loops:

1. `while` loop
2. `for` loop

Loops help reduce code repetition and make programs more efficient.

---

# While Loop

## Syntax

```python
while condition:
    # code block
```

The loop continues executing as long as the condition is `True`.

### Example

```python
count = 1

while(count <= 5):
    print(count)
    count += 1

print("loop ended")
```

### Output

```
1
2
3
4
5
loop ended
```

---

# For Loop

A `for` loop is used to iterate over sequences such as lists, tuples, strings, and sets.

## Example: Iterating Through a List

```python
num = [1, 2, 3, 4, 5, 6]

for el in num:
    print(el)
```

### Output

```
1
2
3
4
5
6
```

---

## Example: Iterating Through a String

```python
str = "aayushi"

for el in str:
    print(el)
```

### Output

```
a
a
y
u
s
h
i
```

---

# Break Statement

The `break` statement immediately terminates the loop when a specified condition is met.

## Example

```python
i = 1

while(i <= 5):
    print(i)

    if(i == 3):
        break

    i += 1
```

### Output

```
1
2
3
```

---

# Continue Statement

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

## Example

```python
i = 0

while(i <= 5):
    if(i == 3):
        i += 1
        continue

    print(i)
    i += 1
```

### Output

```
0
1
2
4
5
```

---

# Multiplication Table Using While Loop

## Program

```python
n = int(input("Enter a number: "))

i = 1

while(i <= 10):
    print(n * i)
    i += 1

print("loop ended")
```

### Example Output (n = 5)

```
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

# Practice Questions

## Question 1: Print Numbers from 1 to 100

```python
i = 1

while(i <= 100):
    print(i)
    i += 1

print("loop ended")
```

---

## Question 2: Print Numbers from 100 to 1

```python
i = 100

while(i >= 1):
    print(i)
    i -= 1

print("loop ended")
```

---

## Question 3: Print Elements of a List Using While Loop

List:

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Program

```python
lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0

while(i < len(lst)):
    print(lst[i])
    i += 1

print("loop ended")
```

---

## Question 4: Search a Number in a Tuple Using While Loop

Tuple:

```python
(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
```

### Program

```python
x = int(input("Enter the number to be searched: "))

t = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

i = 0

while(i < len(t)):
    if(x == t[i]):
        print(i)
        break

    i += 1

print("loop ended")
```

### Example

Input:

```
49
```

Output:

```
6
loop ended
```

---

## Question 5: Print Elements of a List Using For Loop

```python
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in num:
    print(el)
```

---

## Question 6: Search a Number in a Tuple Using For Loop

```python
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter the number: "))

index = 0

for el in tup:
    if(el == x):
        print("Found at index:", index)

    index += 1
```

---

# For Loop with Else

The `else` block executes when the loop completes normally without encountering a `break` statement.

## Example

```python
str = "Bhatt"

for ch in str:
    if(ch == "t"):
        print("t found")
        break

    print(ch)

else:
    print("END")
```

### Output

```
B
h
a
t found
```

---

# Key Points

- `while` loop executes until the condition becomes `False`.
- `for` loop is used to iterate over sequences.
- `break` exits the loop immediately.
- `continue` skips the current iteration.
- `else` executes only if the loop finishes without `break`.
- `len()` returns the number of elements in a sequence.

---