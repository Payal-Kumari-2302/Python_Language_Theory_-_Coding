# Python 90 Days Challenge

## Day 03 – Python Data Types: Fresher Interview Questions

---

### <span style="color:red">Q1. What are data types in Python?</span>

Data types define the type of value stored in a variable and determine what operations can be performed on that value.

---

### <span style="color:red">Q2. What are the main built-in data types in Python?</span>

The main built-in data types include:

* `int`
* `float`
* `complex`
* `bool`
* `str`
* `list`
* `tuple`
* `set`
* `dict`
* `NoneType`

---

### <span style="color:red">Q3. What is an integer (`int`) in Python?</span>

`int` represents whole numbers without a decimal point.

Example:

```python
age = 21
```

---

### <span style="color:red">Q4. What is a float in Python?</span>

`float` represents numbers containing a decimal point.

Example:

```python
price = 99.50
```

---

### <span style="color:red">Q5. What is a complex number in Python?</span>

A complex number consists of a real part and an imaginary part.

Example:

```python
z = 3 + 4j
```

---

### <span style="color:red">Q6. What is a Boolean (`bool`) in Python?</span>

Boolean represents one of two values: `True` or `False`.

Example:

```python
is_student = True
```

---

### <span style="color:red">Q7. What is a string (`str`) in Python?</span>

A string is a sequence of characters enclosed in single, double, or triple quotes.

Example:

```python
name = "Payal"
```

---

### <span style="color:red">Q8. What is a list in Python?</span>

A list is an ordered and mutable collection of elements. It can contain different data types.

Example:

```python
numbers = [10, 20, 30]
```

---

### <span style="color:red">Q9. What is a tuple in Python?</span>

A tuple is an ordered and immutable collection of elements.

Example:

```python
numbers = (10, 20, 30)
```

---

### <span style="color:red">Q10. What is a set in Python?</span>

A set is an unordered collection of unique elements.

Example:

```python
numbers = {10, 20, 30}
```

---

### <span style="color:red">Q11. What is a dictionary in Python?</span>

A dictionary stores data in key-value pairs.

Example:

```python
student = {"name": "Payal", "age": 21}
```

---

### <span style="color:red">Q12. What is NoneType in Python?</span>

`NoneType` is the data type of the special value `None`, which represents the absence of a value.

Example:

```python
result = None
```

---

### <span style="color:red">Q13. How can you check the data type of a variable?</span>

We can use the `type()` function.

Example:

```python
x = 10
print(type(x))
```

Output:

```text
<class 'int'>
```

---

### <span style="color:red">Q14. What is the difference between mutable and immutable data types?</span>

Mutable objects can be changed after creation, while immutable objects cannot be changed after creation.

**Mutable:** `list`, `set`, `dict`

**Immutable:** `int`, `float`, `bool`, `str`, `tuple`

---

### <span style="color:red">Q15. Is Python statically typed or dynamically typed?</span>

Python is a **dynamically typed language**. The type of a variable is determined at runtime, so we do not need to declare its type explicitly.
