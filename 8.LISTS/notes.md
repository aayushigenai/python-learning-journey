# Lists in Python

## Topics Covered

* List Declaration
* Accessing Elements
* List Slicing
* List Methods

---

## 1. List Declaration

A list is an ordered collection used to store multiple values in a single variable.

### Syntax

```python
list_name = [value1, value2, value3]
```

### Example

```python
marks = [23.5, 35.5, 75.5, 85.5, 45.5]
```

### Practiced

* Creating a list of marks
* Printing list elements
* Finding the type of a list using `type()`
* Finding the length of a list using `len()`
* Creating a list with multiple data types

Example:

```python
student = ["Aayushi", 35, "Delhi"]
```

---

## 2. Accessing Elements

List elements are accessed using their index position.

### Syntax

```python
list_name[index]
```

### Example

```python
student = ["Aayushi", 34, "Delhi"]

print(student[2])
```

Output:

```text
Delhi
```

### Practiced

* Accessing elements using positive indexing
* Retrieving specific values from a list

---

## 3. List Slicing

Slicing is used to access multiple elements from a list.

### Syntax

```python
list[start:end]
```

### Examples

```python
marks = [25.5, 35.5, 45.5, 55.5, 65.5]

print(marks[1:4])
print(marks[:4])
print(marks[1:len(marks)])
print(marks[-3:-1])
```

### Practiced

* Slicing with start and end index
* Slicing from beginning
* Slicing till end
* Negative index slicing

---

## 4. List Methods

List methods are built-in functions used to modify lists.

### append()

Adds an element at the end of the list.

```python
marks.append(75)
```

### sort()

Sorts the list in ascending order.

```python
list.sort()
```

### reverse()

Reverses the order of list elements.

```python
list.reverse()
```

### insert()

Inserts an element at a specific index.

```python
list.insert(1, 10)
```

### remove()

Removes the first occurrence of an element.

```python
list.remove("c")
```

### pop()

Removes an element from a specific index.

```python
list.pop(0)
```

### Important Note

Most list methods modify the original list and return `None`.

Example:

```python
print(marks.reverse())
```

Output:

```text
None
```

because the original list is modified directly.

### Practiced

* Appending elements
* Sorting lists
* Reversing lists
* Inserting elements
* Removing elements
* Popping elements using index

---

## Key Learnings

* Lists can store multiple values in a single variable.
* Lists are mutable (modifiable).
* Elements are accessed using indexing.
* Multiple elements can be accessed using slicing.
* Lists can contain different data types.
* Built-in methods help add, remove, sort, and modify elements.
* Most list methods modify the original list directly.

---

## Files Created

* declaration.py
* accessingElement.py
* slicing.py
* methods.py

---

## Date Learned

22 June 2026