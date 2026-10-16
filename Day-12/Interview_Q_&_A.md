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

### Q8. What is th
