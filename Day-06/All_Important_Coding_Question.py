# 🐍 Python Day 07: Control Flow

## 📌 About

This repository contains 6 important Python coding questions based on **Control Flow** using `if`, `if-else`, `elif`, and logical operators.

These programs are useful for BCA students, beginners, and placement preparation.

## 📚 Topics Covered

* `if` Statement
* `if-else` Statement
* `elif` Statement
* Comparison Operators
* Logical Operators
* Modulus Operator (`%`)

## 💻 Coding Questions

### 1. Even or Odd

Check whether a number is even or odd.

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 2. Positive, Negative, or Zero

Determine whether a number is positive, negative, or zero.

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### 3. Greater of Two Numbers

Find the greater number or check whether both numbers are equal.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number:", a)
elif b > a:
    print("Greater number:", b)
else:
    print("Both numbers are equal")
```

### 4. Greatest of Three Numbers

Find the greatest among three numbers.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)
```

### 5. Voting Eligibility

Check whether a person meets the minimum voting age requirement in India.

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

### 6. Leap Year

Check whether a year is a leap year.

```python
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

## 🎯 Learning Outcomes

* Understand conditional statements in Python.
* Apply comparison and logical operators.
* Solve basic programming problems.
* Develop problem-solving skills for placement coding rounds.

## 🛠️ Technologies Used

* **Language:** Python
* **Editor:** Visual Studio Code

## 👩‍💻 Author

BCA Student | Python Learner

---

⭐ If you find this repository helpful, consider giving it a star!
