#Day 6 Exercises
#Exercise Level 1
#1 - Create an empty tuple
empty_tuple = ()

#2 - Create a tuple containing names of your sisters and brothers
brothers = ("Tyron",)
sisters = ("Hazel",)

#3 - Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

#4 - How many siblings do you have?
print(len(siblings))

#5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Rommel", "Armilyn")
family_members = siblings + parents

print(family_members)

#Exercise Level 2
#1 - Unpack siblings and parents from family_members
brother, sister, father, mother = family_members

print(brother)
print(sister)
print(father)
print(mother)

#2 - Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "lettuce")
animal_products = ("milk", "eggs", "cheese")

food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)

#3 - Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

#4 - Slice out the middle item or items from the food_stuff_tp tuple or food_stuff)lt list
middle = len(food_stuff_lt) // 2
print(food_stuff_lt[middle])

#5 - Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

#6 - Delete the food_stuff_tp completely
del food_stuff_tp

#7 - Check if an item exists in tuple:
#Check if "Estonia" is a nordic country
#Check if "Iceland" is a nordic country

nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)