# Strings in Python

## Topics Covered

* Creating Strings
* String Operations
* String Indexing
* String Slicing
* Negative Indexing
* String Functions
* Practice Questions

---

## 1. Creating a String

A string is a sequence of characters enclosed in single (`' '`) or double (`" "`) quotes.

### Example

```python
str1 = "this is a string."
print(str1)
```

### Output

```text
this is a string.
```

### Key Learning

* Strings are used to store text data.
* Python treats text inside quotes as a string.

---

## 2. String Operations

### Concatenation

Combining two or more strings using the `+` operator.

```python
str1 = "hello"
str2 = "aayushi"

print(str1 + str2)
```

### Output

```text
helloaayushi
```

### Key Learning

* `+` joins strings together.
* This process is called concatenation.

---

## 3. Length of a String

The `len()` function returns the total number of characters in a string.

### Example

```python
str1 = "hello"
str2 = "aayushi"

print(len(str1 + str2))
```

### Output

```text
12
```

### Key Learning

* Spaces are also counted as characters.
* `len()` is commonly used to find string size.

---

## 4. String Indexing

Each character in a string has an index position.

### Example

```python
str4 = "YUSHI BHATT"

print(str4[0])
print(str4[1])
```

### Output

```text
Y
U
```

### Key Learning

* Indexing starts from `0`.
* First character is always at index `0`.

---

## 5. String Slicing

Used to extract a part of a string.

### Example

```python
str5 = "GAYATRI"

print(str5[1:4])
print(str5[:])
```

### Output

```text
AYA
GAYATRI
```

### Key Learning

* Starting index is included.
* Ending index is excluded.

---

## 6. Negative Indexing

Negative indexing starts from the end of the string.

### Example

```python
str = "AAPLE"

print(str[-3:-1])
```

### Output

```text
PL
```

### Key Learning

* `-1` represents the last character.
* Useful when working from the end of a string.

---

## 7. String Functions

Python provides built-in functions to work with strings.

### a) endswith()

Checks whether a string ends with a specified value.

```python
str = "i am studying python"

print(str.endswith("thon"))
print(str.endswith("am"))
```

### Output

```text
True
False
```

---

### b) capitalize()

Converts the first character into uppercase.

```python
str = "i am studying python"

print(str.capitalize())
```

### Output

```text
I am studying python
```

---

### c) replace()

Replaces one substring with another.

```python
str1 = "i am happy learning python"

print(str1.replace("python", "javascript"))
```

### Output

```text
i am happy learning javascript
```

---

### d) find()

Returns the index of the first occurrence of a substring.

```python
str = "i am studying python"

print(str.find("i"))
```

### Output

```text
0
```

### Key Learning

* Returns `-1` if the value is not found.

---

### e) count()

Returns how many times a character or word appears.

```python
str = "my name is $$$$$$$ and surname is $$$$"

print(str.count("$"))
```

### Output

```text
11
```

---

## Practice Questions

### Question 1

Write a program to input the user's first name and print its length.

```python
name = input("What is your first name: ")

print(len(name))
```

### Example Output

```text
Aayushi
7
```

---

### Question 2

Write a program to count the occurrence of `$` in a string.

```python
str = "my name is $$$$$$$ and surname is $$$$"

print(str.count("$"))
```

### Output

```text
11
```

---

## Key Learnings

* Strings store text data.
* Strings are immutable (cannot be changed directly).
* Indexing starts from `0`.
* Negative indexing starts from the end.
* Slicing helps extract parts of a string.
* `len()` returns string length.
* `endswith()`, `capitalize()`, `replace()`, `find()`, and `count()` are useful string functions.
* Concatenation joins multiple strings together.

---

## Files Created

* creatingAstring.py
* operationsInString.py
* NegativeIndexing(SPECIAL CASE).py
* stringFunction.py
* practiceQuestion.py

---

## Date Learned

21 June 2026