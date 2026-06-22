# Sets in Python

## Topics Covered

* Set Declaration
* Properties of Sets
* Empty Set Creation
* Set Methods
* Union of Sets
* Intersection of Sets
* Practice Questions

---

# 1. Set Declaration

A set is an unordered collection of unique elements.

### Syntax

```python
set_name = {value1, value2, value3}
```

### Example

```python
collection = {1, 2, 3, 4, 1, 4, 4, "Aayushi", "Bhatt", 5, 6}

print(collection)
print(type(collection))
```

### Output

```text
{1, 2, 3, 4, 'Bhatt', 5, 6, 'Aayushi'}
<class 'set'>
```

### Observation

Duplicate values are automatically removed.

---

# 2. Empty Set

### Incorrect

```python
empty = {}
```

This creates a dictionary, not a set.

### Correct

```python
empty = set()
```

---

# Properties of Sets

### Sets are:

✅ Unordered

✅ Mutable

✅ Contain unique elements

✅ Can store different data types

### Sets do NOT allow:

❌ Duplicate values

❌ Indexing

❌ Slicing

---

# 3. Set Methods

Assume:

```python
collection = {1, 2, 3, "Aayushi", "bhatt", 5}
```

---

## add()

Adds an element to the set.

### Example

```python
collection.add(10)
```

---

## remove()

Removes a specific element.

### Example

```python
collection.remove(5)
```

### Note

Raises an error if the element does not exist.

---

## clear()

Removes all elements from the set.

### Example

```python
collection.clear()
```

### Output

```python
set()
```

---

## pop()

Removes and returns a random element.

### Example

```python
print(collection.pop())
```

### Note

Since sets are unordered, any element may be removed.

---

# 4. Union of Sets

Union combines all unique elements from both sets.

### Example

```python
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))
```

### Output

```text
{1, 2, 3, 4, 5, 6, 7, 8}
```

---

# 5. Intersection of Sets

Intersection returns common elements.

### Example

```python
print(set1.intersection(set2))
```

### Output

```text
{4, 5, 6}
```

---

# Practice Question 1

## Store Word Meanings

### Problem

Store the following word meanings in a dictionary:

* table → a piece of furniture
* table → list of facts & figures
* cat → a small animal

### Solution

```python
dictionary = {
    "table": [
        "a piece of furniture",
        "list of facts & figures"
    ],
    "cat": "a small animal"
}

print(dictionary)
```

### Output

```text
{
 'table': ['a piece of furniture',
           'list of facts & figures'],
 'cat': 'a small animal'
}
```

---

# Practice Question 2

## Classroom Count

### Problem

One classroom is required for one subject.

Find the number of classrooms needed from:

```python
[
 "python", "java", "C++",
 "python", "javascript",
 "java", "python",
 "java", "C++", "C"
]
```

### Solution

```python
subjects = {
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "java",
    "C++",
    "C"
}

print(len(subjects))
```

### Output

```text
5
```

### Explanation

Unique subjects are:

```text
python
java
C++
javascript
C
```

Total classrooms required = 5

---

# Practice Question 3

## Store Subject Marks

### Problem

Take marks of three subjects from the user and store them in a dictionary.

### Solution

```python
subj1 = int(input("Enter marks of subject 1: "))
subj2 = int(input("Enter marks of subject 2: "))
subj3 = int(input("Enter marks of subject 3: "))

subjects = {}

subjects["subject1"] = subj1
subjects["subject2"] = subj2
subjects["subject3"] = subj3

print(subjects)
```

### Sample Output

```text
Enter marks of subject 1: 35
Enter marks of subject 2: 45
Enter marks of subject 3: 55

{'subject1': 35, 'subject2': 45, 'subject3': 55}
```

---

# Practice Question 4

## Store 9 and 9.0 Separately

### Problem

Store 9 and 9.0 as separate values in a set.

### Solution

```python
my_set = {9, "9.0"}

print(my_set)
```

### Output

```text
{'9.0', 9}
```

### Explanation

Normally:

```python
{9, 9.0}
```

produces

```text
{9}
```

because Python treats 9 and 9.0 as equal.

Using a string keeps them separate.

---

# Summary

## Set Concepts Learned

✅ Creating sets

✅ Empty sets

✅ Unique element storage

✅ Removing duplicates

✅ add()

✅ remove()

✅ clear()

✅ pop()

✅ union()

✅ intersection()

---

## Practice Problems Solved

✅ Word meanings dictionary

✅ Classroom count using sets

✅ Store subject marks in dictionary

✅ Store 9 and 9.0 separately

---

## Key Takeaways

* Sets automatically remove duplicates.
* Sets are unordered collections.
* Sets do not support indexing or slicing.
* Union combines unique values.
* Intersection returns common values.
* `len(set)` gives the number of unique elements.
* `pop()` removes a random element.
* Use `set()` to create an empty set.

---

## Files Practiced

* declaring a set.py
* methods in set.py
* practiceQuestion1.py
* practiceQuestion2.py
* practiceQuestion3.py
* practiceQuestion4.py

---

## Date Learned

22 June 2026