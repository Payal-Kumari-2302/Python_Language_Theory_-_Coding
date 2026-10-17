# Day-13: Python 90 Days Challenge

## Coding Questions – Tuples in Python

### Questions

# #**Q1.** Create a tuple containing five integers and print it.

# **Q2.** Create a tuple containing different data types and print it.

# **Q3.** Create a tuple containing a single element and print its type.

# **Q4.** Access and print the first and last elements of a tuple.

# **Q5.** Access the third element of a tuple using negative indexing.

# **Q6.** Slice a tuple to print the elements from index 1 to index 3.

# **Q7.** Count how many times a specified element appears in a tuple.

# **Q8.** Find the index of a specified element in a tuple.

# **Q9.** Find the length of a tuple.

# **Q10.** Check whether a specified element exists in a tuple.

# **Q11.** Concatenate two tuples and print the result.

# **Q12.** Repeat a tuple three times using the repetition operator.

# **Q13.** Convert a list into a tuple.

# **Q14.** Convert a tuple into a list and modify one element.

# **Q15.** Unpack a tuple into separate variables and print their values.

# **Q16.** Use starred unpacking to store the middle elements of a tuple in a list.

# **Q17.** Find the maximum and minimum values in a tuple of integers.

# **Q18.** Calculate the sum of all numeric elements in a tuple.

# **Q19.** Create a nested tuple and access an element from the inner tuple.

# **Q20.** Demonstrate that a tuple is immutable by attempting to change one of its elements.

---

### Practice Instructions

1. Solve all questions in Python.
2. Try to solve each question independently before checking the solutions.
3. Run the programs and verify their outputs.
4. Save your solutions in `coding_questions.md`.

---

### Solutions

**Q1.**

```python
numbers = (10, 20, 30, 40, 50)
print(numbers)
```

**Q2.**

```python
data = ("Payal", 21, 85.5, True)
print(data)
```

**Q3.**

```python
single = (10,)
print(type(single))
```

**Q4.**

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[-1])
```

**Q5.**

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[-3])
```

**Q6.**

```python
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
```

**Q7.**

```python
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))
```

**Q8.**

```python
numbers = (10, 20, 30, 40)
print(numbers.index(30))
```

**Q9.**

```python
numbers = (10, 20, 30, 40, 50)
print(len(numbers))
```

**Q10.**

```python
numbers = (10, 20, 30, 40)
print(30 in numbers)
```

**Q11.**

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)
```

**Q12.**

```python
numbers = (1, 2, 3)
print(numbers * 3)
```

**Q13.**

```python
numbers = [10, 20, 30]
result = tuple(numbers)
print(result)
```

**Q14.**

```python
numbers = (10, 20, 30)
result = list(numbers)
result[0] = 100
print(result)
```

**Q15.**

```python
student = ("Payal", 21, "BCA")
name, age, course = student

print(name)
print(age)
print(course)
```

**Q16.**

```python
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers

print(middle)
```

**Q17.**

```python
numbers = (15, 5, 25, 10, 20)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
```

**Q18.**

```python
numbers = (10, 20, 30, 40)
print(sum(numbers))
```

**Q19.**

```python
data = (10, 20, (30, 40, 50))
print(data[2][1])
```

**Q20.**

```python
numbers = (10, 20, 30)

try:
    numbers[0] = 100
except TypeError as e:
    print("Error:", e)
```
