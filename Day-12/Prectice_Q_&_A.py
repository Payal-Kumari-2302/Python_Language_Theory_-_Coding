# Day-11 – Lists in Python: Coding Practice with Answers

### Q1. Append an Element

Add `40` to the end of a list.

```python
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)
```

**Output:** `[10, 20, 30, 40]`

### Q2. Extend a List

Add multiple elements to a list using `extend()`.

```python
numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)
```

**Output:** `[10, 20, 30, 40]`

### Q3. Insert an Element

Insert `15` at index `1`.

```python
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)
```

**Output:** `[10, 15, 20, 30]`

### Q4. Remove an Element

Remove `20` from the list.

```python
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)
```

**Output:** `[10, 30]`

### Q5. Pop an Element

Remove and return the last element.

```python
numbers = [10, 20, 30]
x = numbers.pop()
print(x)
print(numbers)
```

**Output:**

```text
30
[10, 20]
```

### Q6. Clear a List

Remove all elements from the list.

```python
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
```

**Output:** `[]`

### Q7. Find an Element's Index

Find the index of `30`.

```python
numbers = [10, 20, 30, 40]
print(numbers.index(30))
```

**Output:** `2`

### Q8. Count an Element

Count how many times `10` appears.

```python
numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))
```

**Output:** `3`

### Q9. Sort a List

Sort the numbers in ascending order.

```python
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)
```

**Output:** `[10, 20, 30, 40]`

### Q10. Reverse a List

Reverse the order of list elements.

```python
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)
```

**Output:** `[30, 20, 10]`

### Q11. Copy a List

Create a copy of the original list.

```python
numbers = [10, 20, 30]
new_list = numbers.copy()
print(new_list)
```

**Output:** `[10, 20, 30]`

### Q12. Find the Length of a List

Use `len()` to count the elements.

```python
numbers = [10, 20, 30, 40]
print(len(numbers))
```

**Output:** `4`

### Q13. Find the Sum of Elements

Use `sum()` to calculate the total.

```python
numbers = [10, 20, 30]
print(sum(numbers))
```

**Output:** `60`

### Q14. Find Maximum and Minimum

Find the largest and smallest elements.

```python
numbers = [15, 5, 25, 10, 20]
print(max(numbers))
print(min(numbers))
```

**Output:**

```text
25
5
```

### Q15. Sort Without Modifying the Original List

Use `sorted()` to create a new sorted list.

```python
numbers = [30, 10, 20]
new_list = sorted(numbers)
print(new_list)
print(numbers)
```

**Output:**

```text
[10, 20, 30]
[30, 10, 20]
```

**Day-11 Completed: Lists in Python**
