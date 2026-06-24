# Recursion in Python

## Topics Covered

* Introduction to Recursion
* Recursive Function
* Base Case
* Recursive Call
* Recurrence Relationship
* Recursive Factorial
* Recursive Sum of Natural Numbers
* Recursively Printing List Elements

---

## 1. What is Recursion?

Recursion is a programming technique in which a function calls itself to solve a problem.

Every recursive function must have:

1. **Base Case** – The condition that stops recursion.
2. **Recursive Call** – The function calling itself with a modified argument.

Without a base case, recursion continues forever and causes a stack overflow error.

---

## 2. Recursive Function Example

### Program

```python
def show(n):

    if(n == 0):      # base case
        return

    print(n)
    show(n - 1)

show(5)
```

### Output

```text
5
4
3
2
1
```

### Explanation

* Function starts with `n = 5`
* Prints the current value.
* Calls itself with `n - 1`
* Continues until `n` becomes `0`
* Base case stops the recursion.

---

## 3. Base Case

A base case is the condition where recursion stops and returns control back to previous function calls.

### Example

```python
if(n == 0):
    return
```

Without this condition, the function would keep calling itself indefinitely.

---

## 4. Recursive Factorial Program

### Formula

Factorial of a number:

```text
n! = n × (n-1) × (n-2) × ... × 1
```

Example:

```text
4! = 4 × 3 × 2 × 1 = 24
```

### Program

```python
def fact(n):

    if(n == 0 or n == 1):    # base case
        return 1

    return n * fact(n - 1)   # recursive call

print(fact(4))
```

### Output

```text
24
```

### Explanation

```text
fact(4)
= 4 × fact(3)
= 4 × 3 × fact(2)
= 4 × 3 × 2 × fact(1)
= 4 × 3 × 2 × 1
= 24
```

---

## 5. Recurrence Relationship

The statement that calls the function again is known as the recurrence relationship.

### Example

```python
return n * fact(n - 1)
```

Here:

* Problem is reduced to a smaller version.
* Function keeps solving smaller problems until the base case is reached.

---

## 6. Practice Question 1

### Write a recursive function to calculate the sum of first n natural numbers.

### Program

```python
def sum(n):

    if(n == 0):
        return 0

    return n + sum(n - 1)

print(sum(5))
```

### Output

```text
15
```

### Explanation

```text
sum(5)
= 5 + sum(4)
= 5 + 4 + sum(3)
= 5 + 4 + 3 + sum(2)
= 5 + 4 + 3 + 2 + sum(1)
= 5 + 4 + 3 + 2 + 1
= 15
```

---

## 7. Practice Question 2

### Write a recursive function to print all elements of a list.

### Program

```python
def printList(list, indx=0):

    if(indx == len(list)):
        return

    print(list[indx])

    printList(list, indx + 1)

list = ["mango", "licchi", "papaya", "grapes", "pineapple"]

print(printList(list))
```

### Output

```text
mango
licchi
papaya
grapes
pineapple
None
```

### Explanation

* First element is printed.
* Function calls itself with the next index.
* Continues until index becomes equal to list length.
* Function returns `None`, which is why `None` is displayed at the end.

---

## Key Learnings

* Recursion means a function calling itself.
* Every recursive function must contain a base case.
* Base cases prevent infinite recursion.
* Recursive calls solve smaller versions of the same problem.
* Factorial problems are commonly solved using recursion.
* Recursive functions can calculate sums efficiently.
* Lists can also be traversed recursively using an index parameter.
* Recursive solutions often look shorter and cleaner than iterative solutions.

---

## Files Created

* declaration.py
* recursionFactorial.py
* practiceQuestion1.py
* practiceQuestion2.py

---

## Date Learned

24 June 2026