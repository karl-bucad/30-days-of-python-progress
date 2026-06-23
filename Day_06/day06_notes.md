Tuples:

- Ordered collection of items
- Immutable (cannot be changed after creation)
- Allows duplicate values
- Can store different data types
- Uses parentheses ()

Examples:

fruits = ("banana", "orange", "mango")

Creating tuples:

empty_tuple = ()

or

empty_tuple = tuple()

Length of a tuple:

len(fruits)

Accessing tuple items:

- tuple[0] = first item
- tuple[1] = second item
- tuple[-1] = last item
- tuple[-2] = second-to-last item

Examples:

fruits[0]
fruits[-1]

Slicing tuples:

- tuple[start]
- Start included
- End excluded

Examples:

fruits[1:3]
fruits[:2]
fruits[1:]
fruits[-3:-1]

Checking if an item exists:

"banana" in fruits

Returns:

- True
- False

Important:

- Tuples cannot be modified

This will cause an error:

fruits[0] = "apple"

Error:

TypeError: 'tuple' object does not support item assignment

Changing a tuple to a list:

fruits = ("banana", "orange", "mango")

fruits = list(fruits)

fruits[0] = "apple"

Changing a list back to a tuple:

fruits = tuple(fruits)

Joining tuples:

- Use + operator

Example:

tuple1 = ("a", "b")
tuple2 = ("c", "d")

tuple3 = tuple1 + tuple2

Useful tuple methods:

count()

- Counts occurrences of an item

Example:

numbers = (1, 2, 2, 3)

numbers.count(2)

Output:

2

index()

- Finds the index of the first occurrence

Example:

fruits.index("orange")

Output:

1

Deleting a tuple:

del fruits

Important differences between lists and tuples:

List:

- Uses []
- Mutable
- append()
- insert()
- remove()

Tuple:

- Uses ()
- Immutable
- No append()
- No insert()
- No remove()

Things I'll actually use in projects:

- Creating tuples
- Accessing items with indexes
- Using in
- Converting tuple ↔ list

Most projects will use lists much more often than tuples.