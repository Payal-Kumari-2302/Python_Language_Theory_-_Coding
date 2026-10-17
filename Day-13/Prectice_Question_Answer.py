```python
# Python 90 Days Challenge
# Day 13 - Practice Questions & Solutions

# Python 90 Days Challenge
# Day 13 - Practice

# Q1. Create a tuple containing five integers and print it.

# Q2. Create a tuple containing different data types and print it.

# Q3. Create a tuple with a single element and print its type.

# Q4. Print the first and last elements of a tuple.

# Q5. Access the third element using negative indexing.

# Q6. Print elements from index 1 to index 3 using slicing.

# Q7. Count how many times 10 appears in a tuple.

# Q8. Find the index of the element 30 in a tuple.

# Q9. Find the length of a tuple.

# Q10. Check whether 30 exists in a tuple.

# Q11. Concatenate two tuples and print the result.

# Q12. Repeat a tuple three times.

# Q13. Convert a list into a tuple.

# Q14. Convert a tuple into a list and modify one element.

# Q15. Unpack a tuple into separate variables and print them.

# Q16. Use starred unpacking to store the middle elements.

# Q17. Find the maximum and minimum values in a tuple.

# Q18. Calculate the sum of all elements in a tuple.

# Q19. Create a nested tuple and access an inner element.

# Q20. Demonstrate that a tuple is immutable.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Create a tuple containing five integers and print it.
# ==================================================

numbers = (10, 20, 30, 40, 50)
print(numbers)


# ==================================================
# Q2. Create a tuple containing different data types and print it.
# ==================================================

data = ("Payal", 21, 85.5, True)
print(data)


# ==================================================
# Q3. Create a tuple with a single element and print its type.
# ==================================================

single = (10,)
print(type(single))


# ==================================================
# Q4. Print the first and last elements of a tuple.
# ==================================================

numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[-1])


# ==================================================
# Q5. Access the third element using negative indexing.
# ==================================================

numbers = (10, 20, 30, 40, 50)
print(numbers[-3])


# ==================================================
# Q6. Print elements from index 1 to index 3 using slicing.
# ==================================================

numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])


# ==================================================
# Q7. Count how many times 10 appears in a tuple.
# ==================================================

numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))


# ==================================================
# Q8. Find the index of the element 30 in a tuple.
# ==================================================

numbers = (10, 20, 30, 40)
print(numbers.index(30))


# ==================================================
# Q9. Find the length of a tuple.
# ==================================================

numbers = (10, 20, 30, 40, 50)
print(len(numbers))


# ==================================================
# Q10. Check whether 30 exists in a tuple.
# ==================================================

numbers = (10, 20, 30, 40)
print(30 in numbers)


# ==================================================
# Q11. Concatenate two tuples and print the result.
# ==================================================

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2
print(result)


# ==================================================
# Q12. Repeat a tuple three times.
# ==================================================

numbers = (1, 2, 3)
print(numbers * 3)


# ==================================================
# Q13. Convert a list into a tuple.
# ==================================================

numbers = [10, 20, 30]
result = tuple(numbers)
print(result)


# ==================================================
# Q14. Convert a tuple into a list and modify one element.
# ==================================================

numbers = (10, 20, 30)
result = list(numbers)

result[0] = 100
print(result)


# ==================================================
# Q15. Unpack a tuple into separate variables and print them.
# ==================================================

student = ("Payal", 21, "BCA")

name, age, course = student

print(name)
print(age)
print(course)


# ==================================================
# Q16. Use starred unpacking to store the middle elements.
# ==================================================

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(middle)


# ==================================================
# Q17. Find the maximum and minimum values in a tuple.
# ==================================================

numbers = (15, 5, 25, 10, 20)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# ==================================================
# Q18. Calculate the sum of all elements in a tuple.
# ==================================================

numbers = (10, 20, 30, 40)
print(sum(numbers))


# ==================================================
# Q19. Create a nested tuple and access an inner element.
# ==================================================

data = (10, 20, (30, 40, 50))
print(data[2][1])


# ==================================================
# Q20. Demonstrate that a tuple is immutable.
# ==================================================

numbers = (10, 20, 30)

try:
    numbers[0] = 100
except TypeError:
    print("Tuple elements cannot be changed.")
```
