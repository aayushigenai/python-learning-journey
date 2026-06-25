# 🗑️ Deleting Files in Python

## Why Delete a File?

Sometimes a file is no longer needed after it has been processed. Python allows us to permanently remove files from the system using the `os` module.

---

# The `os` Module

The `os` module provides functions to interact with the operating system, including creating, renaming, and deleting files.

Before deleting a file, import the module:

```python
import os
```

---

# Deleting a File

Syntax:

```python
os.remove("filename")
```

Example:

```python
import os

os.remove("sample.txt")
```

Explanation:

- `os.remove()` deletes the specified file permanently.
- The file path can be relative or absolute.
- If the file does not exist, Python raises a `FileNotFoundError`.

---

# Using an Absolute Path

Example:

```python
import os

os.remove(r"C:\Users\Username\Desktop\Python\sample.txt")
```

Using a raw string (`r""`) avoids problems with backslashes in Windows file paths.

---

# Common Error

If the file doesn't exist:

```python
FileNotFoundError
```

To avoid this, check whether the file exists before deleting it.

Example:

```python
import os

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
```

---

# Practice Question 1 – Create a Text File

**Question**

Create a file named `sample.txt` and write the following content:

```
hi everyone
we are learning File I/O
using java
i like programming in java.
```

Solution:

```python
with open("sample.txt", "w") as f:
    f.write("hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using java\n")
    f.write("i like programming in java.")
```

---

# Practice Question 2 – Replace a Word

**Question**

Replace every occurrence of `"java"` with `"python"` in the file.

Solution:

```python
def replace_java():
    with open("sample.txt", "r") as f:
        data = f.read()

    new_data = data.replace("java", "python")

    with open("sample.txt", "w") as f:
        f.write(new_data)

replace_java()
```

Explanation:

- Read the file.
- Replace `"java"` with `"python"` using `replace()`.
- Write the updated text back to the file.

---

# Practice Question 3 – Search for a Word

**Question**

Check whether the word `"learning"` exists in the file.

Solution:

```python
def check_word():
    word = "learning"

    with open("sample.txt", "r") as f:
        data = f.read()

    if data.find(word) != -1:
        print("Word found")
    else:
        print("Word not found")

check_word()
```

Explanation:

- Read the file.
- `find()` returns:
  - Index of the word if found.
  - `-1` if not found.

---

# Practice Question 4 – Find the Line Number

**Question**

Print the line number where the word `"learning"` appears.

Solution:

```python
def check_for_line():
    word = "learning"
    line_no = 1

    with open("sample.txt", "r") as f:
        for line in f:
            if word in line:
                print(line_no)
                return
            line_no += 1

    print(-1)

check_for_line()
```

Explanation:

- Read one line at a time.
- Compare each line with the target word.
- Print the line number if found.
- Print `-1` if the word is absent.

---

# Practice Question 5 – Count Even Numbers

**Question**

A file contains numbers separated by commas.

Example:

```
1,2,76,84,90,101
```

Print the number of even integers.

Solution:

```python
count = 0

with open("practice.txt", "r") as f:
    data = f.read()

numbers = data.split(",")

for num in numbers:
    if int(num) % 2 == 0:
        count += 1

print(count)
```

Output:

```
4
```

Explanation:

- Read the file.
- Split the string using commas.
- Convert each value into an integer.
- Check whether it is even.
- Increase the counter for every even number.

---

# Summary

| Function | Purpose |
|----------|---------|
| `import os` | Imports operating system functions |
| `os.remove()` | Deletes a file |
| `replace()` | Replaces text in a string |
| `find()` | Searches for a substring |
| `split()` | Splits a string into a list |
| `int()` | Converts a string to an integer |

---

# Important Points to Remember

- Import the `os` module before deleting files.
- `os.remove()` permanently deletes a file.
- Always verify that a file exists before deleting it.
- `replace()` returns a new string; it does not modify the original one.
- `find()` returns `-1` when the word is absent.
- Reading files line by line is memory-efficient for large files.
- Use `split(",")` when processing comma-separated values.
- Convert strings to integers before performing arithmetic operations.
```