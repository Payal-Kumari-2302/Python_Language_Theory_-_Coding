# Day-13: Python 90 Days Challenge

## Interview Questions – Tuples in Python

### Q1. What is a tuple in Python?

**Definition:** A tuple is an ordered and immutable collection of elements.

**Example:**

```python
fruits = ("Apple", "Banana", "Mango")
print(fruits)
```

### Q2. How do you create a tuple?

**Definition:** A tuple is created by placing elements inside parentheses `()` separated by commas.

**Example:**

```python
numbers = (10, 20, 30)
print(numbers)
```

### Q3. Is a tuple mutable or immutable?

**Definition:** A tuple is immutable, which means its elements cannot be changed after creation.

**Example:**

```python
numbers = (10, 20, 30)
# numbers[0] = 100  # TypeError
```

### Q4. How do you access tuple elements?

**Definition:** Tuple elements can be accessed using their index.

**Example:**

```python
colors = ("Red", "Green", "Blue")
print(colors[0])
```

**Output:**

```text
Red
```

### Q5. What is negative indexing in a tuple?

**Definition:** Negative indexing accesses elements from the end of a tuple.

**Example:**

```python
numbers = (10, 20, 30)
print(numbers[-1])
```

**Output:**

```text
30
```

### Q6. What is tuple slicing?

**Definition:** Slicing extracts a specific portion of a tuple.

**Example:**

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
```

**Output:**

```text
(20, 30, 40)
```

### Q7. Can a tuple contain duplicate values?

**Definition:** Yes, a tuple allows duplicate elements.

**Example:**

```python
numbers = (10, 20, 10, 30)
print(numbers)
```

### Q8. Can a tuple store different data types?

**Definition:** Yes, a tuple can contain elements of different data types.

**Example:**

```python
data = ("Payal", 21, 85.5, True)
print(data)
```

### Q9. How do you create a tuple with a single element?

**Definition:** A single-element tuple requires a comma after the element.

**Example:**

```python
single = (10,)
print(type(single))
```

### Q10. What is tuple packing?

**Definition:** Tuple packing means combining multiple values into a single tuple.

**Example:**

```python
student = "Payal", 21, "BCA"
print(student)
```

### Q11. What is tuple unpacking?

**Definition:** Tuple unpacking assigns tuple elements to separate variables.

**Example:**

```python
student = ("Payal", 21, "BCA")
name, age, course = student

print(name)
print(age)
print(course)
```

### Q12. What is the `count()` method?

**Definition:** The `count()` method returns how many times a value appears in a tuple.

**Example:**

```python
numbers = (10, 20, 10, 30)
print(numbers.count(10))
```

**Output:**

```text
2
```

### Q13. What is the `index()` method?

**Definition:** The `index()` method returns the index of the first occurrence of a specified value.

**Example:**

```python
numbers = (10, 20, 30, 20)
print(numbers.index(20))
```

**Output:**

```text
1
```

### Q14. What is the difference between a tuple and a list?

**Definition:** A tuple is immutable, whereas a list is mutable.

**Example:**

```python
my_tuple = (10, 20, 30)
my_list = [10, 20, 30]

my_list[0] = 100
print(my_list)
```

### Q15. How can you find the length of a tuple?

**Definition:** The `len()` function returns the total number of elements in a tuple.

**Example:**

```python
numbers = (10, 20, 30, 40)
print(len(numbers))
```

**Output:**

```text
4
```

### Q16. Can we add or remove elements from a tuple?

**Definition:** Tuples do not support direct addition or removal of elements because they are immutable.

**Example:**

```python
numbers = (10, 20, 30)
# numbers.append(40)  # AttributeError
```

### Q17. What is a nested tuple?

**Definition:** A nested tuple is a tuple that contains another tuple as an element.

**Example:**

```python
data = (10, 20, (30, 40))
print(data[2])
```

**Output:**

```text
(30, 40)
```

### Q18. What is a named tuple?

**Definition:** A named tuple is a tuple-like object whose elements can be accessed using names as well as indexes.

**Example:**

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])
s1 = Student("Payal", 21)

print(s1.name)
```

**Output:**

```text
Payal
```

### Q19. What is starred unpacking in Python?

**Definition:** Starred unpacking uses `*` to collect multiple remaining elements into a list.

**Example:**

```python
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers

print(middle)
```

**Output:**

```text
[20, 30, 40]
```

### Q20. Why are tuples useful in Python?

**Definition:** Tuples are useful for storing ordered data that should not be changed accidentally.

**Example:**

```python
coordinates = (25.6, 85.1)
print(coordinates)
```

**Output:**

```text
(25.6, 85.1)
```
