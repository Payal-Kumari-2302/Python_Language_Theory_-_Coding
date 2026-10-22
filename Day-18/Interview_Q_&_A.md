# Day-18 – Python 90 Days Challenge

## Interview Questions & Answers

### Topic: Function Arguments & Advanced Parameters

**Q1. What is a Function?**
**Definition:** A function is a reusable block of code that performs a specific task.
**Example:** `def greet(): print("Hello!")`

**Q2. What are Parameters?**
**Definition:** Parameters are variables defined in a function to receive values.
**Example:** `def greet(name): print(name)`

**Q3. What are Arguments?**
**Definition:** Arguments are actual values passed to a function when it is called.
**Example:** `greet("Payal")`

**Q4. What are Positional Arguments?**
**Definition:** Positional arguments pass values according to the order of parameters.
**Example:** `student("Payal", 21)`

**Q5. What is a Return Value?**
**Definition:** The `return` statement sends a result back to the caller.
**Example:** `return a + b`

**Q6. Can a Function Return Multiple Values?**
**Definition:** Yes, a function can return multiple values, usually as a tuple.
**Example:** `return 10, 20`

**Q7. What are Default Parameters?**
**Definition:** Default parameters have predefined values used when an argument is not provided.
**Example:** `def greet(name="Payal"): print(name)`

**Q8. What are Keyword Arguments?**
**Definition:** Keyword arguments pass values using parameter names.
**Example:** `student(name="Payal", age=21)`

**Q9. What is `*args`?**
**Definition:** `*args` accepts multiple positional arguments and stores them in a tuple.
**Example:** `def show(*args): print(args)`

**Q10. What is `**kwargs`?**
**Definition:** `**kwargs` accepts multiple keyword arguments and stores them in a dictionary.
**Example:** `def show(**kwargs): print(kwargs)`

**Q11. Differentiate Between `*args` and `**kwargs`.**
**Definition:** `*args` collects positional arguments into a tuple, whereas `**kwargs` collects keyword arguments into a dictionary.
**Example:** `show(10, 20)` and `show(name="Payal")`

**Q12. What is Function Parameter Order?**
**Definition:** It is the order in which different types of parameters are written in a function.
**Example:** `def show(name, age=18, *args, **kwargs): pass`

**Q13. What is a Docstring?**
**Definition:** A docstring describes the purpose of a function.
**Example:** `"""Return the sum of two numbers."""`

**Q14. What are Function Naming Rules?**
**Definition:** Function names should be meaningful, follow Python naming rules, and avoid Python keywords.
**Example:** `def calculate_sum(): pass`
