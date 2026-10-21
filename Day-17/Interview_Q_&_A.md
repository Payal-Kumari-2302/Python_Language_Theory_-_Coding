# Day-17: Python 90 Days Challenge 🐍

## Python Functions – Interview Questions & Answers

### 1. What is a Function?

**Definition:** A function is a reusable block of code that performs a specific task.

**Example:**

```python
def greet():
    print("Hello, Python!")

greet()
```

### 2. What is a Built-in Function?

**Definition:** A built-in function is already provided by Python.

**Example:**

```python
print(len("Python"))
```

**Output:** `6`

### 3. What is a User-defined Function?

**Definition:** A function created by the programmer is called a user-defined function.

**Example:**

```python
def add():
    print(10 + 20)

add()
```

**Output:** `30`

### 4. How do you define a function in Python?

**Definition:** The `def` keyword is used to define a function.

**Example:**

```python
def greet():
    print("Hello")
```

### 5. What is a Function Call?

**Definition:** A function call executes a defined function.

**Example:**

```python
def greet():
    print("Hello")

greet()
```

### 6. What is an Empty Function?

**Definition:** An empty function uses the `pass` statement when its implementation is not yet written.

**Example:**

```python
def my_function():
    pass
```

### 7. What are Parameters?

**Definition:** Parameters are variables specified in a function's definition.

**Example:**

```python
def greet(name):
    print(name)
```

Here, `name` is a parameter.

### 8. What are Arguments?

**Definition:** Arguments are values passed to a function when it is called.

**Example:**

```python
def greet(name):
    print(name)

greet("Payal")
```

**Output:** `Payal`

### 9. What are Positional Arguments?

**Definition:** Positional arguments are assigned to parameters according to their order.

**Example:**

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

**Output:** `30`

### 10. What is a Return Value?

**Definition:** A return value is the result a function sends back using the `return` statement.

**Example:**

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

**Output:** `30`

### 11. What is a Default Parameter?

**Definition:** A default parameter has a predefined value used when an argument is not provided.

**Example:**

```python
def greet(name="Payal"):
    print(name)

greet()
```

**Output:** `Payal`

### 12. What are Keyword Arguments?

**Definition:** Keyword arguments pass values to parameters using their names.

**Example:**

```python
def greet(name, age):
    print(name, age)

greet(age=21, name="Payal")
```

**Output:** `Payal 21`

### 13. What is `*args`?

**Definition:** `*args` allows a function to accept multiple positional arguments.

**Example:**

```python
def show(*args):
    print(args)

show(10, 20, 30)
```

**Output:** `(10, 20, 30)`

### 14. What is `**kwargs`?

**Definition:** `**kwargs` allows a function to accept multiple keyword arguments.

**Example:**

```python
def show(**kwargs):
    print(kwargs)

show(name="Payal", age=21)
```

**Output:** `{'name': 'Payal', 'age': 21}`

### 15. What is a Docstring?

**Definition:** A docstring describes the purpose of a function.

**Example:**

```python
def greet():
    """Display a greeting."""
    print("Hello")

print(greet.__doc__)
```

**Output:** `Display a greeting.`

### 16. What are Function Naming Rules?

**Definition:** Function names should be meaningful, follow Python's naming rules, and preferably use `snake_case`.

**Example:**

```python
def calculate_total():
    pass
```

---

## Key Takeaways

* `def` defines a function.
* Calling a function executes it.
* Parameters receive values through arguments.
* `return` sends a result back to the caller.
* `*args` accepts multiple positional arguments.
* `**kwargs` accepts multiple keyword arguments.
* Docstrings explain a function's purpose.

**Day-17 Complete!** 🚀
Learn • Practice • Grow
