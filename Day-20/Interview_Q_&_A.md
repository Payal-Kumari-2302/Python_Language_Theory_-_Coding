# Python 90 Days Challenge

## Day-20: Python Interview Questions for BCA Freshers

### 1. Recursion

**Q1. What is recursion?**
**Definition:** Recursion is a process in which a function calls itself.
**Example:**

```python
def show(n):
    if n == 0:
        return
    print(n)
    show(n - 1)

show(3)
```

**Q2. What is a base case in recursion?**
**Definition:** A base case is the condition that stops a recursive function.
**Example:**

```python
if n == 0:
    return
```

**Q3. What are the advantages of recursion?**
**Answer:** Recursion can make problems such as factorial and tree traversal easier to solve.

**Q4. What is the difference between recursion and iteration?**
**Answer:** Recursion uses function calls, while iteration uses loops such as `for` and `while`.

### 2. Nested Functions

**Q5. What is a nested function?**
**Definition:** A function defined inside another function is called a nested function.
**Example:**

```python
def outer():
    def inner():
        print("Hello")
    inner()

outer()
```

**Q6. Can an inner function access variables of an outer function?**
**Answer:** Yes. An inner function can access variables defined in its enclosing function.
**Example:**

```python
def outer():
    message = "Hello"
    def inner():
        print(message)
    inner()

outer()
```

**Q7. Why do we use nested functions?**
**Answer:** They help organize code and keep helper functions within the function where they are needed.

### 3. Closures

**Q8. What is a closure in Python?**
**Definition:** A closure is an inner function that remembers variables from its enclosing scope, even after the outer function has finished.
**Example:**

```python
def outer():
    message = "Hello"
    def inner():
        print(message)
    return inner

func = outer()
func()
```

**Q9. What is the main use of a closure?**
**Answer:** Closures allow a function to retain access to variables from its enclosing scope.

### 4. Function Annotations

**Q10. What are function annotations?**
**Definition:** Function annotations provide information about the expected parameter types and return value.
**Example:**

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
```

**Q11. Do function annotations enforce data types automatically?**
**Answer:** No. Python does not automatically enforce annotated types at runtime.

**Q12. What does the `->` symbol mean in Python?**
**Answer:** It introduces the return-value annotation in a function definition.
**Example:**

```python
def square(n: int) -> int:
    return n * n
```

### 5. Higher-Order Functions

**Q13. What is a higher-order function?**
**Definition:** A higher-order function accepts another function as an argument or returns a function.
**Example:**

```python
def square(n):
    return n * n

def calculate(func, value):
    return func(value)

print(calculate(square, 4))
```

**Q14. Name three built-in higher-order functions in Python.**
**Answer:** `map()`, `filter()`, and `sorted()` can accept a function or key function. `reduce()` is also commonly used for this purpose but is available through the `functools` module.

**Q15. Why are higher-order functions useful?**
**Answer:** They help make code reusable and allow functions to be passed as arguments.

---

## BCA Fresher Interview Tip

For a fresher interview, prepare each answer in this order:

1. Give a short definition.
2. Explain the concept in one sentence.
3. Write a small example if asked.
4. Explain the output in simple words.
