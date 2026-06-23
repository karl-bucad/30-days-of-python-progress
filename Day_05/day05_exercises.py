#Day 5 Exercises
#Exercise Level 1
#1 - Declare an empty list
empty_list = []

#2 - Declare a list with more than 5 items
names = ["Karl", "Yanz", "Bella", "Be", "Bucad", "Fitzgerald"]

#3 - Find the length of your list
print(len(names))

#4 - Get the first item, the middle item and the last item of the list
print(names[0])
print(names[len(names) // 2])
print(names[-1])

#5 - Declare a list called mixed_data_types, put your (name, age, height, marital status, address)
mixed_data_types = ["Karl", 21, 5.7, "single", "Michigan"]

#6 - Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 - Print the list using print()
print(it_companies)

#8 - Print the number of companies in the list
print(len(it_companies))

#9 - Print the first, middle and last company
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

#10 - Print the list after modifying one of the companies
it_companies[4] = "Nvidia"
print(it_companies)

#11 - Add an IT company to it_companies
it_companies.append("IBM")
print(it_companies)

#12 - Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "TSMC")
print(it_companies)

#13 - Change one of the it_companies names to uppercase (IBM excluded)
it_companies[1] = it_companies[1].upper()
print(it_companies)

#14 - Join the it_companies with a string '#; '
print("#; ".join(it_companies))

#15 - Check if a certain company exists in the it_companies list
does_exist = "Apple" in it_companies
print(does_exist)

#16 - Sort the list using sort() method
it_companies.sort()
print(it_companies)

#17 - Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18 - Slice out the first 3 companies from the list
print(it_companies[:3])

#19 - Slice out the last 3 companies from the list
print(it_companies[-3:])

#20 - Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
print(it_companies[middle_index])

#21 - Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#22 - Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

#23 - Remove the last IT company from the list
it_companies.pop()
print(it_companies)

#24 - Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#25 - Destroy the IT companies list
del it_companies

#26 - Join the front_end list and back_end list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end #or front_end.extend(back_end)
print(full_stack)

#27 - After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = (front_end + back_end).copy()

redux_index = full_stack.index("Redux")
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")

print(full_stack)

#Exercise Level 2
#The following is a list of 10 student ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages.sort()
print(ages)

min_age = min(ages)
max_age = max(ages)

print(min_age)
print(max_age)

#Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages.sort()
middle = len(ages) // 2

if len(ages % 2 == 0):
    median = (ages[middle - 1] + ages[middle]) // 2
else:
    median = ages[middle]

print(median)

#Find the average age (sum of all items divided by their number )
average = sum(ages) / len(ages)
print(average)

#Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)
print(age_range)

#Compare the value of (min - average) and (max - average), use abs() method
min_difference = abs(min(ages) - average)
max_difference = abs(max(ages) - average)

print(min_difference)
print(max_difference)