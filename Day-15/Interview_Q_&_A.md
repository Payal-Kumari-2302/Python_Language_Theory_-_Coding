# Python 90 Days Challenge

## Day-15 — Python Set Interview Questions

### Definitions & Examples

### Q1. What is a set in Python?

**Definition:** A set is a collection of unique elements. It is unordered and does not allow duplicate values.

**Example:**

```python
numbers = {10, 20, 30, 20}
print(numbers)
```

**Output:** `{10, 20, 30}`
*Note: The order of elements may vary.*

### Q2. What are the main characteristics of a set?

**Definition:** A Python set stores unique elements, is mutable, and does not support indexing.

**Example:**

```python
items = {10, 20, 30}
items.add(40)
print(items)
```

**Output:** `{10, 20, 30, 40}`
*Note: The order may vary.*

### Q3. Does a set allow duplicate elements?

**Definition:** No, a set automatically removes duplicate elements.

**Example:**

```python
numbers = {1, 2, 2, 3, 3}
print(numbers)
```

**Output:** `{1, 2, 3}`

### Q4. What is the difference between a list and a set?

**Definition:** A list is ordered and allows duplicates, whereas a set is unordered and stores unique elements.

**Example:**

```python
my_list = [1, 2, 2, 3]
my_set = {1, 2, 2, 3}

print(my_list)
print(my_set)
```

**Output:**

```text
[1, 2, 2, 3]
{1, 2, 3}
```

### Q5. How do you create an empty set in Python?

**Definition:** We use `set()` to create an empty set. `{}` creates an empty dictionary.

**Example:**

```python
my_set = set()
print(my_set)
print(type(my_set))
```

**Output:**

```text
set()
<class 'set'>
```

### Q6. Can we access set elements using indexing?

**Definition:** No, sets do not support indexing because they are unordered collections.

**Example:**

```python
numbers = {10, 20, 30}
print(numbers[0])
```

**Output:** `TypeError`

### Q7. What is the difference between `add()` and `update()`?

**Definition:** `add()` inserts one element, while `update()` inserts multiple elements from an iterable.

**Example:**

```python
numbers = {1, 2}
numbers.add(3)
numbers.update([4, 5])

print(numbers)
```

**Output:** `{1, 2, 3, 4,
