# Python 90 Days Challenge

# Day-21: Interview Questions & Answers

## Topic: Modules and Packages in Python

### Q1. What is a Module?

**Definition:** A module is a Python file containing reusable code.

**Real-World Example:** A `calculator.py` file contains functions for addition and subtraction that can be reused in other files.

### Q2. What is a Package?

**Definition:** A package is a folder that contains multiple Python modules.

**Real-World Example:** A college management system can organize student, teacher, and attendance modules inside a package.

### Q3. Why Do We Use Modules and Packages?

**Definition:** Modules and packages help organize code, reuse logic, and avoid repetition.

**Real-World Example:** A college management application can be divided into student, teacher, and attendance modules.

### Q4. What Is Importing in Python?

**Definition:** Importing means using code from another module.

**Real-World Example:** Importing the `math` module to perform mathematical calculations.

```python
import math

print(math.sqrt(25))
```

**Output:**

```text
5.0
```

### Q5. What Are the Different Ways to Import a Module?

**Definition:** Python provides different import styles to access modules and their members.

**Real-World Example:** Importing an entire module or importing only the required function.

```python
import math
import math as m
from math import sqrt
from math import sqrt, pow
from math import *
```

**Interview Point:** Avoid `from module import *` in large programs because it can cause name conflicts.

### Q6. What Is a Standard Library Module?

**Definition:** A standard library module is included with Python and does not require separate installation.

**Real-World Example:** Using the `datetime` module to get the current date and time.

**Important Modules:**

* `math` — Mathematical operations
* `random` — Random values
* `datetime` — Date and time
* `os` — Operating system tasks
* `sys` — Python runtime information
* `json` — Working with JSON data
* `statistics` — Basic statistics

### Q7. How Can You Create Your Own Module?

**Definition:** Any Python file can be used as a module by importing it into another Python file.

**Real-World Example:** Creating calculator functions in one file and using them in another file.

**calculator.py**

```python
def add(a, b):
    return a + b
```

**main.py**

```python
import calculator

result = calculator.add(10, 20)
print(result)
```

**Output:**

```text
30
```

### Q8. How Can You Import a Specific Function from a Module?

**Definition:** The `from ... import ...` statement imports a specific function or object from a module.

**Real-World Example:** Importing only the addition function from a calculator module.

```python
from calculator import add

print(add(10, 20))
```

**Output:**

```text
30
```

### Q9. What Is the Module Search Path?

**Definition:** The module search path contains locations where Python searches for imported modules.

**Real-World Example:** When you write `import calculator`, Python searches its module locations to find the file.

**General Search Order:**

1. Current working directory
2. Paths listed in `PYTHONPATH`, if set
3. Standard library directories
4. Installed third-party package directories

### Q10. What Is the `dir()` Function?

**Definition:** The `dir()` function shows the names available inside a module or object.

**Real-World Example:** A developer can inspect the names available in the `math` module.

```python
import math

print(dir(math))
```

**Output:** A list of names available inside the `math` module.

### Q11. What Is `__name__ == "__main__"`?

**Definition:** It checks whether a Python file is being run directly rather than imported as a module.

**Real-World Example:** Running calculator test code directly while preventing it from running automatically when the module is imported.

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

**Output when run directly:**

```text
30
```

### Q12. What Is `__init__.py`?

**Definition:** `__init__.py` is a special file used in Python packages. It can contain package initialization code.

**Real-World Example:** A calculator package can use `__init__.py` to expose functions at the package level.

**Package Structure:**

```text
mypackage/
    __init__.py
    calculator.py
    messages.py
```

### Q13. What Is the Difference Between Absolute and Relative Imports?

**Definition:**

* **Absolute Import:** Imports code using the full path from the project or package root.
* **Relative Import:** Imports code based on the current module's location.

**Real-World Example:** Importing an addition function from `calculator.py` into `reports.py`.

**Absolute Import:**

```python
from app.calculator import add
```

**Relative Import:**

```python
from .calculator import add
```

### Q14. What Is Package Management?

**Definition:** Package management means installing, updating, removing, and tracking Python packages.

**Real-World Example:** Installing and managing libraries required by a data analysis project.

### Q15. What Is pip?

**Definition:** `pip` is Python's package installer.

**Real-World Example:** Installing the `requests` package to send HTTP requests.

**Check pip Version:**

```bash
python -m pip --version
```

**Install a Package:**

```bash
python -m pip install requests
```

**Upgrade a Package:**

```bash
python -m pip install --upgrade requests
```

**Uninstall a Package:**

```bash
python -m pip uninstall requests
```

**List Installed Packages:**

```bash
python -m pip list
```

### Q16. What Is a Virtual Environment?

**Definition:** A virtual environment is an isolated Python environment for a project.

**Real-World Example:** Two projects can use different versions of a library without interfering with each other.

**Create a Virtual Environment:**

```bash
python -m venv venv
```

**Activate on Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Deactivate:**

```bash
deactivate
```

### Q17. What Is `requirements.txt`?

**Definition:** `requirements.txt` stores a list of packages required by a Python project.

**Real-World Example:** Sharing a GitHub project so another developer can install its dependencies.

**Save Installed Packages:**

```bash
python -m pip freeze > requirements.txt
```

**Install Dependencies:**

```bash
python -m pip install -r requirements.txt
```

**Example Contents:**

```text
requests==2.32.3
numpy==2.0.0
```

### Q18. What Are Third-Party Packages?

**Definition:** Third-party packages are packages created by developers outside Python's standard library.

**Real-World Example:** Using `pandas` for data analysis or `Flask` for web development.

| Package    | Common Use            |
| ---------- | --------------------- |
| `requests` | Sending HTTP requests |
| `numpy`    | Numerical computing   |
| `pandas`   | Data analysis         |
| `flask`    | Web development       |
| `django`   | Web applications      |
| `pytest`   | Testing               |

### Q19. What Is a Circular Import?

**Definition:** A circular import occurs when two modules import each other.

**Real-World Example:** `student.py` imports `fees.py`, while `fees.py` also imports `student.py`.

**Example Structure:**

```text
a.py -> imports b.py
b.py -> imports a.py
```

**How to Avoid It:** Move shared logic into a separate module that both files can import.

---

## Quick Revision

| No. | Topic                    | Short Definition                               |
| --: | ------------------------ | ---------------------------------------------- |
|   1 | Module                   | A Python file containing reusable code         |
|   2 | Package                  | A folder containing Python modules             |
|   3 | Importing                | Using code from another module                 |
|   4 | Standard Library         | Modules included with Python                   |
|   5 | `dir()`                  | Shows available names                          |
|   6 | `__name__ == "__main__"` | Checks whether a file runs directly            |
|   7 | `__init__.py`            | A special package file                         |
|   8 | Absolute Import          | Uses the full module path                      |
|   9 | Relative Import          | Uses the current module's location             |
|  10 | `pip`                    | Python's package installer                     |
|  11 | Virtual Environment      | An isolated project environment                |
|  12 | `requirements.txt`       | Lists project dependencies                     |
|  13 | Third-Party Package      | A package created outside the standard library |
|  14 | Circular Import          | Two modules importing each other               |

---

**Revision Goal:** Understand all 19 questions, practise the code examples, and explain the real-world examples in your own words.
