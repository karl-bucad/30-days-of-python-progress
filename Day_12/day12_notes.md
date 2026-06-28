Modules
- A module is a Python file (`.py`) that contains variables, functions, or classes.
- Modules allow you to organize and reuse code across multiple files.

Creating a module:
- Save Python code in a `.py` file.
- Example:
```python
# mymodule.py
def generate_full_name(first_name, last_name):
    return first_name + " " + last_name
```

Importing a module:
- Use the `import` keyword.

Example:
```python
import mymodule

print(mymodule.generate_full_name("Karl", "Bucad"))
```

Importing specific functions:
- Import only what you need from a module.

Example:
```python
from mymodule import generate_full_name

print(generate_full_name("Karl", "Bucad"))
```

Renaming imports:
- Use `as` to give an imported module or function a new name.

Example:
```python
from mymodule import generate_full_name as fullname

print(fullname("Karl", "Bucad"))
```

Common built-in modules:
- math
- random
- os
- sys
- statistics
- string
- datetime
- json
- collections
- re (regular expressions)

OS module:
- Used for interacting with the operating system.

Common functions:
- `os.mkdir()` → create a folder
- `os.chdir()` → change current directory
- `os.getcwd()` → get current working directory
- `os.rmdir()` → remove a directory

Sys module:
- Gives information about the Python runtime and command-line arguments.

Useful functions:
- `sys.argv` → command-line arguments
- `sys.exit()` → exit the program
- `sys.maxsize` → largest integer supported
- `sys.path` → module search paths
- `sys.version` → current Python version

Statistics module:
- Used for statistical calculations.

Common functions:
- `mean()`
- `median()`
- `mode()`
- `stdev()`

Math module:
- Provides mathematical functions and constants.

Common functions:
- `math.pi` → π constant
- `math.sqrt(x)` → square root
- `math.pow(x, y)` → exponent
- `math.floor(x)` → round down
- `math.ceil(x)` → round up
- `math.log10(x)` → base-10 logarithm

Importing from math:
```python
from math import pi, sqrt
```

Import everything from a module:
- Use `*` to import everything (generally not recommended).

Example:
```python
from math import *
```

String module:
- Contains useful string constants.

Examples:
- `string.ascii_letters`
- `string.digits`
- `string.punctuation`

Random module:
- Used for generating random numbers.

Common functions:
- `random()` → random decimal between 0.0 and 1.0
- `randint(a, b)` → random integer between `a` and `b` (inclusive)

Example:
```python
from random import random, randint

print(random())
print(randint(1, 10))
```

Things I learned:
- Modules help organize and reuse code.
- `import` imports an entire module.
- `from module import function` imports specific functions.
- `as` renames imported modules or functions.
- `math` provides mathematical operations.
- `random` generates random numbers.
- `statistics` performs statistical calculations.
- `os` interacts with the operating system.
- `sys` provides information about the Python runtime.
- `string` contains useful predefined string constants.