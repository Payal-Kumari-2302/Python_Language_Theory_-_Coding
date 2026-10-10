```python
# Python 90 Days Challenge
# Day 08 - Practice Questions & Solutions


# Q1. Print numbers from 1 to 10 using a for loop.

# Q2. Print numbers from 10 to 1 using a while loop.

# Q3. Print even numbers from 1 to 50.

# Q4. Print odd numbers from 1 to 50.

# Q5. Print the multiplication table of a number.

# Q6. Calculate the sum of first N natural numbers.

# Q7. Calculate the factorial of a number.

# Q8. Print each character of a string using a for loop.

# Q9. Count the digits of a number using a while loop.

# Q10. Reverse a number using a while loop.

# Q11. Check whether a number is prime.

# Q12. Print the Fibonacci series.

# Q13. Print a right-angled triangle star pattern.

# Q14. Use break to stop a loop when the number reaches 6.

# Q15. Use continue to skip the number 5.


# ==========================================
# PRACTICE INSTRUCTION
# ==========================================
# First, try to solve all the questions yourself.
# Do not look at the solution immediately.
# If you cannot solve a question, check the solution
# and understand the logic before moving forward.


# ==================================================
# Q1. Print numbers from 1 to 10 using a for loop.
# ==================================================

for i in range(1, 11):
    print(i)


# ==================================================
# Q2. Print numbers from 10 to 1 using a while loop.
# ==================================================

i = 10

while i >= 1:
    print(i)
    i -= 1


# ==================================================
# Q3. Print even numbers from 1 to 50.
# ==================================================

for i in range(2, 51, 2):
    print(i)


# ==================================================
# Q4. Print odd numbers from 1 to 50.
# ==================================================

for i in range(1, 51, 2):
    print(i)


# ==================================================
# Q5. Print the multiplication table of a number.
# ==================================================

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# ==================================================
# Q6. Calculate the sum of first N natural numbers.
# ==================================================

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


# ==================================================
# Q7. Calculate the factorial of a number.
# ==================================================

num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        fact *= i

    print("Factorial =", fact)


# ==================================================
# Q8. Print each character of a string using a for loop.
# ==================================================

text = input("Enter a string: ")

for character in text:
    print(character)


# ==================================================
# Q9. Count the digits of a number using a while loop.
# ==================================================

num = abs(int(input("Enter a number: ")))
count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Total digits =", count)


# ==================================================
# Q10. Reverse a number using a while loop.
# ==================================================

num = int(input("Enter a non-negative number: "))
reverse = 0

if num < 0:
    print("Please enter a non-negative number.")
else:
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    print("Reversed number =", reverse)


# ==================================================
# Q11. Check whether a number is prime.
# ==================================================

num = int(input("Enter a number: "))

if num < 2:
    print("Not a Prime Number")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")


# ==================================================
# Q12. Print the Fibonacci series.
# ==================================================

n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n < 0:
    print("Please enter a non-negative number.")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()


# ==================================================
# Q13. Print a right-angled triangle star pattern.
# ==================================================

for i in range(1, 6):
    print("*" * i)


# ==================================================
# Q14. Use break to stop when the number reaches 6.
# ==================================================

for i in range(1, 11):
    if i == 6:
        break

    print(i)


# ==================================================
# Q15. Use continue to skip the number 5.
# ==================================================

for i in range(1, 11):
    if i == 5:
        continue

    print(i)


# ==========================================
# END OF DAY 08 - PYTHON LOOPS
# ==========================================
```
