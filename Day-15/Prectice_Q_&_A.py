```python
# Python 90 Days Challenge
# Day 15 - Practice Questions & Solutions


# Q1. Create a set containing five integers and print it.

# Q2. Create a set containing duplicate values and print it.

# Q3. Create an empty set and print its type.

# Q4. Add an element to a set using add().

# Q5. Add multiple elements to a set using update().

# Q6. Remove an element from a set using remove().

# Q7. Use discard() to remove an element that does not exist.

# Q8. Find the union of two sets.

# Q9. Find the intersection of two sets.

# Q10. Find the difference between two sets.

# Q11. Find the symmetric difference between two sets.

# Q12. Check whether one set is a subset of another.

# Q13. Check whether one set is a superset of another.

# Q14. Check whether two sets are disjoint.

# Q15. Remove duplicate elements from a list using a set.

# Q16. Copy a set, add an element to the copy, and print both sets.

# Q17. Create a frozenset from a list.

# Q18. Use set comprehension to create squares from 1 to 10.

# Q19. Find common student roll numbers in two classes.

# Q20. Find elements that belong to only one of two sets.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Create a set containing five integers and print it.
# ==================================================

numbers = {10, 20, 30, 40, 50}
print(numbers)


# ==================================================
# Q2. Create a set containing duplicate values and print it.
# ==================================================

numbers = {10, 20, 10, 30, 20, 40}
print(numbers)


# ==================================================
# Q3. Create an empty set and print its type.
# ==================================================

my_set = set()

print(my_set)
print(type(my_set))


# ==================================================
# Q4. Add an element to a set using add().
# ==================================================

numbers = {10, 20, 30}
numbers.add(40)

print(numbers)


# ==================================================
# Q5. Add multiple elements using update().
# ==================================================

numbers = {10, 20, 30}
numbers.update([40, 50, 60])

print(numbers)


# ==================================================
# Q6. Remove an element using remove().
# ==================================================

numbers = {10, 20, 30, 40}
numbers.remove(20)

print(numbers)


# ==================================================
# Q7. Use discard() to remove an element that does not exist.
# ==================================================

numbers = {10, 20, 30}
numbers.discard(50)

print(numbers)


# ==================================================
# Q8. Find the union of two sets.
# ==================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.union(B)
print(result)


# ==================================================
# Q9. Find the intersection of two sets.
# ==================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.intersection(B)
print(result)


# ==================================================
# Q10. Find the difference between two sets.
# ==================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))
print(B.difference(A))


# ==================================================
# Q11. Find the symmetric difference between two sets.
# ==================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A.symmetric_difference(B)
print(result)


# ==================================================
# Q12. Check whether one set is a subset of another.
# ==================================================

A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))


# ==================================================
# Q13. Check whether one set is a superset of another.
# ==================================================

A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))


# ==================================================
# Q14. Check whether two sets are disjoint.
# ==================================================

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))


# ==================================================
# Q15. Remove duplicate elements from a list using a set.
# ==================================================

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)


# ==================================================
# Q16. Copy a set, add an element to the copy, and print both.
# ==================================================

A = {10, 20, 30}
B = A.copy()

B.add(40)

print("Original set:", A)
print("Copied set:", B)


# ==================================================
# Q17. Create a frozenset from a list.
# ==================================================

numbers = [10, 20, 30, 20]

fixed_set = frozenset(numbers)

print(fixed_set)


# ==================================================
# Q18. Use set comprehension to cre
```
