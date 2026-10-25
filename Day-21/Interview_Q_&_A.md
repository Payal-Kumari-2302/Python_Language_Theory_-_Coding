# Python 90 Days Challenge

# Day-21: Scope and Namespaces

## Interview Questions with Short Answers

### Q1. What is scope in Python?

**Answer:** Scope defines where a variable can be accessed in a program.

**Example:**

```python
def show():
    x = 10  # Local scope
```

### Q2. What is local scope in Python?

**Answer:** A variable created inside a function has local scope.

**Example:**

```python
def show():
    x = 5
    print(x)
```

### Q3. What is global scope in Python?

**Answer:** A variable created outside all functions has global scope.

**Example:**

```python
x = 10

def show():
    print(x)
```

### Q4. What is the difference between local and global scope?

**Answer:** Local variables are accessible inside their function, while global variables can be accessed throughout the module.

**Example:**

```python
x = 10  # Global

def show():
    y = 5  # Local
```

### Q5. What is enclosing scope in Python?

**Answer:** Enclosing scope refers to a variable in an outer function that contains an inner function.

**Example:**

```python
def outer():
    x = 10
    def inner():
        print(x)
```

### Q6. What is built-in scope in Python?

**Answer:** Built-in scope contains predefined Python names, such as `print()`, `len()`, and `sum()`.

**Example:**

```python
print(len("Python"))
```

### Q7. What is variable shadowing in Python?

**Answer:** Variable shadowing occurs when a variable in a nearer scope has the same name as one in an outer scope.

**Example:**

```python
x = 10

def show():
    x = 5
    print(x)  # 5
```

### Q8. What is the `global` keyword?

**Answer:** The `global` keyword allows a function to modify a global variable.

**Example:**

```python
x = 10

def show():
    global x
    x = 20
```

### Q9. What is the `nonlocal` keyword?

**Answer:** The `nonlocal` keyword allows an inner function to modify a variable in its enclosing function.

**Example:**

```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
```

### Q10. What is the difference between `global` and `nonlocal`?

**Answer:** `global` refers to a module-level variable, while `nonlocal` refers to a variable in an enclosing function.

### Q11. What is the LEGB rule in Python?

**Answer:** LEGB is the order Python follows to search for a name: Local, Enclosing, Global, and Built-in.

### Q12. What is a namespace in Python?

**Answer:** A namespace is a mapping between names and the objects they refer to.

**Example:**

```python
x = 10
name = "Payal"
```

### Q13. Why does Python use namespaces?

**Answer:** Namespaces organize names and help avoid naming conflicts.

### Q14. What are the main types of namespaces in Python?

**Answer:** The main types are local, enclosing, global, and built-in namespaces.

### Q15. What is the `locals()` function?

**Answer:** `locals()` returns a dictionary representing the current local namespace.

**Example:**

```python
def show():
    x = 10
    print(locals())
```

### Q16. What is the `globals()` function?

**Answer:** `globals()` returns a dictionary representing the current global namespace.

**Example:**

```python
x = 10
print(globals())
```

### Q17. What is the difference between `locals()` and `globals()`?

**Answer:** `locals()` represents the current local namespace, while `globals()` represents the module's global namespace.

### Q18. What is a `NameError` in Python?

**Answer:** A `NameError` occurs when Python cannot find the name being used.

**Example:**

```python
print(age)  # NameError if age is undefined
```

### Q19. What is an `UnboundLocalError` in Python?

**Answer:** An `UnboundLocalError` occurs when a local variable is accessed before it has been assigned a value.

**Example:**

```python
def show():
    print(x)
    x = 10
```

### Q20. What is the difference between `NameError` and `UnboundLocalError`?

**Answer:** `NameError` occurs when a name cannot be found. `UnboundLocalError` occurs when a local variable is accessed before assignment. It is a subclass of `NameError`.
