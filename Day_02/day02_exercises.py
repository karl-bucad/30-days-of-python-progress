#Exercise Level 1
#1 (done)

#2 - Write a python comment saying "Day 2: 30 Days of python programming"
#Day 2: 30 Days of python programming

#3 - Declare a first name variable and assign a value to it
firstname = "Karl"

#4 - Declare a last name variable and assign a value to it
lastname = "Bucad"

#5 - Declare a full name variable and assign a value to it
fullname = "Karl Bucad"

#6 - Declare a country variable and assign a value to it
country = "Philippines"

#7 - Declare a city variable and assign a value to it
city = "Sterling Heights"

#8 - Declare an age variable and assign a value to it
age = 20

#9 - Declare a year variable and assign a value to it
year = 2025

#10 - Declare a variable is_married and assign a value to it
is_married = False

#11 - Declare a variable is_true and assign a value to it
is_true = True

#12 - Declare a variable is_light_on and assign a value to it
is_light_on = True

#13 - Declare multiple variable on one line
a, b, c = 1, 2, 3
print(a, b, c)

#Exercise Level 2
#1 - Check the data type of all your variables using type() built-in function
print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2 - Using the len() built-in function, find the length of your first name
print(len(firstname)) #length is 4

#3 - Compare the length of your first name and your last name
print(len(firstname)) #length is 4
print(len(lastname)) #length is 5, last name is longer

#4 - Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#5 - Add num_one and num_two and assign the value to a variable total
num_total = num_one + num_two

#6 - Subtract num_two from num_one and assign the value to a variable diff
num_difference = num_one - num_two

#7 - Multiply num_two and num_one and assign the value to a variable product
num_product = num_two * num_one

#8 - Divide num_one by num_two and assign the value to a variable division
num_division = num_one / num_two

#9 - Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
num_remainder = num_two % num_one

#10 - Calculate num_one to the power of num_two and assign the value to a variable exp
num_exp = num_one ** num_two

#11 - Find floor division of num_one by num_two and assign the value to a variable floor_division
num_floor_division = num_one // num_two

#12 - Radius of a circle is 30 meters.
#   I. Calculate the area of a circle and assign the value to a variable name of area_of_circle
#   II. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#   III. Take radius as user input and calculate the area.

#I. (Area of a circle = 3.14 * r ** 2)
r = 30
area_of_circle = 3.14 * r ** 2
print(area_of_circle)

#II. (Circumference of a circle = 2 * 3.14 * radius)
radius = 30
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)

#III. 
user_radius = float(input("Enter radius: "))
user_area_of_circle = 3.14 * user_radius ** 2
print(user_area_of_circle)

#13 - Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_firstname = input("Enter first name: ")
user_lastname = input("Enter last name: ")
user_country = input("Enter country: ")
user_age = int(input("Enter age: "))
print(user_firstname, user_lastname, user_country, user_age)

#14 - Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
#(done)