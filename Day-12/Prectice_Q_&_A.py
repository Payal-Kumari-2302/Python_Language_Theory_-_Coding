```python
# Python 90 Days Challenge
# Day 11 - Practice Questions & Solutions

# Python 90 Days Challenge
# Day 11 - Lists Practice

# Q1. Add 40 to the end of the list [10, 20, 30] using append().

# Q2. Add [30, 40] to the list [10, 20] using extend().

# Q3. Insert 15 at index 1 in the list [10, 20, 30].

# Q4. Remove 20 from the list [10, 20, 30].

# Q5. Remove the last element from the list [10, 20, 30].

# Q6. Remove all elements from the list [10, 20, 30].

# Q7. Find the index of 30 in the list [10, 20, 30, 40].

# Q8. Count how many times 10 appears in [10, 20, 10, 30, 10].

# Q9. Sort [40, 10, 30, 20] in ascending order.

# Q10. Reverse the list [10, 20, 30].

# Q11. Create a copy of the list [10, 20, 30].

# Q12. Find the number of elements in [10, 20, 30, 40].

# Q13. Calculate the sum of [10, 20, 30].

# Q14. Find the maximum and minimum values in [15, 5, 25, 10, 20].

# Q15. Sort [30, 10, 20] without changing the original list.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solutions immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Add an element using append().
# ==================================================

numbers = [10, 20, 30]
numbers.append(40)
print(numbers)


# ==================================================
# Q2. Add multiple elements using extend().
# ==================================================

numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)


# ==================================================
# Q3. Insert an element using insert().
# ==================================================

numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)


# ==================================================
# Q4. Remove an element using remove().
# ==================================================

numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)


# ==================================================
# Q5. Remove the last element using pop().
# ==================================================

numbers = [10, 20, 30]
numbers.pop()
print(numbers)


# ==================================================
# Q6. Remove all elements using clear().
# ==================================================

numbers = [10, 20, 30]
numbers.clear()
print(numbers)


# ==================================================
# Q7. Find the index using index().
# ==================================================

numbers = [10, 20, 30, 40]
print(numbers.index(30))


# ==================================================
# Q8. Count elements using count().
# ==================================================

numbers = [10, 20, 10, 30, 10]
print(numbers.count(10))


# ==================================================
# Q9. Sort a list using sort().
# ==================================================

numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)


# ==================================================
# Q10. Reverse a list using reverse().
# ==================================================

numbers = [10, 20, 30]
numbers.reverse()
print(numbers)


# ==================================================
# Q11. Copy a list using copy().
# ==================================================

numbers = [10, 20, 30]
new_numbers = numbers.copy()
print(new_numbers)


# ==================================================
# Q12. Find the length of a list using len().
# ==================================================

numbers = [10, 20, 30, 40]
print(len(numbers))


# ==================================================
# Q13. Calculate the sum using sum().
# ==================================================

numbers = [10, 20, 30]
print(sum(numbers))


# ==================================================
# Q14. Find maximum and minimum values.
# ==================================================

numbers = [15, 5, 25, 10, 20]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


# ==================================================
# Q15. Sort a list using sorted().
# ==================================================

numbers = [30, 10, 20]
sorted_numbers = sorted(numbers)

print("Original List:", numbers)
print("Sorted List:", sorted_numbers)
```
