```python
# Python 90 Days Challenge
# Day 09 - Break and Continue Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Print numbers from 1 to 10, but stop when the number is 6.

# Q2. Print numbers from 1 to 10, but skip the number 5.

# Q3. Print odd numbers from 1 to 20 using continue.

# Q4. Print numbers from 1 to 20, but stop when you reach 10.

# Q5. Print numbers from 1 to 15, skipping multiples of 3.

# Q6. Take 5 numbers from the user and stop if the user enters 0.

# Q7. Print numbers from 1 to 20, skipping even numbers.

# Q8. Find the first number between 1 and 100 divisible by both 7 and 9.

# Q9. Print numbers from 1 to 30, excluding numbers divisible by 2 or 3.

# Q10. Keep asking the user for numbers until a negative number is entered.

# Q11. Print the multiplication table of a number from 1 to 10, but stop at 5.

# Q12. Print numbers from 1 to 20 and stop at the first number divisible by 7.

# Q13. Print only positive numbers from a list using continue.

# Q14. Search for a number in a list and stop when the number is found.

# Q15. Print numbers from 1 to 20, skipping multiples of 4.


# ==========================================
# PRACTICE INSTRUCTIONS
# ==========================================

# 1. First, try to solve all questions yourself.
# 2. Use break to stop a loop immediately.
# 3. Use continue to skip the current iteration.
# 4. Use if conditions wherever required.
# 5. Practise both for loops and while loops.
# 6. Check the expected output carefully.
# 7. Do not copy the solution without understanding the logic.


# ==================================================
# Q1. Print numbers from 1 to 10, but stop when the number is 6.
# ==================================================

# Expected Output:
# 1
# 2
# 3
# 4
# 5

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# ==================================================
# Q2. Print numbers from 1 to 10, but skip the number 5.
# ==================================================

# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# ==================================================
# Q3. Print odd numbers from 1 to 20 using continue.
# ==================================================

# Expected Output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)


# ==================================================
# Q4. Print numbers from 1 to 20, but stop when you reach 10.
# ==================================================

# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(1, 21):
    if i == 10:
        break
    print(i)


# ==================================================
# Q5. Print numbers from 1 to 15, skipping multiples of 3.
# ==================================================

# Expected Output:
# 1
# 2
# 4
# 5
# 7
# 8
# 10
# 11
# 13
# 14

for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)


# ==================================================
# Q6. Take 5 numbers from the user and stop if the user enters 0.
# ==================================================

# Example Input:
# 4
# 7
# 2
# 0
#
# Expected Output:
# 4
# 7
# 2

for i in range(5):
    num = int(input("Enter a number: "))

    if num == 0:
        break

    print(num)


# ==================================================
# Q7. Print numbers from 1 to 20, skipping even numbers.
# ==================================================

# Expected Output:
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)


# ==================================================
# Q8. Find the first number between 1 and 100 divisible by both 7 and 9.
# ==================================================

# Expected Output:
# 63

for i in range(1, 101):
    if i % 7 == 0 and i % 9 == 0:
        print(i)
        break


# ==================================================
# Q9. Print numbers from 1 to 30, excluding multiples of 2 or 3.
# ==================================================

# Expected Output:
# 1
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 25
# 29

for i in range(1, 31):
    if i % 2 == 0 or i % 3 == 0:
        continue
    print(i)


# ==================================================
# Q10. Keep asking for numbers until a negative number is entered.
# ==================================================

# Example Input:
# 5
# 8
# 3
# -1
#
# Expected Output:
# 5
# 8
# 3

while True:
    num = int(input("Enter a number: "))

    if num < 0:
        break

    print(num)


# ==================================================
# Q11. Print the multiplication table of a number from 1 to 10, but stop at 5.
# ==================================================

# Example Input:
# 3
#
# Expected Output:
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15

num = int(input("Enter a number: "))

for i in range(1, 11):
    if i > 5:
        break

    print(f"{num} x {i} = {num * i}")


# ==================================================
# Q12. Print numbers from 1 to 20 and stop at the first number divisible by 7.
# ==================================================

# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7

for i in range(1, 21):
    print(i)

    if i % 7 == 0:
        break


# ==================================================
# Q13. Print only positive numbers from a list using continue.
# ==================================================

# Example List:
# [-2, 5, 0, 8, -1, 3]
#
# Expected Output:
# 5
# 8
# 3

numbers = [-2, 5, 0, 8, -1, 3]

for num in numbers:
    if num <= 0:
        continue
    print(num)


# ==================================================
# Q14. Search for a number in a list and stop when found.
# ==================================================

# Example:
# Numbers = [10, 20, 30, 40, 50]
# Search = 30
#
# Expected Output:
# Number found: 30

numbers = [10, 20, 30, 40, 50]
search = 30

for num in numbers:
    if num == search:
        print("Number found:", num)
        break


# ==================================================
# Q15. Print numbers from 1 to 20, skipping multiples of 4.
# ==================================================

# Expected Output:
# 1
# 2
# 3
# 5
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 15
# 17
# 18
# 19

for i in range(1, 21):
    if i % 4 == 0:
        continue
    print(i)


# ==========================================
# END OF DAY 09 - BREAK AND CONTINUE
# ==========================================
```
