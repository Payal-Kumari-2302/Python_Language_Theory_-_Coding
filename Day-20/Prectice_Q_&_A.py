```python
# Python 90 Days Challenge
# Day 20 - Recursion, Nested Functions, Closures,
#          Function Annotations & Higher-Order Functions
# Practice Questions & Solutions


# ==========================================
# PRACTICE QUESTIONS
# ==========================================

# Q1. Write a recursive function to calculate
#     the factorial of a number.
#
# Q2. Write a recursive function to print numbers
#     from 1 to N.
#
# Q3. Write a recursive function to calculate
#     the sum of natural numbers from 1 to N.
#
# Q4. Write a recursive function to calculate
#     the power of a number without using **.
#
# Q5. Write a recursive function to calculate
#     the sum of digits of a positive integer.
#
# Q6. Create an outer function containing an inner
#     function that prints "Hello, Python!".
#
# Q7. Create a nested function to calculate
#     the square of a number.
#
# Q8. Create a nested function to calculate
#     the area of a rectangle.
#
# Q9. Create a closure that remembers a person's
#     name and prints a greeting.
#
# Q10. Create a closure that returns a function
#      to add a fixed number to another number.
#
# Q11. Create a closure to calculate the discounted
#      price using a given discount percentage.
#
# Q12. Write a function to add two numbers using
#      function annotations.
#
# Q13. Write a function to calculate the square
#      of a number using function annotations.
#
# Q14. Create a multiply() function with annotations
#      and print its __annotations__ attribute.
#
# Q15. Create a higher-order function that accepts
#      another function and a number as arguments.
#
# Q16. Use map() and lambda to calculate the square
#      of every number in [1, 2, 3, 4, 5].
#
# Q17. Use filter() and lambda to select even numbers
#      from [1, 2, 3, 4, 5, 6].
#
# Q18. Use map() to convert Celsius temperatures
#      into Fahrenheit.
#
# Q19. Create a higher-order function that accepts
#      a function to double a number.
#
# Q20. Use reduce() to calculate the product of
#      [1, 2, 3, 4, 5].


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================

# First, try to solve all the questions yourself.
# Then compare your code with the solutions below.
# Revise recursion, nested functions, closures,
# function annotations, and higher-order functions.


# ==================================================
# Q1. Factorial Using Recursion
# ==================================================

def factorial(n):
    if n < 0:
        return "Negative numbers are not allowed"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Output:
# 120


# ==================================================
# Q2. Print Numbers from 1 to N Using Recursion
# ==================================================

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n, end=" ")

print_numbers(5)

# Output:
# 1 2 3 4 5


# ==================================================
# Q3. Sum of Natural Numbers Using Recursion
# ==================================================

def natural_sum(n):
    if n <= 0:
        return 0
    return n + natural_sum(n - 1)

print(natural_sum(5))

# Output:
# 15


# ==================================================
# Q4. Calculate Power Using Recursion
# ==================================================

def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print(power(2, 4))

# Output:
# 16


# ==================================================
# Q5. Sum of Digits Using Recursion
# ==================================================

def digit_sum(n):
    if n < 0:
        raise ValueError("Number must be non-negative")
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))

# Output:
# 10


# ==================================================
# Q6. Create a Nested Function
# ==================================================

def outer():
    def inner():
        print("Hello, Python!")
    inner()

outer()

# Output:
# Hello, Python!


# ==================================================
# Q7. Square Using a Nested Function
# ==================================================

def calculate_square(n):
    def square():
        return n * n
    return square()

print(calculate_square(5))

# Output:
# 25


# ==================================================
# Q8. Area of Rectangle Using a Nested Function
# ==================================================

def rectangle_area(length, width):
    def calculate():
        return length * width
    return calculate()

print(rectangle_area(5, 4))

# Output:
# 20


# ==================================================
# Q9. Greeting Using a Closure
# ==================================================

def greet_person(name):
    def greet():
        print("Hello,", name + "!")
    return greet

greeting = greet_person("Payal")
greeting()

# Output:
# Hello, Payal!


# ==================================================
# Q10. Add a Fixed Number Using a Closure
# ==================================================

def make_adder(number):
    def add(value):
        return number + value
    return add

add_ten = make_adder(10)

print(add_ten(5))

# Output:
# 15


# ==================================================
# Q11. Calculate Discount Using a Closure
# ==================================================

def make_discount(discount):
    def calculate(price):
        return price - (price * discount / 100)
    return calculate

discounted_price = make_discount(10)

print(discounted_price(1000))

# Output:
# 900.0


# ==================================================
# Q12. Addition Using Function Annotations
# ==================================================

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))

# Output:
# 30


# ==================================================
# Q13. Square Using Function Annotations
# ==================================================

def square(n: int) -> int:
    return n * n

print(square(6))

# Output:
# 36


# ==================================================
# Q14. Function Annotations Attribute
# ==================================================

def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4, 5))
print(multiply.__annotations__)

# Output:
# 20
# {'a': <class 'int'>, 'b': <class 'int'>,
#  'return': <class 'int'>}


# ==================================================
# Q15. Higher-Order Function
# ==================================================

def square_number(n):
    return n * n

def calculate(func, value):
    return func(value)

print(calculate(square_number, 4))

# Output:
# 16


# ==================================================
# Q16. Square Numbers Using map() and Lambda
# ==================================================

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x, numbers))

print(result)

# Output:
# [1, 4, 9, 16, 25]


# ==================================================
# Q17. Filter Even Numbers
# ==================================================

numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

# Output:
# [2, 4, 6]


# ==================================================
# Q18. Convert Celsius to Fahrenheit Using map()
# ==================================================

celsius = [0, 10, 20, 30]

fahrenheit = list(
    map(lambda c: (c * 9 / 5) + 32, celsius)
)

print(fahrenheit)

# Output:
# [32.0, 50.0, 68.0, 86.0]


# ==================================================
# Q19. Double a Number Using a Higher-Order Function
# ==================================================

def double(n):
    return n * 2

def apply_function(func, value):
    return func(value)

print(apply_function(double, 5))

# Output:
# 10


# ==================================================
# Q20. Product Using reduce()
# ==================================================

from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)

print(result)

# Output:
# 120


# ==========================================
# END OF DAY-20 PRACTICE QUESTIONS & SOLUTIONS
# ==========================================
```
