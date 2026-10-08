# 🐍 Python 90 Days Challenge

## Day 06 – Control Flow

### BCA Fresher Interview Questions

---

### 1. What is Control Flow in Python?

**Definition:** Control flow determines which statements of a program are executed.

**Purpose:** It helps a program make decisions based on conditions.

**Real-World Example:** A system checks whether a customer is eligible for a discount.

---

### 2. What is an `if` statement?

**Definition:** `if` executes a block of code when a condition is `True`.

**Purpose:** Used for decision-making when a condition needs to be checked.

**Real-World Example:** If a person is 18 or older, allow voting.

```python
if age >= 18:
    print("Eligible to vote")
```

---

### 3. What is an `if-else` statement?

**Definition:** `if-else` executes one block when the condition is `True` and another when it is `False`.

**Purpose:** Used when there are two possible outcomes.

**Real-World Example:** A student either passes or fails.

```python
if marks >= 40:
    print("Passed")
else:
    print("Failed")
```

---

### 4. What is an `elif` statement?

**Definition:** `elif` means **else if** and is used to check multiple conditions.

**Purpose:** Used when there are more than two possible conditions.

**Real-World Example:** Assigning grades based on marks.

```python
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Fail")
```

---

### 5. What happens if the condition of an `if` statement is False?

**Definition:** The indented block under `if` is skipped.

**Purpose:** It allows Python to execute code only when the condition is satisfied.

**Real-World Example:** If age is below 18, the voting code is not executed.

---

### 6. How does Python execute multiple `elif` conditions?

**Definition:** Python checks `elif` conditions from top to bottom.

**Purpose:** To execute the first condition that is `True`.

**Real-World Example:** A grading system checks Grade A first, then Grade B, then Grade C.

---

### 7. Can we use `else` with `if`?

**Definition:** Yes, an `else` block can be used with an `if` statement.

**Purpose:** It handles the case when the `if` condition is `False`.

**Real-World Example:** If login credentials are correct, allow login; otherwise, show an error.

---

### 8. What is indentation in Python?

**Definition:** Indentation means spaces at the beginning of a line to define a block of code.

**Purpose:** It tells Python which statements belong to an `if`, `else`, or `elif` block.

**Real-World Example:**

```python
if age >= 18:
    print("Eligible")
```

Here, `print()` belongs to the `if` block because it is indented.

---

### 9. What is the difference between `if` and `if-else`?

**Definition:** `if` executes code only when the condition is `True`, while `if-else` provides an alternative block when the condition is `False`.

**Purpose:** `if` is used for one possible action; `if-else` is used for two possible outcomes.

**Real-World Example:**

* `if` → Check if a person is eligible.
* `if-else` → Check whether a person is eligible or not.

---

### 10. What is the difference between `if-else` and `if-elif-else`?

**Definition:** `if-else` handles two possible outcomes, while `if-elif-else` handles multiple conditions.

**Purpose:** `elif` is useful when more than two choices are possible.

**Real-World Example:**

* `if-else` → Pass or Fail
* `if-elif-else` → Grade A, B, C, or Fail

---

### 11. Give a real-world example of `if-elif-else`.

**Definition:** It is a decision structure used to select one option from multiple conditions.

**Purpose:** To handle multiple possible outcomes.

**Real-World Example:**

```python
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

A student's grade is decided according to their marks.

---

### 12. Why are conditional statements important in Python?

**Definition:** Conditional statements allow a program to make decisions.

**Purpose:** They make programs behave differently according to different conditions.

**Real-World Example:** An ATM checks whether the entered PIN is correct before allowing a transaction.

---

## ⭐ Interview Tip

For a fresher interview, remember this simple flow:

**`if` → one condition**

**`if-else` → two outcomes**

**`if-elif-else` → multiple conditions**
