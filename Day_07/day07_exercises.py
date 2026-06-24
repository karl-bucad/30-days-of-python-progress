#Day 7 Exercises
#Exercise Level 1
#1 - Find the length of the set it_companies
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

#2 - Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#3 - Insert multiple IT companies at once to the set it_companies
it_companies.update(["Tesla", "Netflix", "Nvidia"])
print(it_companies)

#4 - Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(it_companies)

#5 - What is the difference between remove and discard?
#remove() gives an error if the item doesn't exist
#discard() doesn't give an error if the item doesn't exist

#Exercise Level 2
#1 - Join A and B
print(A.union(B))

#2 - Find A intersection B
print(A.intersection(B))

#3 - Is A subet of B?
print(A.issubset(B))

#4 - Are A and B disjoint sets
print(A.isdisjoint(B))

#5 - Join A and B and B with A
print(A.union(B))
print(B.union(A))

#6 - What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7 - Delete the sets completely
del A
del B

#Exercise level 3
#1 - Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)

print(len(age))
print(len(ages_set))

#The list is bigger because it includes duplicates
#The set is smaller because it only keeps unique values

#2 - Explain the difference between the following data types: string, list, tuple and set
#string = text
#list = ordered, mutable, allows duplicates
#tuple = ordered, immutable, allows duplicates
#set = unordered, mutable, doesn't allow duplicates

#3 - I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentenece? Use the split methods and set to get the unique words
sentence = "I am a teacher and I love to inspire and teach people"

words = sentence.split()
unique_words = set(words)

print(unique_words)
print(len(unique_words))