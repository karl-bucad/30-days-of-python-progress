#Day 3 Exercises
#1 - Declare your age as integer variable
age = 20

#2 - Declare your height as a float variable
height = 67.0 # is in inches

#3 - Declare a variable that store a complex number
equation = 6 - 7j

#4 - Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
user_base = int(input("Enter base: "))
user_height = int(input("Enter height: "))
area = 0.5 * user_base * user_height
print("The area of the triangle is ", area)

#5 - Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
user_side_a = int(input("Enter side a: "))
user_side_b = int(input("Enter side b: "))
user_side_c = int(input("Enter side c: "))
perimeter = user_side_a + user_side_b + user_side_c
print("The perimeter of the triangle is ", perimeter)

#6 - Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
user_length = int(input("Enter length: "))
user_width = int(input("Enter width: "))
area = user_length * user_width
perimeter = 2 * (user_length + user_width)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)

#7 - Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14
user_radius = int(input("Enter radius: "))
area = 3.14 * user_radius * user_radius
circumference = 2 * 3.14 * user_radius
print("The area of the circle is ", area)
print("The circumference of the circle is ", circumference)

#8 - Calculate the slope, x-intercept, and y-intercept of y = 2x - 2
slope = 2
x_intercept = 1
y_intercept = -2

print("Slope:", slope)
print("x-intercept:", x_intercept)
print("y-intercept:", y_intercept)

#9 - Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6, 10)
x1 = 2
x2 = 6
y1 = 2
y2 = 10
slope = (y2 - y1)/(x2 - x1)
print("The slope is ", slope)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("The Euclidean distance is ", distance)

#10 - Compare the slopes in tasks 8 and 9
task8_slope = 2
task9_slope = 2
print(task8_slope == task9_slope) #True

#11 - Calculate the value of y(y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0
x1 = 1 #didn't work
x2 = -1 #didn't work
x3 = -2 #didn't work
x4 = -3 #worked
y_value = x4 ** 2 + 6 * x4 + 9
print("Y is going to be 0 when the x value is ", x4)

#12 - Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len("python")) #6 characters
print(len("dragon")) #6 characters
print(len("python") > len("dragon")) #false comparison statement

#13 - Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

#14 - I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print("jargon" in "I hope this course is not full of jargon")

#15 - There is no "on" in both dragon and python
print("on" not in "dragon" and "on" not in "python")

#16 - Find the length of the text python and convert the value to float and convert it to string
length = (len("python"))
print(length) # length in int
print(float(length)) # length in float
print(str(length)) # length in string

#17 - Even nummbers are divisble by 2 and the remainder is zero. How do you chekc if a number is even or not using python?
number = 10
print(number % 2 == 0) # is even, outputs true

number_two = 7
print(number_two % 2 == 0) # is odd, outputs false

#18 - Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7 // 3
int_conversion = int(2.7)

print(floor_division == int_conversion) #outputs True

#19 - Check if type of '10' is equal to type of 10
type1 = type("10")
type2 = type(10)
print(type1 == type2) #outputs False

#20 - Check if int('9.8') is equal to 10
#integer = int('9.8') #this causes an error because '9.8' is not a valid integer string
#print(integer == 10) #so int('9.8') can't even be compared to 10 without crashing

#21 - Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
user_hours = int(input("Enter hours: "))
user_rph = int(input("Enter rate per hour: "))
pay = user_hours * user_rph
print("Your weekly earning is ", pay)

#22 - Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
user_years_lived = int(input("Enter number of years you have lived: "))
years_in_seconds = 60 * 60 * 24 * 365 * user_years_lived
print("You have lived for ", years_in_seconds, "seconds")

#23 - Write a python script that displays the following data
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")