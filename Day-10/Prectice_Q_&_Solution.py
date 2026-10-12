# Python 90 Days Challenge

# Day 10 - Practice Questions & Solutions

# Python 90 Days Challenge

# Day 10 - Practice

# Q1. Demonstrate the use of the pass statement in a loop.

# Q2. Write a program using the else block with a for loop.

# Q3. Write a program to demonstrate that loop else does not execute after break.

# Q4. Print the following star pattern using nested loops.

# Q5. Print numbers from 10 to 1 using range().

# Q6. Print multiples of 5 from 1 to 50 using range().

# Q7. Print each character of a string with its index using enumerate().

# Q8. Print list elements with index numbers starting from 1 using enumerate().

# Q9. Print names and marks together using zip().

# Q10. Demonstrate zip() with two lists of different lengths.

# Q11. Demonstrate the use of iter() and next().

# Q12. Handle StopIteration using try-except.

# Q13. Find common elements in two lists using nested loops.

# Q14. Display names and marks with index numbers using enumerate() and zip().

# Q15. Write a while loop that stops when a condition becomes False.

# Q16. Write a program to demonstrate a controlled loop that avoids becoming infinite.

# ==========================================

# PRACTICE INSTRUCTION

# ==========================================

# First, try to solve all the questions yourself.

# Do not look at the solution immediately.

# If you cannot solve a question, check the solution

# and understand the logic before moving forward.

# ==================================================

# Q1. Demonstrate the use of the pass statement in a loop.

# ==================================================

for i in range(1, 6):
if i == 3:
pass
print(i)

# ==================================================

# Q2. Write a program using the else block with a for loop.

# ==================================================

for i in range(1, 6):
print(i)
else:
print("Loop completed")

# ==================================================

# Q3. Demonstrate that loop else does not execute after break.

# ==================================================

for i in range(1, 6):
if i == 3:
break
print(i)
else:
print("Loop completed")

# ==================================================

# Q4. Print a star pattern using nested loops.

# ==================================================

for i in range(1, 5):
for j in range(i):
print("*", end=" ")
print()

# ==================================================

# Q5. Print numbers from 10 to 1 using range().

# ==================================================

for i in range(10, 0, -1):
print(i)

# ==================================================

# Q6. Print multiples of 5 from 1 to 50 using range().

# ==================================================

for i in range(5, 51, 5):
print(i)

# ==================================================

# Q7. Print each character with its index using enumerate().

# ==================================================

text = "Python"

for index, char in enumerate(text):
print(index, char)

# ==================================================

# Q8. Print list elements with index numbers starting from 1.

# ==================================================

fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits, start=1):
print(index, fruit)

# ==================================================

# Q9. Print names and marks together using zip().

# ==================================================

names = ["Aman", "Riya", "Rahul"]
marks = [85, 90, 78]

for name, mark in zip(names, marks):
print(name, mark)

# ==================================================

# Q10. Demonstrate zip() with lists of different lengths.

# ==================================================

names = ["Aman", "Riya", "Rahul"]
marks = [85, 90]

for name, mark in zip(names, marks):
print(name, mark)

# ==================================================

# Q11. Demonstrate the use of iter() and next().

# ==================================================

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# ==================================================

# Q12. Handle StopIteration using try-except.

# ==================================================

numbers = [10, 20]

iterator = iter(numbers)

try:
print(next(iterator))
print(next(iterator))
print(next(iterator))
except StopIteration:
print("No more items")

# ==================================================

# Q13. Find common elements using nested loops.

# ==================================================

list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]

for i in list1:
for j in list2:
if i == j:
print(i)

# ==================================================

# Q14. Display names and marks with index numbers.

# ==================================================

names = ["Aman", "Riya", "Rahul"]
marks = [85, 90, 78]

for index, (name, mark) in enumerate(zip(names, marks), start=1):
print(index, name, mark)

# ==================================================

# Q15. Write a while loop that stops when a condition becomes False.

# ==================================================

i = 1

while i <= 5:
print(i)
i += 1

# ==================================================

# Q16. Demonstrate a controlled loop that avoids becoming infinite.

# ==================================================

count = 1

while True:
print(count)

```
if count == 5:
    break

count += 1
```
