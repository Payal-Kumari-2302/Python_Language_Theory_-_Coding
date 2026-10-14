# Day 11 – Lists in Python

## Q1. What is a list in Python?

**Definition:** A list is a built-in data structure used to store multiple items in a single variable. It is ordered, mutable, and allows duplicate values.

**Example:**

```python
fruits = ["Apple", "Banana", "Mango"]
print(fruits)
```

## Q2. What are the main features of a list?

**Definition:** A Python list is ordered, mutable, allows duplicate values, and can store different data types.

**Example:**

```python
items = [10, "Python", 10, 3.5]
print(items)
```

## Q3. What is positive and negative indexing?

**Definition:** Positive indexing starts from `0` on the left, while negative indexing starts from `-1` on the right.

**Example:**

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])
```

## Q4. What is the difference between append() and extend()?

**Definition:**

* `append()` adds one item to the end of a list.
* `extend()` adds multiple items from an iterable to a list.

**Example:**

```python
numbers = [10, 20]

numbers.append(30)
print(numbers)

numbers.extend([40, 50])
print(numbers)
```

## Q5. What is the difference between remove() and pop()?

**Definition:**

* `remove()` removes an item by value.
* `pop()` removes and returns an item by index. Without an index, it removes the last item.

**Example:**

```python
numbers = [10, 20, 30, 40]

numbers.remove(20)
print(numbers)

removed = numbers.pop()
print(removed)
print(numbers)
```

## Q6. What is the difference between sort() and sorted()?

**Definition:**

* `sort()` sorts the original list.
* `sorted()` returns a new sorted list without changing the original list.

**Example:**

```python
numbers = [30, 10, 20]

numbers.sort()
print(numbers)

numbers = [30, 10, 20]
print(sorted(numbers))
print(numbers)
```

## Q7. What are index() and count() methods?

**Definition:**

* `index()` returns the index of the first occurrence of a value.
* `count()` returns the number of times a value appears in a list.

**Example:**

```python
numbers = [10, 20, 10, 30]

print(numbers.index(20))
print(numbers.count(10))
```

## Q8. What does the reverse() method do?

**Definition:** The `reverse()` method reverses the order of elements in the original list.

**Example:**

```python
numbers = [10, 20, 30, 40]
numbers.reverse()

print(numbers)
```
