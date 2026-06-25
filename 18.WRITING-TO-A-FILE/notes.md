# 📂 Writing to a File in Python

## What is File Handling?
File handling allows a Python program to create, read, write, update, and delete files stored on the computer.

To work with a file:
1. Open the file.
2. Perform the required operation.
3. Close the file.

---

# Opening a File

Syntax:

```python
file_object = open("filename", "mode")
```

Example:

```python
f = open("sample.txt", "w")
```

---

# File Modes

| Mode | Meaning | File Pointer Position | Creates File? | Deletes Existing Data? |
|------|---------|----------------------|---------------|-------------------------|
| `"r"` | Read only | Beginning | ❌ | ❌ |
| `"w"` | Write only | Beginning | ✅ | ✅ Yes |
| `"a"` | Append only | End | ✅ | ❌ |
| `"r+"` | Read + Write | Beginning | ❌ | ❌ |
| `"w+"` | Read + Write | Beginning | ✅ | ✅ Yes |
| `"a+"` | Read + Append | End | ✅ | ❌ |

---

# Writing to a File (`"w"` Mode)

`"w"` stands for **write mode**.

Characteristics:
- Opens the file for writing.
- If the file already exists, **all previous content is erased**.
- If the file does not exist, Python creates it automatically.
- The file pointer starts at the beginning.

Example:

```python
f = open("demo1.txt", "w")

f.write("I am learning Python.")

f.close()
```

Output inside file:

```
I am learning Python.
```

---

# Creating a New File

Python automatically creates a new file when:

- The file does not exist.
- It is opened using modes like `"w"`, `"w+"`, `"a"` or `"a+"`.

Example:

```python
f = open("sample.txt", "w")

f.close()
```

If `sample.txt` didn't exist before, it will now be created.

---

# Appending to a File (`"a"` Mode)

`"a"` stands for **append mode**.

Characteristics:
- Adds new content to the **end** of the file.
- Existing data remains unchanged.
- Creates the file if it does not exist.
- File pointer starts at the end.

Example:

```python
f = open("demo1.txt", "a")

f.write("\nPython is an amazing language.")

f.close()
```

If file initially contains:

```
I am learning Python.
```

After appending:

```
I am learning Python.
Python is an amazing language.
```

---

# Read and Write (`"r+"` Mode)

`"r+"` opens a file for both reading and writing.

Characteristics:
- File pointer starts at the beginning.
- Existing data is **not deleted**.
- Writing begins from the current pointer position.
- File must already exist.

Example:

```python
f = open("sample.txt", "r+")

f.write("abcd")

print(f.read())

f.close()
```

Suppose the original file contains:

```
tbhd is a good girl.
```

After writing:

```
abcd is a good girl.
```

Explanation:
- `"tbhd"` is overwritten by `"abcd"`.
- Remaining text stays unchanged.
- `read()` prints everything after the current file pointer.

---

# Read and Write (`"w+"` Mode)

`"w+"` allows both reading and writing.

Characteristics:
- Opens the file for reading and writing.
- Deletes all previous content immediately.
- Creates the file if it doesn't exist.
- File pointer starts at the beginning.

Example:

```python
f = open("sample2.txt", "w+")

f.write("Hello Python")

print(f.read())

f.close()
```

Output:

```
(empty)
```

Why?

After writing, the file pointer reaches the end of the file. Therefore `read()` has nothing left to read.

To read what was written:

```python
f.seek(0)

print(f.read())
```

Output:

```
Hello Python
```

---

# Append and Read (`"a+"` Mode)

`"a+"` opens a file for both appending and reading.

Characteristics:
- File pointer starts at the end.
- Existing data is preserved.
- New data is always appended.
- Creates file if it doesn't exist.

Example:

```python
f = open("sample3.txt", "a+")

print(f.read())

f.write("abcd")

f.close()
```

Output:

```
(empty)
```

Reason:

The pointer starts at the end of the file.

Since there is nothing after the end, `read()` prints nothing.

If you want to read the entire file:

```python
f.seek(0)

print(f.read())
```

---

# Closing a File

Always close a file after finishing your work.

Syntax:

```python
f.close()
```

Why close a file?
- Saves changes.
- Frees system resources.
- Prevents file corruption.
- Good programming practice.

---

# Summary

| Mode | Read | Write | Creates File | Deletes Old Data | Pointer Starts |
|------|------|--------|--------------|------------------|----------------|
| `"r"` | ✅ | ❌ | ❌ | ❌ | Beginning |
| `"w"` | ❌ | ✅ | ✅ | ✅ | Beginning |
| `"a"` | ❌ | ✅ (Append) | ✅ | ❌ | End |
| `"r+"` | ✅ | ✅ | ❌ | ❌ | Beginning |
| `"w+"` | ✅ | ✅ | ✅ | ✅ | Beginning |
| `"a+"` | ✅ | ✅ (Append) | ✅ | ❌ | End |

---

# Important Points to Remember

- `"w"` deletes all existing content before writing.
- `"a"` never deletes existing data; it always writes at the end.
- `"r+"` starts from the beginning without deleting data.
- `"w+"` deletes existing content and allows both reading and writing.
- `"a+"` appends new content and also allows reading.
- After writing, the file pointer moves to the end of the written data.
- Use `seek(0)` to move the pointer back to the beginning before reading.
- Always close files using `close()` after finishing.