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

**Output:** `{1, 2, 3, 4, 5}`

### Q8. What is the difference between `remove()` and `discard()`?

**Definition:** Both remove an element. However, `remove()` raises a `KeyError` if the element is absent, whereas `discard()` does not raise an error.

**Example:**

```python
numbers = {1, 2, 3}

numbers.remove(2)
numbers.discard(5)

print(numbers)
```

**Output:** `{1, 3}`

### Q9. What are union and intersection?

**Definition:** Union combines all unique elements from two sets. Intersection returns only the common elements.

**Example:**

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
```

**Output:**

```text
{1, 2, 3, 4, 5}
{3}
```

### Q10. What is the difference between difference and symmetric difference?

**Definition:** Difference returns elements present in the first set but not in the second. Symmetric difference returns elements that are not common to both sets.

**Example:**

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)
print(a ^ b)
```

**Output:**

```text
{1, 2}
{1, 2, 4, 5}
```

### Q11. What are subset and superset?

**Definition:** A subset contains only elements that are present in another set. A superset contains all elements of another set.

**Example:**

```python
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))
print(b.issuperset(a))
```

**Output:**

```text
True
True
```

### Q12. What are disjoint sets?

**Definition:** Two sets are disjoint if they have no common elements.

**Example:**

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
```

**Output:** `True`

### Q13. What is a frozenset?

**Definition:** A `frozenset` is an immutable version of a set. Its elements cannot be added or removed after creation.

**Example:**

```python
numbers = frozenset([1, 2, 3])
print(numbers)
```

**Output:** `frozenset({1, 2, 3})`

### Q14. How can you remove duplicate elements from a list using a set?

**Definition:** Convert the list into a set to remove duplicate elements.

**Example:**

```python
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)
```

**Output:** `{1, 2, 3, 4}`
*Note: The original list's order is not guaranteed to be preserved.*

### Q15. What is the difference between `b = a` and `b = a.copy()`?

**Definition:** `b = a` makes both variables refer to the same set. `b = a.copy()` creates a separate, shallow copy of the set.

**Example:**

```python
a = {10, 20, 30}
b = a.copy()

b.add(40)

print(a)
print(b)
```

**Output:**

```text
{10, 20, 30}
{10, 20, 30, 40}
```
