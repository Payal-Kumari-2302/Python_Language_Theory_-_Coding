# Day 11 – All List Methods in Python

## Q1. What does the append() method do?

**Definition:** Adds one item to the end of a list.

```python
numbers = [10, 20]
numbers.append(30)
print(numbers)
```

## Q2. What does the extend() method do?

**Definition:** Adds all items from an iterable to the end of a list.

```python
numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)
```

## Q3. What does the insert() method do?

**Definition:** Adds an item at a specified index.

```python
numbers = [10, 30]
numbers.insert(1, 20)
print(numbers)
```

## Q4. What does the remove() method do?

**Definition:** Removes the first occurrence of a specified value.

```python
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)
```

## Q5. What does the pop() method do?

**Definition:** Removes and returns an item by index. By default, it removes the last item.

```python
numbers = [10, 20, 30]
numbers.pop()
print(numbers)
```

## Q6. What does the clear() method do?

**Definition:** Removes all items from a list.

```python
numbers = [10, 20, 30]
numbers.clear()
print(numbers)
```

## Q7. What does the index() method do?

**Definition:** Returns the index of the first occurrence of a specified value.

```python
numbers = [10, 20, 30]
print(numbers.index(20))
```

## Q8. What does the count() method do?

**Definition:** Returns the number of times a value appears in a list.

```python
numbers = [10, 20, 10, 30]
print(numbers.count(10))
```

## Q9. What does the sort() method do?

**Definition:** Sorts the original list in ascending order by default.

```python
numbers = [30, 10, 20]
numbers.sort()
print(numbers)
```

## Q10. What does the reverse() method do?

**Definition:** Reverses the order of items in the original list.

```python
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)
```

## Q11. What does the copy() method do?

**Definition:** Returns a shallow copy of a list.

```python
numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)
```
