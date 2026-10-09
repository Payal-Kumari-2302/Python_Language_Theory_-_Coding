# 🐍 Python 90 Days Challenge — Day 07

## Coding Practice: Control Flow

### 📌 Topics

* Nested Conditions
* Ternary Operator
* match-case
* Truthy and Falsy Values

---

# Part 1: Coding Practice Questions

### Q1. Voting Eligibility

Write a Python program to check whether a person is eligible to vote based on their age.

### Q2. Positive, Negative, or Zero

Write a program to check whether a number is positive, negative, or zero.

### Q3. Adult or Minor Using Ternary Operator

Write a program to determine whether a person is an adult or a minor using the ternary operator.

### Q4. Check an Empty or Non-Empty String

Write a program to check whether a string is empty or non-empty using truthy and falsy values.

### Q5. Login Authentication System

Write a program that checks a username and password using nested conditions.

* Username: `admin`
* Password: `12345`
* Display an appropriate message for successful or unsuccessful login.

### Q6. Find the Largest of Three Numbers

Write a program to find the largest of three numbers using nested conditions.

### Q7. Simple Calculator Using match-case

Write a calculator program that accepts two numbers and an operator (`+`, `-`, `*`, `/`) and performs the corresponding calculation using `match-case`.

Handle invalid operators and division by zero.

### Q8. Shopping Discount Calculator

Write a program to calculate a shopping discount according to these rules:

* Amount ≥ ₹5,000: 20% discount.
* Amount ≥ ₹2,000 but < ₹5,000: 10% discount.
* Amount < ₹2,000: No discount.

Display the discount and final payable amount.

### Q9. ATM Withdrawal System

Write a program that simulates an ATM withdrawal. Check whether the withdrawal amount is positive and does not exceed the available balance. Display the remaining balance when the transaction is valid.

### Q10. Student Pass or Fail

Write a program that accepts marks for three subjects.

* Each mark must be between 0 and 100.
* The student must score at least 35 in every subject to pass.
* Display an appropriate message for invalid marks.

### Q11. Menu-Driven Program Using match-case

Create a menu-driven program with these options:

1. Check Even or Odd.
2. Check Positive or Negative.
3. Find the Square of a Number.
4. Exit.

Execute the selected operation using `match-case`.

### Q12. Truthy and Falsy Values

Given the list below, write a program to check whether each value is truthy or falsy.

```python
values = [0, 10, "", "Python", None, False, True, " "]
```

Print each value with its truthy or falsy status.

---

# Part 2: Instructions


---

# Part 3: Solutions

## Solution 1: Voting Eligibility

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

## Solution 2: Positive, Negative, or Zero

```python
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

## Solution 3: Adult or Minor Using Ternary Operator

```python
age = int(input("Enter your age: "))

status = "Adult" if age >= 18 else "Minor"

print(status)
```

## Solution 4: Check an Empty or Non-Empty String

```python
text = input("Enter a string: ")

if text:
    print("String is Not Empty")
else:
    print("String is Empty")
```

## Solution 5: Login Authentication System

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "12345":
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")
```

## Solution 6: Find the Largest of Three Numbers

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("Largest number is", largest)
```

## Solution 7: Simple Calculator Using match-case

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid Operator")
```

## Solution 8: Shopping Discount Calculator

```python
amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Payable Amount:", final_amount)
```

## Solution 9: ATM Withdrawal System

```python
balance = float(input("Enter account balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Invalid withdrawal amount")
else:
    if withdrawal <= balance:
        balance = balance - withdrawal
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
```

## Solution 10: Student Pass or Fail

```python
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

if 0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= m3 <= 100:
    if m1 >= 35 and m2 >= 35 and m3 >= 35:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid Marks")
```

## Solution 11: Menu-Driven Program Using match-case

```python
print("1. Check Even or Odd")
print("2. Check Positive or Negative")
print("3. Find Square")
print("4. Exit")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")

    case 2:
        num = float(input("Enter a number: "))
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")

    case 3:
        num = float(input("Enter a number: "))
        print("Square:", num ** 2)

    case 4:
        print("Exiting Program")

    case _:
        print("Invalid Choice")
```

## Solution 12: Truthy and Falsy Values

```python
values = [0, 10, "", "Python", None, False, True, " "]

for value in values:
    if value:
        print(repr(value), "-> Truthy")
    else:
        print(repr(value), "-> Falsy")
```

---

## 🎯 Day 07 Completion Goal

* Understand nested conditions.
* Use the ternary operator for simple decisions.
* Implement menu-driven programs using `match-case`.
* Understand truthy and falsy values.
* Solve all 12 coding questions independently.
