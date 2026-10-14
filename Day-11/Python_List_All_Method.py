# Python List Methods

Python provides several built-in methods to manipulate lists.

## 1. append()

**Definition:** Adds an element to the end of a list.

```python
numbers = [10, 20]
numbers.append(30)
print(numbers)  # [10, 20, 30]
```

## 2. extend()

**Definition:** Adds multiple elements to a list.

```python
numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)  # [10, 20, 30, 40]
```

## 3. insert()

**Definition:** Inserts an element at a specified position.

```python
numbers = [10, 30]
numbers.insert(1, 20)
print(numbers)  # [10, 20, 30]
```

## 4. remove()

**Definition:** Removes the first occurrence of a specified value.

```python
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)  # [10, 30]
```

## 5. pop()

**Definition:** Removes and returns an element by index. By default, removes the last element.

```python
numbers = [10, 20, 30]
numbers.pop()
print(numbers)  # [10, 20]
```

## 6. clear()

**Definition:** Removes all elements from a list.

```python
numbers = [10, 20, 30]
numbers.clear()
print(numbers)  # []
```

## 7. index()

**Definition:** Returns the index of the first occurrence of a value.

```python
numbers = [10, 20, 30]
print(numbers.index(20))  # 1
```

## 8. count()

**Definition:** Returns the number of occurrences of a value.

```python
numbers = [10, 20, 10, 30]
print(numbers.count(10))  # 2
```

## 9. sort()

**Definition:** Sorts the original list in ascending order by default.

```python
numbers = [30, 10, 20]
numbers.sort()
print(numbers)  # [10, 20, 30]
```

## 10. reverse()

**Definition:** Reverses the order of elements in the original list.

```python
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)  # [30, 20, 10]
```

## 11. copy()

**Definition:** Returns a shallow copy of a list.

```python
numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)  # [10, 20, 30]
```

---

# Useful Built-in Functions for Lists

## 12. len()

**Definition:** Returns the number of elements in a list.

```python
numbers = [10, 20, 30]
print(len(numbers))  # 3
```

## 13. sum()

**Definition:** Returns the sum of numeric elements.

```python
numbers = [10, 20, 30]
print(sum(numbers))  # 60
```

## 14. min()

**Definition:** Returns the smallest element.

```python
numbers = [10, 20, 30]
print(min(numbers))  # 10
```

## 15. max()

**Definition:** Returns the largest element.

```python
numbers = [10, 20, 30]
print(max(numbers))  # 30
```

## 16. sorted()

**Definition:** Returns a new sorted list without modifying the original list.

```python
numbers = [30, 10, 20]
print(sorted(numbers))  # [10, 20, 30]
print(numbers)          # [30, 10, 20]
```

---

## Important Note

* List methods modify the original list when specified by their behavior.
* `len()`, `sum()`, `min()`, `max()`, and `sorted()` are built-in functions, not list methods.
