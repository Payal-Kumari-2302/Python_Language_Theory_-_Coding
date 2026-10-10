# 🐍 Python Loops — Pattern Printing & Coding Questions with Solutions

**Topics:** `for` loop, `while` loop, nested loops, star patterns, number patterns, and coding interview questions.

---

# ⭐ Part 1: Star Pattern Questions

## Q1. Print a Square Pattern

**Output:**

```text
* * * *
* * * *
* * * *
* * * *
```

**Solution:**

```python
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
```

## Q2. Print a Right-Angled Triangle

**Output:**

```text
*
* *
* * *
* * * *
* * * * *
```

**Solution:**

```python
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
```

## Q3. Print an Inverted Right-Angled Triangle

**Output:**

```text
* * * * *
* * * *
* * *
* *
*
```

**Solution:**

```python
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

## Q4. Print an Increasing Star Pattern

**Output:**

```text
*
**
***
****
*****
```

**Solution:**

```python
for i in range(1, 6):
    print("*" * i)
```

## Q5. Print an Inverted Star Triangle

**Output:**

```text
*****
****
***
**
*
```

**Solution:**

```python
for i in range(5, 0, -1):
    print("*" * i)
```

## Q6. Print a Pyramid Pattern

**Output:**

```text
    *
   ***
  *****
 *******
*********
```

**Solution:**

```python
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

## Q7. Print an Inverted Pyramid

**Output:**

```text
*********
 *******
  *****
   ***
    *
```

**Solution:**

```python
n = 5

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

## Q8. Print a Hollow Square

**Output:**

```text
* * * * *
*       *
*       *
*       *
* * * * *
```

**Solution:**

```python
n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

## Q9. Print a Diamond Pattern

**Output:**

```text
    *
   ***
  *****
 *******
  *****
   ***
    *
```

**Solution:**

```python
n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" "
```
