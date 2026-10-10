```python
# Python 90 Days Challenge
# Day 08 - Pattern Matching
# Practice Questions & Solutions


# ==================================================
# PRACTICE QUESTIONS WITH OUTPUT
# ==================================================

# Q1. Print a square star pattern.
#
# Output:
# * * * *
# * * * *
# * * * *
# * * * *


# Q2. Print a right-angled triangle star pattern.
#
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


# Q3. Print an inverted right-angled triangle.
#
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *


# Q4. Print an increasing star pattern without spaces.
#
# Output:
# *
# **
# ***
# ****
# *****


# Q5. Print a right-aligned triangle.
#
# Output:
#     *
#    **
#   ***
#  ****
# *****


# Q6. Print a pyramid star pattern.
#
# Output:
#     *
#    ***
#   *****
#  *******
# *********


# Q7. Print an inverted pyramid pattern.
#
# Output:
# *********
#  *******
#   *****
#    ***
#     *


# Q8. Print a hollow square pattern.
#
# Output:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *


# Q9. Print an increasing number triangle.
#
# Output:
# 1
# 12
# 123
# 1234
# 12345


# Q10. Print the same number in each row.
#
# Output:
# 1
# 22
# 333
# 4444
# 55555


# Q11. Print Floyd's triangle.
#
# Output:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


# Q12. Print an inverted number triangle.
#
# Output:
# 12345
# 1234
# 123
# 12
# 1


# Q13. Print the same number five times in each row.
#
# Output:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5


# Q14. Print a binary number pattern.
#
# Output:
# 1
# 01
# 101
# 0101
# 10101


# Q15. Print a diamond star pattern.
#
# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


# ==================================================
# PRACTICE INSTRUCTIONS
# ==================================================

# 1. Read each question carefully.
# 2. Try to solve the questions before checking the solutions.
# 3. Use nested loops when rows and columns are required.
# 4. Use print("*", end=" ") to print on the same line.
# 5. Use print() to move to the next line.
# 6. Understand how spaces and stars create a pattern.
# 7. Practise changing the number of rows.
# 8. Understand the logic instead of memorizing the code.


# ==================================================
# SOLUTIONS
# ==================================================


# Q1. Square Star Pattern

for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()


# Q2. Right-Angled Triangle

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# Q3. Inverted Right-Angled Triangle

for i in range(5, 0, -1):
    print("* " * i)


# Q4. Increasing Star Pattern Without Spaces

for i in range(1, 6):
    print("*" * i)


# Q5. Right-Aligned Triangle

n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


# Q6. Pyramid Star Pattern

n = 5

for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


# Q7. Inverted Pyramid Pattern

n = 5

for i in range(n, 0, -1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


# Q8. Hollow Square Pattern

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Q9. Increasing Number Triangle

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q10. Same Number in Each Row

for i in range(1, 6):
    print(str(i) * i)


# Q11. Floyd's Triangle

num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# Q12. Inverted Number Triangle

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Q13. Repeat the Same Number Five Times

for i in range(1, 6):
    for j in range(5):
        print(i, end=" ")
    print()


# Q14. Binary Number Pattern

for i in range(1, 6):
    for j in range(i):
        print((i + j) % 2, end="")
    print()


# Q15. Diamond Star Pattern

n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# ==================================================
# END OF DAY 08 - PATTERN MATCHING
# ==================================================
```

