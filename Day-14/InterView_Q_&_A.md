
# Python 90 Days Challenge – Day 14

## Python Dictionary: BCA Fresher Interview Questions

### Q1. What is a dictionary in Python?

**Answer:** A dictionary stores data in key-value pairs.

**Example:**

```python
student = {"name": "Payal", "age": 21}
print(student["name"])
# Output: Payal
```

### Q2. Is a dictionary mutable?

**Answer:** Yes, we can modify a dictionary after creating it.

**Example:**

```python
student = {"name": "Payal"}
student["name"] = "Priya"
```

### Q3. Can a dictionary contain duplicate keys?

**Answer:** No. Duplicate keys overwrite their previous values.

**Example:**

```python
data = {"a": 10, "a": 20}
print(data)
# Output: {'a': 20}
```

### Q4. How do you add an item to a dictionary?

**Answer:** Assign a value to a new key.

**Example:**

```python
student = {"name": "Payal"}
student["age"] = 21
```

### Q5. How do you access a dictionary value safely?

**Answer:** Use the `get()` method to avoid a `KeyError` when a key is missing.

**Example:**

```python
student = {"name": "Payal"}
print(student.get("age", "Not found"))
# Output: Not found
```

### Q6. What is the difference between `get()` and `pop()`?

**Answer:** `get()` retrieves a value; `pop()` retrieves and removes an item.

**Example:**

```python
data = {"a": 10, "b": 20}
print(data.get("a"))  # 10
print(data.pop("b"))  # 20
```

### Q7. How do you delete an item from a dictionary?

**Answer:** Use `del` or `pop()`.

**Example:**

```python
student = {"name": "Payal", "age": 21}
del student["age"]
```

### Q8. What do `keys()`, `values()`, and `items()` return?

**Answer:** They provide the dictionary's keys, values, and key-value pairs.

**Example:**

```python
data = {"a": 10, "b": 20}
print(data.keys())
print(data.values())
print(data.items())
```

### Q9. How do you check whether a key exists?

**Answer:** Use the `in` operator.

**Example:**

```python
student = {"name": "Payal"}
print("name" in student)
# Output: True
```

### Q10. How do you loop through a dictionary?

**Answer:** Use a `for` loop with `items()`.

**Example:**

```python
student = {"name": "Payal", "age": 21}

for key, value in student.items():
    print(key, value)
```

### Q11. What is a nested dictionary?

**Answer:** A dictionary inside another dictionary is called a nested dictionary.

**Example:**

```python
students = {
    "student1": {"name": "Payal", "marks": 85}
}
print(students["student1"]["marks"])
# Output: 85
```

### Q12. What is dictionary comprehension?

**Answer:** It is a short way to create a dictionary using an expression and a loop.

**Example:**

```python
squares = {x: x*x for x in range(1, 4)}
print(squares)
# Output: {1: 1, 2: 4, 3: 9}
```

### Q13. What is the difference between a list and a dictionary?

**Answer:** A list stores items accessed by index; a dictionary stores key-value pairs accessed by keys.

**Example:**

```python
my_list = ["Payal", 21]
my_dict = {"name": "Payal", "age": 21}
```

### Q14. How do you find the number of items in a dictionary?

**Answer:** Use the `len()` function.

**Example:**

```python
data = {"a": 10, "b": 20}
print(len(data))
# Output: 2
```

### Q15. Give a real-world use of dictionaries.

**Answer:** Dictionaries can store student records, employee details, and product information.

**Example:**

```python
employee = {
    "id": 101,
    "name": "Payal",
    "department": "IT"
}
```

---

**Revision Tip:** Understand each answer and practise running the examples in Python.
