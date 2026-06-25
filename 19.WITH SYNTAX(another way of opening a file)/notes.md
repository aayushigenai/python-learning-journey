# 📂 Using the `with` Statement for File Handling

## What is the `with` Statement?

The `with` statement provides a cleaner and safer way to work with files.

Instead of manually opening and closing a file, Python automatically closes the file once the block inside `with` finishes executing.

General syntax:

```python
with open("filename", "mode") as f:
    # perform file operations
```

---

# Why Use `with`?

Using `with` has several advantages:

- Automatically closes the file.
- Makes the code shorter and cleaner.
- Prevents forgetting to call `close()`.
- Reduces the chances of resource leaks.

Without `with`:

```python
f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()
```

With `with`:

```python
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
```

No need to call:

```python
f.close()
```

Python handles it automatically.

---

# Reading a File Using `with`

Example:

```python
with open("normalFile.txt", "r") as f:
    data = f.read()
    print(data)
```

Explanation:

- Opens the file in read mode.
- Reads the complete contents.
- Stores the data in a variable.
- Prints the data.
- Automatically closes the file after exiting the block.

---

# Writing to a File Using `with`

Example:

```python
with open("normalFile.txt", "w") as f:
    f.write("new data")
```

Explanation:

- Opens the file in write mode.
- If the file already exists, its previous contents are erased.
- Writes `"new data"` into the file.
- Automatically closes the file.

---

# How `with` Works

```python
with open("sample.txt", "r") as f:
    data = f.read()
```

When execution enters the `with` block:

- The file is opened.
- The variable `f` refers to the opened file.

When execution leaves the block:

- Python automatically closes the file, even if an error occurs inside the block.

---

# Advantages of Using `with`

- Cleaner syntax.
- No need to remember `close()`.
- Safer file handling.
- Automatically releases system resources.
- Recommended approach in Python.

---

# Summary

| Method | Need to Call `close()`? | Recommended |
|---------|------------------------|-------------|
| `open()` | ✅ Yes | ❌ Not preferred |
| `with open()` | ❌ No | ✅ Yes |

---

# Important Points to Remember

- `with` automatically closes the file after the block finishes.
- It works with any file mode (`"r"`, `"w"`, `"a"`, `"r+"`, `"w+"`, `"a+"`).
- It makes programs cleaner, shorter, and less error-prone.
- It is the preferred and most Pythonic way to perform file handling.
```