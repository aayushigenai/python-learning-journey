# Tuples in Python

## Topics Covered

* Tuple Declaration
* Accessing Elements
* Tuple Slicing
* Tuple Methods
* Practice Questions

---

## 1. Tuple Declaration

A tuple is an ordered collection of elements that cannot be modified after creation.

### Syntax

```python
tuple_name = (value1, value2, value3)
```

### Example

```python
tup = (23, 43, 77, 34, 28)
```

### Practiced

```python
print(tup)
print(type(tup))
print(tup[2])
```

### Output

```text
(23, 43, 77, 34, 28)
<class 'tuple'>
77
```

### Empty Tuple

```python
tup1 = ()
```

### Tuple With One Element

```python
tup2 = (1,)
```

> A comma is mandatory for a single-element tuple.

---

## 2. Accessing Elements

Tuple elements are accessed using indexing.

### Syntax

```python
tuple_name[index]
```

### Example

```python
tup = (23, 43, 77, 34, 28)

print(tup[2])
```

Output:

```text
77
```

---

## 3. Tuple Slicing

Slicing is used to access multiple elements from a tuple.

### Syntax

```python
tuple_name[start:end]
```

### Example

```python
tuple = (23, 33, 12, 41, 23, 23, 83)

print(tuple[1:3])
```

### Output

```text
(33, 12)
```

---

## 4. Tuple Methods

Tuples provide limited built-in methods because they are immutable.

### index()

Returns the index of the first occurrence of an element.

```python
tuple.index(23)
```

Output:

```text
0
```

### count()

Returns the number of occurrences of an element.

```python
tuple.count(23)
```

Output:

```text
3
```

---

## 5. Practice Questions

### Question 1

Write a program to ask the user to enter the names of their favorite three movies and store them.

### Solution

```python
movies = []

mov1 = input("Enter first movie: ")
mov2 = input("Enter second movie: ")
mov3 = input("Enter third movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
```

### Sample Output

```text
['Enola Holmes 1', 'Enola Holmes 2', 'Enola Holmes 3']
```

---

### Question 2

Check whether a list is a palindrome or not.

### Solution

```python
list1 = [1, 2, 3, 2, 1]

list2 = list1.copy()
list2.reverse()

if list1 == list2:
    print("It is a palindrome")
else:
    print("Not a palindrome")
```

### Output

```text
It is a palindrome
```

---

### Question 3

Count the number of students with grade "A".

Given:

```python
["C", "D", "A", "A", "B", "B", "A"]
```

### Solution

```python
grades = ["C", "D", "A", "A", "B", "B", "A"]

count = grades.count("A")

print(count)
```

### Output

```text
3
```

---

### Question 4

Store the following grades and sort them from A to D.

Given:

```python
["C", "D", "A", "A", "B", "B", "A"]
```

### Solution

```python
grades = ["C", "D", "A", "A", "B", "B", "A"]

grades.sort()

print(grades)
```

### Output

```text
['A', 'A', 'A', 'B', 'B', 'C', 'D']
```

---

## Key Learnings

* Tuples are ordered collections.
* Tuples are immutable.
* Elements are accessed using indexing.
* Multiple elements can be accessed using slicing.
* Single-element tuples require a trailing comma.
* `index()` returns the first occurrence index.
* `count()` returns the number of occurrences.
* Lists provide more modification operations than tuples.

---

## Files Created

* declaration.py
* slicing in tuple.py
* Practicequestion1.py
* practiceQuestion2.py
* practiceQuestion3.py
* practiceQuestion4.py

---

## Date Learned

22 June 2026