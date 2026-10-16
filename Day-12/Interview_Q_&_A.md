# Day-12 – Tuple Interview Questions & Answers

### Q1. What is a tuple in Python?

**Answer:** A tuple is an ordered and immutable collection of elements.

```python
t = (10, 20, 30)
```

### Q2. What are the main features of tuples?

**Answer:** Tuples are ordered, immutable, allow duplicates, and support indexing and slicing.

```python
t = (10, 20, 10)
print(t[0])  # 10
```

### Q3. How do you create a single-element tuple?

**Answer:** By adding a comma after the element.

```python
t = (10,)
```

### Q4. Can a tuple contain duplicate values?

**Answer:** Yes.

```python
t = (10, 20, 10)
```

### Q5. Can a tuple store different data types?

**Answer:** Yes.

```python
t = (10, "Python", 3.5, True)
```

### Q6. What is the difference between a list and a tuple?

**Answer:** A list is mutable, whereas a tuple is immutable.

```python
my_list = [10, 20]
my_tuple = (10, 20)
```

### Q7. How many built-in methods does a tuple have?

**Answer:** Two: `count()` and `index()`.

```python
t = (10, 20, 10)
print(t.count(10))  # 2
```

### Q8. What is the use of `count()`?

**Answer:** It counts how many times an element appears.

```python
t = (10, 20, 10)
print(t.count(10))  # 2
```

### Q9. What is the use of `index()`?

**Answer:** It returns the index of the first occurrence of an element.

```python
t = (10, 20, 30)
print(t.index(20))  # 1
```

### Q10. What are tuple packing and unpacking?

**Answer:** Packing combines values into a tuple; unpacking assigns them to separate variables.

```python
t = ("Payal", 21)  # Packing
name, age = t      # Unpacking
```

### Q11. Can we modify a tuple after creation?

**Answer:** No, tuples are immutable.

```python
t = (10, 20, 30)
# t[0] = 100  # TypeError
```

### Q12. Can a tuple contain a list?

**Answer:** Yes. The list inside the tuple can be modified.

```python
t = (10, [20, 30])
t[1].append(40)
print(t)  # (10, [20, 30, 40])
```

### Q13. What is a nested tuple?

**Answer:** A tuple that contains another tuple.

```python
t = ((1, 2), (3, 4))
print(t[1][0])  # 3
```

### Q14. Can we concatenate two tuples?

**Answer:** Yes, using the `+` operator.

```python
print((1, 2) + (3, 4))
# (1, 2, 3, 4)
```

### Q15. Can we repeat a tuple?

**Answer:** Yes, using the `*` operator.

```python
print((1, 2) * 2)
# (1, 2, 1, 2)
```

### Q16. What are the applications of tuples?

**Answer:** Tuples are used to store fixed data, coordinates, and RGB color values.

```python
point = (10, 20)
```

### Q17. Can a tuple be used as a dictionary key?

**Answer:** Yes, if all its elements are hashable.

```python
data = {(10, 20): "Point"}
```

### Q18. What happens if we modify a tuple element?

**Answer:** Python raises a `TypeError`.

```python
t = (10, 20)
# t[0] = 100
```

---

**Day-12 Completed: Tuples in Python**
