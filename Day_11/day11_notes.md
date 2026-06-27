Functions
- Functions are reusable blocks of code that perform a specific task.
- Use the `def` keyword to define a function.
- A function's code only runs when it is called.

Basic function syntax:
```python
def function_name():
    # code
```

Call a function:
```python
function_name()
```

Functions without parameters:
- Do not require any input.
- Can perform a task and optionally return a value.

Functions with parameters:
- Parameters allow you to pass information into a function.
- Arguments are the actual values passed when calling the function.

Example:
```python
def greet(name):
    return f"Hello, {name}"
```

Functions with multiple parameters:
- Functions can take two or more parameters.

Example:
```python
def add_numbers(x, y):
    return x + y
```

Return statement:
- `return` sends a value back to where the function was called.
- A function stops executing once it reaches `return`.
- If no `return` statement is used, the function returns `None`.

Functions can return:
- Strings
- Integers
- Floats
- Booleans
- Lists
- Tuples
- Dictionaries
- Any other Python object

Default parameters:
- Parameters can have default values.
- If no argument is provided, the default value is used.

Example:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")
```

Keyword arguments:
- Arguments can be passed by parameter name.
- Order does not matter.

Example:
```python
add_numbers(y=5, x=3)
```

Arbitrary number of arguments (`*args`):
- Use `*args` when you don't know how many positional arguments will be passed.
- `args` is stored as a tuple.

Example:
```python
def add_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
```

Arbitrary named arguments (`**kwargs`):
- Use `**kwargs` when accepting an unknown number of keyword arguments.
- `kwargs` is stored as a dictionary.

Example:
```python
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
```

Dictionary unpacking:
- Use `**` to unpack a dictionary into keyword arguments.

Example:
```python
person = {"name": "Karl", "age": 21}

def introduce(name, age):
    print(name, age)

introduce(**person)
```

Functions as parameters:
- A function can be passed as an argument to another function.

Example:
```python
def square(x):
    return x ** 2

def calculate(func, num):
    return func(num)
```

Things I learned:
- `def` creates a function.
- Parameters are variables inside the function.
- Arguments are the values passed into the function.
- `return` sends a value back and immediately ends the function.
- Functions help avoid repeating code.
- `*args` collects multiple positional arguments into a tuple.
- `**kwargs` collects multiple keyword arguments into a dictionary.
- Functions can call other functions.
- Functions can be passed as arguments to other functions.