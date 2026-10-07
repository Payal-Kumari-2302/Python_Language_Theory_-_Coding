# 🐍 Python 90 Days Challenge

## Day 05 – Python Strings | BCA Fresher Interview Questions

### 1. What is a string in Python?

A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.

### 2. How do you create a string in Python?

We can create a string using single quotes, double quotes, or triple quotes.

```python
name = "Payal"
```

### 3. What is string indexing?

String indexing is used to access individual characters of a string. Python indexing starts from `0`.

```python
word = "Python"
print(word[0])  # P
```

### 4. What is negative indexing?

Negative indexing is used to access characters from the end of a string.

```python
word = "Python"
print(word[-1])  # n
```

### 5. What is string slicing?

String slicing is used to extract a part of a string.

```python
word = "Python"
print(word[0:3])  # Pyt
```

### 6. Is a string mutable or immutable in Python?

A string is **immutable**, which means its characters cannot be changed directly after the string is created.

### 7. What are string methods in Python?

String methods are built-in methods used to perform operations on strings.

Examples:

`lower()`, `upper()`, `strip()`, `replace()`, `split()`, `find()`, and `count()`.

### 8. What is the difference between `lower()` and `upper()`?

`lower()` converts a string to lowercase, while `upper()` converts a string to uppercase.

```python
"PYTHON".lower()   # python
"python".upper()   # PYTHON
```

### 9. What is the use of `strip()`?

`strip()` removes extra spaces from the beginning and end of a string.

```python
" Python ".strip()
```

### 10. What is the use of `split()`?

`split()` divides a string into a list using a specified separator.

```python
"a,b,c".split(",")
```

Output:

```text
['a', 'b', 'c']
```

### 11. What is the difference between `find()` and `index()`?

Both are used to find the position of a substring.

* `find()` returns `-1` if the substring is not found.
* `index()` raises an error if the substring is not found.

### 12. What is string concatenation?

String concatenation means joining two or more strings using the `+` operator.

```python
first = "Hello"
second = "Python"

print(first + " " + second)
```

### 13. What is string formatting in Python?

String formatting is used to insert values into a string.

The commonly used methods are **f-strings** and `format()`.

```python
name = "Payal"
print(f"Hello {name}")
```

### 14. What are escape characters in Python?

Escape characters are special characters that start with a backslash `\`.

Common examples:

* `\n` → New line
* `\t` → Tab
* `\\` → Backslash
* `\'` → Single quote
* `\"` → Double quote

### 15. How can you reverse a string in Python?

We can reverse a string using slicing with `[::-1]`.

```python
word = "Python"
print(word[::-1])
```

Output:

```text
nohtyP
```
