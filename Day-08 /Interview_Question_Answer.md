# Python 90 Days Challenge

# Day 08 – Interview Questions & Answers

## Topic: Loops (For Loop & While Loop)

### Q1. What is a loop in Python?

**Definition:** A loop executes a block of code repeatedly.

**Purpose:** To avoid writing the same code multiple times.

**Example:**

```python
for i in range(1, 4):
    print(i)
```

**Output:** `1 2 3`

### Q2. What is a for loop? Explain its working.

**Definition:** A `for` loop iterates over a sequence, such as a string or a range of numbers.

**Purpose:** To process each item in a sequence.

**Example:**

```python
for char in "Hi":
    print(char)
```

**Output:** `H I`

**Working:** It takes one character at a time and stops when all characters have been processed.

### Q3. What is a while loop? Explain its working.

**Definition:** A `while` loop executes code as long as its condition is `True`.

**Purpose:** To repeat code until a condition becomes `False`.

**Example:**

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

**Output:** `1 2 3`

**Working:** Python checks the condition before each iteration. The loop stops when the condition becomes `False`.

### Q4. What is the difference between a for loop and a while loop?

**Definition:**

* **For Loop:** Iterates over a sequence.
* **While Loop:** Repeats while a condition is `True`.

**Purpose:**

* **For Loop:** Used to iterate over a sequence or range.
* **While Loop:** Used when repetition depends on a condition.

**Example:**

```python
# For loop
for i in range(1, 4):
    print(i)

# While loop
number = 1
while number <= 3:
    print(number)
    number += 1
```

**Key Difference:** A `for` loop stops when the sequence is exhausted, while a `while` loop stops when its condition becomes `False`.

### Q5. What is the purpose of range() in Python?

**Definition:** The `range()` function generates a sequence of numbers.

**Purpose:** To iterate over a specified range of numbers.

**Example:**

```python
for i in range(1, 5):
    print(i)
```

**Output:** `1 2 3 4`

**Note:** The ending value `5` is excluded.

### Q6. When does a while loop stop?

**Definition:** A `while` loop stops when its condition becomes `False`.

**Purpose:** The condition determines how long the loop runs.

**Example:**

```python
number = 1

while number <= 2:
    print(number)
    number += 1
```

**Output:** `1 2`

### Q7. What is an infinite loop?

**Definition:** An infinite loop continues running because its stopping condition is never reached.

**Purpose:** It can be used for continuous operations when an appropriate stopping mechanism is provided.

**Example:**

```python
while True:
    print("Hello")
```

**Note:** This loop continues until it is interrupted.

### Q8. Why should we update a variable inside a while loop?

**Definition:** Updating a variable means changing its value during loop execution.

**Purpose:** To help the loop reach its stopping condition and avoid an unintended infinite loop.

**Example:**

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

**Output:** `1 2 3`

### Q9. Can a for loop iterate over a string?

**Definition:** Yes, a `for` loop can process a string one character at a time.

**Purpose:** To access or process individual characters.

**Example:**

```python
for char in "Code":
    print(char)
```

**Output:** `C o d e`

### Q10. Why is indentation important in loops?

**Definition:** Indentation is the whitespace at the beginning of a line that defines a block of code in Python.

**Purpose:** It identifies which statements belong to the loop body.

**Example:**

```python
for i in range(3):
    print(i)
```

**Output:** `0 1 2`

**Note:** The `print()` statement is indented, so it belongs to the loop.

---

## Quick Revision

* **Loop:** Repeats a block of code.
* **For Loop:** Iterates over a sequence.
* **While Loop:** Runs while a condition is `True`.
* **range():** Generates a sequence of numbers.
* **Stopping Condition:** Determines when a loop ends.
* **Infinite Loop:** Continues without reaching a stopping condition.
* **Variable Update:** Helps a loop progress toward termination.
* **String Iteration:** Processes characters one by one.
* **Indentation:** Defines the loop body.

**Day:** 08 / 90
**Topic:** Loops – For Loop and While Loop
**Level:** Fresher / Beginner
