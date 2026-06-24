Sets:

- Unordered collection of unique items
- No duplicate values allowed
- Uses {}
- Cannot access items by index
- Useful for removing duplicates

Examples:

fruits = {"banana", "orange", "mango"}

Creating sets:

empty_set = set()

Important:

{}

creates a dictionary, NOT a set.

Length of a set:

len(fruits)

Checking if an item exists:

"mango" in fruits

Returns:

- True
- False

Adding items:

add()

- Adds one item

Example:

fruits.add("lime")

update()

- Adds multiple items

Example:

fruits.update(["apple", "grape"])

Removing items:

remove()

- Removes an item
- Gives an error if item doesn't exist

Example:

fruits.remove("banana")

discard()

- Removes an item
- No error if item doesn't exist

Example:

fruits.discard("banana")

pop()

- Removes a random item

Example:

removed_item = fruits.pop()

Clearing a set:

fruits.clear()

Result:

set()

Deleting a set:

del fruits

Converting between lists and sets:

List → Set

fruits = ["apple", "banana", "apple"]

fruits = set(fruits)

Result:

{"apple", "banana"}

Duplicates are removed.

Set → List

fruits = list(fruits)

Joining sets:

union()

- Returns a new set

Example:

set1.union(set2)

or

set1 | set2

update()

- Adds one set into another

Example:

set1.update(set2)

Intersection:

intersection()

- Returns items that exist in BOTH sets

Example:

set1.intersection(set2)

or

set1 & set2

Difference:

difference()

- Returns items in first set but not second

Example:

set1.difference(set2)

or

set1 - set2

Symmetric Difference:

symmetric_difference()

- Returns items that are in either set but NOT both

Example:

set1.symmetric_difference(set2)

or

set1 ^ set2

Subset and Superset:

issubset()

Example:

small_set.issubset(big_set)

Returns:

- True
- False

issuperset()

Example:

big_set.issuperset(small_set)

Returns:

- True
- False

Disjoint Sets:

isdisjoint()

- Checks if two sets have no common items

Example:

even_numbers.isdisjoint(odd_numbers)

Returns:

- True
- False

Most important set methods:

add()
update()
remove()
discard()
pop()
clear()
union()
intersection()
difference()

Things I'll actually use in projects:

- Removing duplicates from data
- Checking membership with "in"
- Converting list ↔ set
- Basic union/intersection operations

Important:

Lists:

- Ordered
- Allow duplicates
- Use []

Sets:

- Unordered
- No duplicates
- Use {}