#Day 9 Exercises
#Exercise Level 1
#1 - Get user input using input("Enter your age: "). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.
#Output:
#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.

user_age = int(input("Enter your age: "))
if user_age >= 18:
        print("You are old enough to drive.")
else:
        missing_years = 18 - user_age
        if missing_years == 1:
            print("You need 1 more year to learn to drive")
        else:
            print("You need", missing_years, "more years to learn to drive")

#2 - Compare the value of my_age and your_age using if ... else. Who is older (me or you)?
# Use input("Enter your age: ") to get the age as input. You can use a nested condition to print "year" for 1 year difference in age,
# "years" for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.

my_age = 21
your_age = int(input("Enter your age: "))
if my_age > your_age:
        difference = my_age - your_age
        if difference == 1:
               print("You are 1 year younger than me")
        else:
               print("You are", difference, "years younger than me")
elif my_age < your_age:
        difference = your_age - my_age
        if difference == 1:
               print("You are 1 year older than me")
        else:
               print("You are", difference, "years older than me")
else:
        print("We are the same age")

#3 - Get two numbers from the user input prompt. If a is greater than b return a is greater than b, if a is less than b return a is smaller than b,
# else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
        
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
        print(a, "is greater than", b)
elif a < b:
        print(a, "is smaller than", b)
else:
        print(a, "is equal to", b)

#Exercise Level 2
#1 - Write a code which gives grade to students according to their scores:
# '''sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# '''

grade = int(input("Enter your grade: "))

if grade >= 90:
        print("Your final grade is an A")
elif grade >= 80:
        print("Your final grade is a B")
elif grade >= 70:
        print("Your final grade is a C")
elif grade >= 60:
        print("Your final grade is a D")
else:
        print("Your final grade is an F")

#2 - Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September,
# October, or November, the season is Autumn. December, January or February, the season is Winter. March, April or May,
# the season is Spring. June, July or August, the season is Summer

month = input("Enter what month it is: ").capitalize()

if month == "September" or month == "October" or month == "November":
        print("The season you are in is Autumn/Fall")
elif month == "December" or month == "January" or month == "February":
        print("The season you are in is Winter")
elif month == "March" or month == "April" or month == "May":
        print("The season you are in is Spring")
elif month == "June" or month == "July" or month == "August":
        print("The season you are in is Summer")
else:
        print("Please enter a valid month")

#3 - The following list contains some fruits:
# '''sh
# fruits = ["banana", "orange", "mango", "lemon"]
# '''
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print("That fruit already exist in the list")

fruits = ["banana", "orange", "mango", "lemon"]

fruit = input("Enter fruit: ").lower()
if fruit in fruits:
        print("That fruit already exists in the list")
else:
        fruits.append(fruit)
        print(fruits)

#Exercise Level 3
#1 - Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list
if 'skills' in person:
        skills = person['skills']
        middle_skill = len(skills) // 2
        print(skills[middle_skill])

# Check if the person dictionary has skills key, if so check if the person has "Python" skill and print out the result
if 'skills' in person:
        print("Python" in person["skills"])

# If a person skills has only JavaScript and React, print("He is a front end developer"), if the person skills has Node, Python, MongoDB, print("He is a backend developer"),
# if the person has React, Node and MongoDB, print("He is a fullstack developer"), else print("unknown title") - for more accurate results more conditions can be nested!
skills = person["skills"]

if "JavaScript" in skills and "React" in skills and len(skills) == 2:
    print("He is a front end developer")

elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
    print("He is a backend developer")

elif "React" in skills and "Node" in skills and "MongoDB" in skills:
    print("He is a fullstack developer")

else:
    print("unknown title")

# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.
if person["is_married"] and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} "
        f"lives in {person['country']}. He is married."
    )