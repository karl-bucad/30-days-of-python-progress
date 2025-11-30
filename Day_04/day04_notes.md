Strings = text inside quotes (' ' or " ")

len() gets length of a string

Multiline strings: use triple quotes (''' ''' or """ """)

String concatenation:
"Hello" + " " + "World"

Escape characters:
\n = new line
\t = tab
\\ = backslash
\' = single quote
\" = double quote

String formatting:
- Old style: %s, %d, %f
- str.format(): "I am {}".format(name)
- f-strings: f"I am {name}"

Strings are sequences:
- Indexing: text[0], text[1], text[-1]
- Slicing: text[start:end]
- Reverse string: text[::-1]
- Slice with step: text[0:6:2]

Common string methods:
capitalize()
count()
endswith()
expandtabs()
find() / rfind()
index() / rindex()
isalnum()
isalpha()
isdecimal()
isdigit()
isnumeric()
isidentifier()
islower()
isupper()
join()
strip()
replace()
split()
title()
swapcase()
startswith()