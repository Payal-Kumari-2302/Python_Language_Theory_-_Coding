```python
# Python 90 Days Challenge
# Day 19 - Functions, Lambda, map(), filter() & reduce()
# Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Create a function named greet() that prints
#     "Hello, Python!".
#
# Q2. Store a function in another variable and call
#     the function using that variable.
#
# Q3. Create a lambda function to find the square
#     of a number.
#
# Q4. Create a lambda function to add two numbers.
#
# Q5. Use map() to find the square of each number
#     in the list [1, 2, 3, 4, 5].
#
# Q6. Use map() to convert all names to uppercase:
#     ["aman", "riya", "kabir"].
#
# Q7. Use filter() to select even numbers from:
#     [1, 2, 3, 4, 5, 6, 7, 8].
#
# Q8. Use filter() to select numbers greater than 10:
#     [5, 12, 3, 18, 7, 25].
#
# Q9. Use reduce() to calculate the sum of:
#     [1, 2, 3, 4, 5].
#
# Q10. Use reduce() to calculate the product of:
#      [1, 2, 3, 4, 5].
#
# Q11. Use map() and lambda to add 5 to each number:
#      [10, 20, 30, 40].
#
# Q12. Use filter() to select numbers divisible by 3:
#      [3, 6, 9, 12, 15, 18].
#
# Q13. Use reduce() and lambda to calculate the sum:
#      [10, 20, 30, 40].
#
# Q14. Predict the output:
#      numbers = [1, 2, 3, 4]
#      result = list(map(lambda x: x * 3, numbers))
#      print(result)
#
# Q15. Predict the output:
#      numbers = [2, 4, 5, 7, 8]
#      result = list(filter(lambda x: x % 2 == 0, numbers))
#      print(result)
#
# Q16. Predict the output:
#      from functools import reduce
#      numbers = [2, 3, 4]
#      result = reduce(lambda x, y: x + y, numbers)
#      print(result)


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================

# First, try to solve all the questions yourself.
# Do not look at the solutions immediately.
# Revise functions, lambda functions, map(),
# filter(), and reduce() if you face any difficulty.


# ==================================================
# Q1. Create a Function
# ==================================================

def greet():
    print("Hello, Python!")

greet()


# ==================================================
# Q2. Store a Function in Another Variable
# ==================================================

def welcome():
    print("Welcome to Python!")

message = welcome
message()


# ==================================================
# Q3. Square Using Lambda
# ==================================================

square = lambda x: x * x

print(square(5))


# ==================================================
# Q4. Add Two Numbers Using Lambda
# ==================================================

add = lambda a, b: a + b

print(add(10, 20))


# ==================================================
# Q5. Square Numbers Using map()
# ==================================================

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x, numbers))

print(result)


# ==================================================
# Q6. Convert Names to Uppercase Using map()
# ==================================================

names = ["aman", "riya", "kabir"]

result = list(map(lambda name: name.upper(), names))

print(result)


# ==================================================
# Q7. Filter Even Numbers
# ==================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)


# ==================================================
# Q8. Filter Numbers Greater Than 10
# ==================================================

numbers = [5, 12, 3, 18, 7, 25]

result = list(filter(lambda x: x > 10, numbers))

print(result)


# ==================================================
# Q9. Sum Using reduce()
# ==================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)


# ==================================================
# Q10. Product Using reduce()
# ==================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)


# ==================================================
# Q11. Add 5 Using map() and Lambda
# ==================================================

numbers = [10, 20, 30, 40]

result = list(map(lambda x: x + 5, numbers))

print(result)


# ==================================================
# Q12. Filter Numbers Divisible by 3
# ==================================================

numbers = [3, 6, 9, 12, 15, 18]

result = list(filter(lambda x: x % 3 == 0, numbers))

print(result)


# ==================================================
# Q13. Sum Using reduce() and Lambda
# ==================================================

from functools import reduce

numbers = [10, 20, 30, 40]

result = reduce(lambda x, y: x + y, numbers)

print(result)


# ==================================================
# Q14. Predict the Output of map()
# ==================================================

numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 3, numbers))

print(result)

# Output:
# [3, 6, 9, 12]


# ==================================================
# Q15. Predict the Output of filter()
# ==================================================

numbers = [2, 4, 5, 7, 8]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output:
# [2, 4, 8]


# ==================================================
# Q16. Predict the Output of reduce()
# ==================================================

from functools import reduce

numbers = [2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)

# Output:
# 9
```
