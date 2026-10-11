```python
# Python 90 Days Challenge
# Day 09 - Break and Continue
# Pattern Printing Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Print a star triangle, but stop when the row number reaches 4.

# Q2. Print a star triangle, skipping row number 3.

# Q3. Print a number triangle, skipping even numbers.

# Q4. Print an increasing star pattern, but stop after 4 rows.

# Q5. Print a number pattern, skipping multiples of 3.

# Q6. Print a square star pattern, but skip the middle row.

# Q7. Print a triangle pattern, skipping even-numbered rows.

# Q8. Print numbers in a triangle, but stop when the number reaches 6.

# Q9. Print a star pattern, skipping the third star in each row.

# Q10. Print a number triangle, skipping number 3 in every row.

# Q11. Print an inverted star triangle, stopping after 2 rows.

# Q12. Print a square number pattern, skipping even numbers.

# Q13. Print a triangle of numbers, skipping rows divisible by 3.

# Q14. Print a star pattern, stopping when the row contains 4 stars.

# Q15. Print a number pattern, skipping multiples of 2 or 3.


# ==========================================
# PRACTICE INSTRUCTIONS
# ==========================================

# 1. Try to solve each question before checking the solution.
# 2. Use break to stop the loop.
# 3. Use continue to skip the current iteration.
# 4. Use nested loops to print rows and columns.
# 5. Use print("*", end=" ") for the same line.
# 6. Use print() to move to the next line.
# 7. Understand how break and continue affect patterns.


# ==================================================
# Q1. Print a star triangle, but stop when the row number reaches 4.
# ==================================================

# Expected Output:
# *
# * *
# * * *

for i in range(1, 6):
    if i == 4:
        break

    for j in range(i):
        print("*", end=" ")
    print()


# ==================================================
# Q2. Print a star triangle, skipping row number 3.
# ==================================================

# Expected Output:
# *
# * *
# * * * *
# * * * * *

for i in range(1, 6):
    if i == 3:
        continue

    for j in range(i):
        print("*", end=" ")
    print()


# ==================================================
# Q3. Print a number triangle, skipping even numbers.
# ==================================================

# Expected Output:
# 1
# 1 3
# 1 3 5
# 1 3 5 7

for i in range(1, 5):
    for j in range(1, i * 2):
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()


# ==================================================
# Q4. Print an increasing star pattern, but stop after 4 rows.
# ==================================================

# Expected Output:
# *
# * *
# * * *
# * * * *

for i in range(1, 7):
    if i > 4:
        break

    print("* " * i)


# ==================================================
# Q5. Print a number pattern, skipping multiples of 3.
# ==================================================

# Expected Output:
# 1
# 1 2
# 1 2
# 1 2 4
# 1 2 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 3 == 0:
            continue
        print(j, end=" ")
    print()


# ==================================================
# Q6. Print a square star pattern, but skip the middle row.
# ==================================================

# Expected Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(1, 6):
    if i == 3:
        continue

    for j in range(5):
        print("*", end=" ")
    print()


# ==================================================
# Q7. Print a triangle pattern, skipping even-numbered rows.
# ==================================================

# Expected Output:
# *
# * * *
# * * * * *

for i in range(1, 6):
    if i % 2 == 0:
        continue

    print("* " * i)


# ==================================================
# Q8. Print numbers in a triangle, but stop when the number reaches 6.
# ==================================================

# Expected Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, 10):
        if j == 6:
            break
        if j > i:
            break
        print(j, end=" ")
    print()


# ==================================================
# Q9. Print a star pattern, skipping the third star in each row.
# ==================================================

# Expected Output:
# *
# * *
# * * 
# * * * *
# * * * *

for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 3:
            continue
        print("*", end=" ")
    print()


# ==================================================
# Q10. Print a number triangle, skipping number 3 in every row.
# ==================================================

# Expected Output:
# 1
# 1 2
# 1 2
# 1 2 4
# 1 2 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 3:
            continue
        print(j, end=" ")
    print()


# ==================================================
# Q11. Print an inverted star triangle, stopping after 2 rows.
# ==================================================

# Expected Output:
# * * * * *
# * * * *

for i in range(5, 0, -1):
    if i < 4:
        break
    print("* " * i)


# ==================================================
# Q12. Print a square number pattern, skipping even numbers.
# ==================================================

# Expected Output:
# 1 3 5
# 1 3 5
# 1 3 5

for i in range(3):
    for j in range(1, 6):
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()


# ==================================================
# Q13. Print a triangle of numbers, skipping rows divisible by 3.
# ==================================================

# Expected Output:
# 1
# 1 2
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    if i % 3 == 0:
        continue

    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ==================================================
# Q14. Print a star pattern, stopping when the row contains 4 stars.
# ==================================================

# Expected Output:
# *
# * *
# * * *

for i in range(1, 6):
    if i == 4:
        break
    print("* " * i)


# ==================================================
# Q15. Print a number pattern, skipping multiples of 2 or 3.
# ==================================================

# Expected Output:
# 1
# 1
# 1
# 1
# 1 5

for i in range(1, 6):
    for j in range(1, i + 1):
        if j % 2 == 0 or j % 3 == 0:
            continue
        print(j, end=" ")
    print()


# ==========================================
# END OF DAY 09 - BREAK AND CONTINUE PATTERNS
# ==========================================
```
