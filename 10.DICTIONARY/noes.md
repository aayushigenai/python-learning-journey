# Dictionary in Python

## Topics Covered

* Dictionary Declaration
* Accessing Values
* Updating Values
* Adding New Key-Value Pairs
* Nested Dictionaries
* Dictionary Methods

---

# 1. Dictionary Declaration

A dictionary stores data in the form of **key-value pairs**.

### Syntax

```python
dictionary_name = {
    "key1": value1,
    "key2": value2
}
```

### Example

```python
dic = {
    "name": "Aayushi",
    "age": 34,
    "course": "CSE",
    "isAdult": True
}

print(dic)
```

### Output

```text
{'name': 'Aayushi', 'age': 34, 'course': 'CSE', 'isAdult': True}
```

---

## Important Points

* Keys must be unique.
* Keys can be of immutable data types.
* Values can be of any data type.
* Dictionaries are mutable.
* Keys cannot be lists or dictionaries.
* Values can be lists, tuples, dictionaries, etc.

### Example

```python
info = {
    "name": "Aayushi",
    "subjects": ["os", "dbms", "programming", "coding"],
    "topics": ("python", "array", "linkedlist"),
    "age": 20
}
```

---

# 2. Accessing Dictionary Values

Values can be accessed using their keys.

### Syntax

```python
dictionary[key]
```

### Example

```python
print(dic["name"])
print(dic["age"])
print(dic["course"])
print(dic["isAdult"])
```

### Output

```text
Aayushi
34
CSE
True
```

---

# 3. Updating Existing Values

Dictionary values can be modified using keys.

### Example

```python
dic["name"] = "Ayushi"
```

The old value is overwritten.

---

# 4. Adding New Key-Value Pairs

New entries can be added easily.

### Example

```python
dic["surname"] = "Bhatt"
```

### Output

```python
{
 'name': 'Ayushi',
 'age': 34,
 'course': 'CSE',
 'isAdult': True,
 'surname': 'Bhatt'
}
```

---

# 5. Nested Dictionaries

A dictionary can contain another dictionary as a value.

### Example

```python
dic = {
    "name": "Aayushi",
    "surname": "Bhatt",
    "age": 20,

    "subjects": {
        "maths": 35,
        "chemistry": 55,
        "physics": 75,
        "computer science": 85
    },

    "isAdult": True
}
```

### Accessing Nested Dictionary

```python
print(dic["subjects"])
```

### Output

```text
{
 'maths': 35,
 'chemistry': 55,
 'physics': 75,
 'computer science': 85
}
```

---

# 6. Dictionary Methods

## keys()

Returns all keys present in the dictionary.

### Example

```python
print(dic.keys())
```

### Output

```text
dict_keys(['name', 'age', 'course', 'isAdult'])
```

---

## len()

Returns the number of key-value pairs.

### Example

```python
print(len(dic))
```

### Output

```text
4
```

---

## values()

Returns all values of the dictionary.

### Example

```python
print(dic.values())
```

### Output

```text
dict_values(['Aayushi', 34, 'CSE', True])
```

---

## items()

Returns key-value pairs as tuples.

### Example

```python
print(dic.items())
```

### Output

```text
dict_items([
('name', 'Aayushi'),
('age', 34),
('course', 'CSE'),
('isAdult', True)
])
```

---

## get()

Returns the value of a key.

### Example

```python
print(dic.get("name"))
```

### Output

```text
Aayushi
```

### Difference Between [] and get()

```python
dic["name2"]     # Error
dic.get("name2") # Returns None
```

Output:

```text
None
```

---

## update()

Adds or updates key-value pairs.

### Example

```python
dic.update({"city": "Jaipur"})
```

### Output

```python
{
 'name': 'Aayushi',
 'age': 34,
 'course': 'CSE',
 'isAdult': True,
 'city': 'Jaipur'
}
```

---

# Summary

### Dictionary Operations Learned

✅ Creating dictionaries

✅ Storing different data types

✅ Accessing values using keys

✅ Updating existing values

✅ Adding new key-value pairs

✅ Creating nested dictionaries

✅ Using dictionary methods:
- keys()
- values()
- items()
- get()
- update()

### Key Takeaways

* Dictionaries store data in key-value format.
* Keys must be unique.
* Dictionaries are mutable.
* Nested dictionaries help organize complex data.
* `get()` is safer than direct key access when a key may not exist.
* `update()` can add or modify entries.

---

## Files Practiced

* declaringAaDictionary.py
* accessing values.py
* nested dictionaries.py
* methods.py

---

## Date Learned

22 June 2026