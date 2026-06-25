Conditionals:

- Used to make decisions in a program
- Execute different code depending on whether a condition is True or False

Comparison operators:

- > greater than
- < less than
- >= greater than or equal to
- <= less than or equal to
- == equal to
- != not equal to

Basic if statement:

age = 21

if age >= 18:
    print("Adult")

if-else statement:

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

if-elif-else statement:

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Needs Improvement")

Shorthand if-else:

print("Adult") if age >= 18 else print("Minor")

Nested if statements:

age = 20

if age >= 18:
    if age >= 21:
        print("Can drink")
    else:
        print("Adult")

Logical operators:

and

- Both conditions must be True

Example:

age = 22

if age >= 18 and age < 65:
    print("Working age")

or

- At least one condition must be True

Example:

username = "Karl"
access_level = 3

if username == "admin" or access_level >= 4:
    print("Access granted")
else:
    print("Access denied")

not

- Reverses True and False

Example:

logged_in = False

if not logged_in:
    print("Please log in")

Important operators to memorize:

==
!=
>
<
>=
<=
and
or
not

Things I'll actually use in projects:

Weather App:

if temperature > 80:
    print("Hot outside")
else:
    print("Nice weather")

Expense Tracker:

if amount > budget:
    print("Over budget")

Contact Manager:

if name in contacts:
    print("Contact found")
else:
    print("Contact not found")

Common mistakes:

Using = instead of ==

Wrong:

if age = 18:

Correct:

if age == 18:

Remember:

- = assigns a value
- == compares two values

Indentation matters:

Correct:

if age >= 18:
    print("Adult")

Wrong:

if age >= 18:
print("Adult")

Most important concepts to memorize:

if

if...else

if...elif...else

and

or

not