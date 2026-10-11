# Python 90 Days Challenge

# Day 09 – Interview Questions & Answers

## Topic: Break and Continue Statements

### Q1. What is the `break` statement in Python?

**Definition:** The `break` statement is used to terminate a loop immediately.

**Purpose:** To stop a loop when a particular condition is satisfied.

**Example:**

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

**Output:**

```text
1
2
3
```

**Working:** When `i` becomes `4`, the `break` statement terminates the loop.

### Q2. What is the `continue` statement in Python?

**Definition:** The `continue` statement skips the remaining code in the current iteration and moves to the next iteration.

**Purpose:** To skip specific values or conditions without terminating the entire loop.

**Example:**

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```text
1
2
4
5
```

**Working:** When `i` becomes `3`, Python skips the `print()` statement for that iteration and continues with the next iteration.

### Q3. What is the difference between `break` and `continue`?

**Definition:**

* **Break:** Terminates the entire loop.
* **Continue:** Skips the current iteration and proceeds to the next iteration.

**Purpose:**

* **Break:** Used when the loop needs to stop immediately.
* **Continue:** Used when a particular iteration needs to be skipped.

**Example:**

```python
# Break example
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# Continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output:**

```text
# Break Output
1
2

# Continue Output
1
2
4
5
```

**Key Difference:** `break` stops the loop, whereas `continue` skips only the current iteration.

### Q4. Can we use `break` inside a `while` loop?

**Definition:** Yes, the `break` statement can be used inside both `for` and `while` loops.

**Purpose:** To terminate a loop when a specific condition is met.

**Example:**

```python
number = 1

while number <= 5:
    if number == 4:
        break
    print(number)
    number += 1
```

**Output:**

```text
1
2
3
```

**Working:** When `number` becomes `4`, the `break` statement stops the loop immediately.

### Q5. Can we use `continue` inside a `while` loop?

**Definition:** Yes, the `continue` statement can be used inside a `while` loop.

**Purpose:** To skip the current iteration when a condition is satisfied.

**Example:**

```python
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)
```

**Output:**

```text
1
2
4
5
```

**Working:** When `number` becomes `3`, the `continue` statement skips the `print()` statement and moves to the next iteration.

**Important Note:** In a `while` loop, update the loop variable before `continue` when necessary. Otherwise, the condition may remain `True` indefinitely.

### Q6. Can we use `break` and `continue` together in the same loop?

**Definition:** Yes, both statements can be used in the same loop.

**Purpose:** To skip certain iterations and stop the loop when another condition is met.

**Example:**

```python
for i in range(1, 8):
    if i == 3:
        continue

    if i == 6:
        break

    print(i)
```

**Output:**

```text
1
2
4
5
```

**Working:**

* When `i` is `3`, the current iteration is skipped.
* When `i` is `6`, the loop terminates.
* The value `6` is not printed because `break` stops the loop before `print(i)` executes.

### Q7. What happens when `break` is used in a nested loop?

**Definition:** A nested loop is a loop placed inside another loop.

**Purpose:** The `break` statement terminates only the innermost loop in which it is executed.

**Example:**

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 3:
            break
        print(i, j)
```

**Output:**

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

**Working:** Whenever `j` becomes `3`, the inner loop stops. The outer loop continues with the next value of `i`.

### Q8. What is the purpose of using `break` and `continue` in Python?

**Definition:** Both are loop-control statements that change the normal flow of loop execution.

**Purpose:**

* **Break:** Stops a loop when further iterations are unnecessary.
* **Continue:** Skips iterations that do not need to be processed.

**Example:**

```python
for number in range(1, 6):
    if number == 2:
        continue

    if number == 5:
        break

    print(number)
```

**Output:**

```text
1
3
4
```

**Working:** The number `2` is skipped, and the loop stops when the number becomes `5`.

---

## Quick Revision

* **Break Statement:** Terminates the loop immediately.
* **Continue Statement:** Skips the current iteration.
* **Break in a For Loop:** Stops the `for` loop.
* **Break in a While Loop:** Stops the `while` loop.
* **Continue in a For Loop:** Moves to the next iteration.
* **Continue in a While Loop:** Returns to the condition check after skipping the remaining statements in the current iteration.
* **Nested Loop:** `break` terminates only the innermost loop where it is executed.
* **Loop Control:** `break` and `continue` change the normal flow of loop execution.
