Lists:

- Ordered collection of items
- Mutable (can be modified)
- Allows duplicate values
- Can store different data types

Creating lists:

- [] creates an empty list
- list() creates an empty list

Examples:

fruits = ["banana", "orange", "mango"]
empty_list = []

Useful functions:

- len() = number of items in a list

Accessing list items:

- list[0] = first item
- list[1] = second item
- list[-1] = last item
- list[-2] = second-to-last item

Examples:

fruits[0]
fruits[-1]

Slicing:

- list[start]
- Start included
- End excluded

Examples:

fruits[1:3]
fruits[:2]
fruits[1:]
fruits[::-1]  # reverse list

Modifying lists:

fruits[0] = "apple"

Checking if an item exists:

"banana" in fruits

Returns:

- True
- False

Adding items:

- append() = add to end of list
- insert(index, item) = add at specific position

Examples:

fruits.append("apple")
fruits.insert(1, "apple")

Removing items:

- remove(item) = removes first occurrence
- pop() = removes last item
- pop(index) = removes item at index
- del = deletes item or list entirely
- clear() = empties list

Examples:

fruits.remove("banana")
fruits.pop()
fruits.pop(0)
del fruits[0]
fruits.clear()

Copying lists:

fruits_copy = fruits.copy()

Use copy() if you want a separate copy.

Combining lists:

- creates a new combined list
- extend() adds one list into another

Examples:

list3 = list1 + list2

list1.extend(list2)

Useful list methods:

- count() = counts occurrences
- index() = finds first index
- reverse() = reverses list
- sort() = sorts original list
- sorted() = returns sorted copy

Examples:

fruits.count("orange")

fruits.index("orange")

fruits.reverse()

fruits.sort()

sorted(fruits)

Methods to memorize:

- append()
- insert()
- remove()
- pop()
- clear()
- copy()
- count()
- index()
- reverse()
- sort()

Things I'll use in projects:

- append()
- remove()
- pop()
- len()
- loops with lists
- indexing
- slicing