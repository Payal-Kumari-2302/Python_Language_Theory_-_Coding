# Python 90 Days Challenge

## Day 19 — Interview Questions & Answers

### Topics: Advanced Functions

### 1. What are First-Class Functions in Python?

**Definition:** Functions can be stored in variables, passed as arguments, and returned from other functions.

**Example:**

```python
def greet():
    print("Hello")

message = greet
message()
```

**Output:** `Hello`

### 2. What is a Lambda Function?

**Definition:** A lambda function is a small anonymous function written using the `lambda` keyword.

**Example:**

```python
square = lambda x: x * x
print(square(5))
```

**Output:** `25`

### 3. What is the Syntax of a Lambda Function?

**Definition:** A lambda function uses arguments followed by a single expression.

**Example:**

```python
lambda x: x + 10
```

### 4. What is the `map()` Function?

**Definition:** `map()` applies a function to every item in an iterable.

**Example:**

```python
numbers = [1, 2, 3]
print(list(map(lambda x: x * x, numbers)))
```

**Output:** `[1, 4, 9]`

### 5. What is the `filter()` Function?

**Definition:** `filter()` selects items from an iterable based on a condition.

**Example:**

```python
numbers = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, numbers)))
```

**Output:** `[2, 4]`

### 6. What is the `reduce()` Function?

**Definition:** `reduce()` combines iterable items step by step into one final value.

**Example:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, numbers))
```

**Output:** `10`

### 7. What is the Difference Between `map()` and `filter()`?

**Definition:** `map()` transforms every item, while `filter()` selects items that satisfy a condition.

**Example:**

```python
numbers = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))
```

**Output:**

```text
[2, 4, 6, 8]
[2, 4]
```

### 8. What is the Difference Between `map()`, `filter()`, and `reduce()`?

**Definition:**

* `map()` — transforms items.
* `filter()` — selects items.
* `reduce()` — combines items into one value.

**Example:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]

print(list(map(lambda x: x * 2, numbers)))
print(list(filter(lambda x: x > 2, numbers)))
print(reduce(lambda a, b: a + b, numbers))
```

### 9. What Does `list()` Do with `map()` and `filter()`?

**Definition:** In Python 3, `map()` and `filter()` return iterators. `list()` converts their results into a list.

**Example:**

```python
numbers = [1, 2, 3]
result = map(lambda x: x + 1, numbers)
print(list(result))
```

**Output:** `[2, 3, 4]`

### 10. From Which Module Do We Import `reduce()`?

**Definition:** We import `reduce()` from the `functools` module.

**Example:**

```python
from functools import reduce
```

### 11. What Does the Function Passed to `filter()` Return?

**Definition:** It returns `True` or `False` to decide whether an item should be kept.

**Example:**

```python
print(list(filter(lambda x: x > 5, [2, 6, 8])))
```

**Output:** `[6, 8]`

### 12. Can a Lambda Function Take Multiple Arguments?

**Definition:** Yes, a lambda function can accept multiple arguments but contains only one expression.

**Example:**

```python
add = lambda a, b: a + b
print(add(5, 3))
```

**Output:** `8`

### 13. When Should We Use a Lambda Function?

**Definition:** Use a lambda function for small, simple operations.

**Example:**

```python
double = lambda x: x * 2
print(double(4))
```

**Output:** `8`

### 14. What Does `reduce()` Return?

**Definition:** `reduce()` returns a single final value after combining the iterable's items.

**Example:**

```python
from functools import reduce

print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))
```

**Output:** `24`
