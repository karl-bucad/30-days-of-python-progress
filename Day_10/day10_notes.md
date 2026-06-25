Loops:

- Used to repeat a block of code
- Two main types:
   - while loop
   - for loop

While loop:

- Repeats while a condition is True

Example:

count = 0

while count < 5:
    print(count)
    count += 1

Output:

0
1
2
3
4

while...else:

- The else block runs after the while loop finishes normally.

Example:

count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop finished")

break:

- Stops the loop immediately.

Example:

for number in range(10):
    if number == 5:
        break
    print(number)

Output:

0
1
2
3
4

continue:

- Skips the current iteration and continues with the next.

Example:

for number in range(5):
    if number == 2:
        continue
    print(number)

Output:

0
1
3
4

For loop:

- Used to loop through sequences such as:
   - Lists
   - Strings
   - Tuples
   - Dictionaries
   - Sets

Looping through a list:

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

Looping through a string:

for letter in "Python":
    print(letter)

Looping through a tuple:

numbers = (1, 2, 3)

for number in numbers:
    print(number)

Looping through a dictionary:

Keys only:

person = {
    "name": "Karl",
    "age": 21
}

for key in person:
    print(key)

Keys and values:

for key, value in person.items():
    print(key, value)

Looping through a set:

colors = {"red", "blue", "green"}

for color in colors:
    print(color)

range():

- Generates a sequence of numbers.

Basic:

range(5)

Produces:

0 1 2 3 4

Common examples:

for i in range(5):
    print(i)

Start and end:

range(1, 6)

Produces:

1 2 3 4 5

Step value:

range(0, 11, 2)

Produces:

0 2 4 6 8 10

Reverse:

range(10, 0, -2)

Produces:

10 8 6 4 2

Nested loops:

A loop inside another loop.

Example:

for i in range(3):
    for j in range(2):
        print(i, j)

Output:

0 0
0 1
1 0
1 1
2 0
2 1

for...else:

The else runs after the loop finishes normally.

Example:

for i in range(5):
    print(i)
else:
    print("Loop finished")

pass:

- Placeholder when Python expects code.

Example:

for i in range(5):
    pass

Useful loop keywords:

break
continue
pass

Common mistakes:

Infinite while loop:

Wrong:

count = 0

while count < 5:
    print(count)

Correct:

count = 0

while count < 5:
    print(count)
    count += 1

Forgetting the colon:

Wrong:

for i in range(5)

Correct:

for i in range(5):

Most important things to memorize:

while

for

range()

break

continue

pass