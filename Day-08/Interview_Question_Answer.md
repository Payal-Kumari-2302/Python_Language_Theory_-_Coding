# 🐍 Python Loops — Interview Questions for Freshers

## 1. What is a Loop in Python?

**Definition:** A loop is used to execute a block of code repeatedly.

**Real-World Example:** Checking attendance of every student in a class.

```python
for i in range(1, 6):
    print(i)
```

## 2. What Are the Different Types of Loops in Python?

**Definition:** Python has two main loops: `for` loop and `while` loop.

* **For Loop:** Used to iterate over a sequence.
* **While Loop:** Used to repeat code while a condition is True.

**Real-World Example:** Reading a list of students (`for`) or studying until the exam syllabus is complete (`while`).

## 3. What Is the Difference Between a For Loop and a While Loop?

**Definition:**

* **For Loop:** Used when iterating over a sequence or a known range.
* **While Loop:** Used when repetition depends on a condition.

**Real-World Example:** Printing 10 student names (`for`) or waiting until a bus arrives (`while`).

## 4. What Is the Syntax of a For Loop?

**Definition:** A `for` loop executes code for each item in an iterable.

**Syntax:**

```python
for variable in sequence:
    # Code to execute
```

**Real-World Example:** Printing each item in a shopping list.

```python
items = ["Milk", "Bread", "Rice"]

for item in items:
    print(item)
```

## 5. What Is the Syntax of a While Loop?

**Definition:** A `while` loop executes code as long as a condition is True.

**Syntax:**

```python
while condition:
    # Code to execute
```

**Real-World Example:** Counting attempts until a user reaches three attempts.

```python
attempt = 1

while attempt <= 3:
    print(attempt)
    attempt += 1
```

## 6. What Is the Use of the range() Function?

**Definition:** The `range()` function generates a sequence of integers.

**Real-World Example:** Generating roll numbers from 1 to 5.

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```text
1
2
3
4
5
```

## 7. What Are the Parameters of the range() Function?

**Definition:** The `range()` function accepts three parameters: `start`, `stop`, and `step`.

* `start`: Starting number (default: 0).
* `stop`: Ending limit (excluded).
* `step`: Difference between numbers (default: 1).

**Real-World Example:** Printing even numbers from 2 to 10.

```python
for i in range(2, 11, 2):
    print(i)
```

## 8. What Is an Infinite Loop?

**Definition:** An infinite loop continues running because its termination condition is never reached.

**Real-World Example:** A digital clock continuously updating the time while it is running.

```python
while True:
    print("Clock is running")
    break
```

*Note: The `break` statement stops this demonstration after one iteration.*

## 9. What Is a Nested Loop?

**Definition:** A nested loop is a loop inside another loop.

**Real-World Example:** Checking every seat in each row of a classroom.

```python
for row in range(1, 3):
    for seat in range(1, 4):
        print(row, seat)
```

## 10. Can We Use an else Statement with a Loop in Python?

**Definition:** Yes. The `else` block executes when a loop finishes normally without being terminated by `break`.

**Real-World Example:** Displaying a message when all products have been checked.

```python
for i in range(3):
    print("Checking product")

else:
    print("All products checked")
```

## 11. What Is the Difference Between break and continue?

**Definition:**

* `break`: Terminates the loop immediately.
* `continue`: Skips the current iteration and moves to the next one.

**Real-World Example:** Stop checking items (`break`) or skip an unavailable item (`continue`).

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

## 12. What Is the Use of the pass Statement in Loops?

**Definition:** The `pass` statement does nothing. It is used as a placeholder when code is required syntactically but has not been implemented yet.

**Real-World Example:** Creating a structure for a feature that will be developed later.

```python
for i in range(3):
    pass
```

## 13. Can a For Loop Iterate Over a String?

**Definition:** Yes. A `for` loop can access each character of a string one by one.

**Real-World Example:** Checking each character in a username.

```python
for char in "Python":
    print(char)
```

## 14. Can We Use a While Loop Without an else Statement?

**Definition:** Yes. The `else` statement is optional in a `while` loop.

**Real-World Example:** Counting down before a presentation starts.

```python
count = 3

while count > 0:
    print(count)
    count -= 1
```

## 15. When Should We Use a For Loop Instead of a While Loop?

**Definition:** Use a `for` loop when iterating over a sequence or a known range of items.

**Real-World Example:** Calculating the total price of products in a shopping cart.

```python
prices = [100, 200, 300]
total = 0

for price in prices:
    total += price

print("Total:", total)
```

**Output:**

```text
Total: 600
```

---

## 📌 Quick Revision

| Topic         | Key Point                              |
| ------------- | -------------------------------------- |
| Loop          | Repeats a block of code                |
| For Loop      | Iterates over a sequence               |
| While Loop    | Repeats while a condition is True      |

