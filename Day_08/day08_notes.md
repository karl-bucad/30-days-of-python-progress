Dictionaries:

- Store data as key pairs
- Mutable (can be modified)
- Unordered collection
- Uses {}

Example:

person = {
    "name": "Karl",
    "age": 21,
    "country": "USA"
}

Creating dictionaries:

empty_dict = {}

or

empty_dict = dict()

Dictionary length:

- Number of key pairs

Example:

len(person)

Accessing values:

person["name"]
person["age"]

Output:

Karl
21

Important:

person["city"]

causes an error if the key doesn't exist.

Safer method:

person.get("city")

Output:

None

Adding items:

person["job"] = "Student"

Result:

{
    "name": "Karl",
    "age": 21,
    "job": "Student"
}

Modifying items:

person["age"] = 22

Checking if a key exists:

"name" in person

Returns:

- True
- False

Removing items:

pop()

- Removes a key

Example:

person.pop("age")

popitem()

- Removes the last item

Example:

person.popitem()

del

- Removes a specific key

Example:

del person["country"]

Converting dictionary to items:

items()

- Returns key pairs as tuples

Example:

person.items()

Output:

dict_items([
    ("name", "Karl"),
    ("age", 21)
])

Clearing a dictionary:

person.clear()

Result:

{}

Deleting a dictionary:

del person

Copying a dictionary:

person_copy = person.copy()

Use copy() to avoid modifying the original dictionary.

Getting keys:

person.keys()

Output:

dict_keys([
    "name",
    "age",
    "country"
])

Getting values:

person.values()

Output:

dict_values([
    "Karl",
    21,
    "USA"
])

Most important dictionary methods:

get()
keys()
values()
items()
pop()
copy()
clear()

Important differences:

Lists:

- Ordered
- Access with indexes
- fruits[0]

Dictionaries:

- Key pairs
- Access with keys

person["name"]

Most important concepts to memorize:

dictionary["key"]

dictionary.get("key")

dictionary["new_key"] = value

dictionary.keys()

dictionary.values()

dictionary.items()