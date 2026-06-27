#Day 11 Exercises
import math
#Exercise Level 1
#1 - Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(x, y):
    total = x + y
    return total

#2 - Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return math.pi * r * r

#3 - Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0

    for num in args:
        if type(num) != int and type(num) != float:
            return "All arguments must be numbers"
        total += num

    return total    

#4 - Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    fahrenheit = (c * 9 / 5) + 32
    return fahrenheit

#5 - Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.capitalize()

    if month in ["September", "October", "November"]:
        return "Autumn"
    elif month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Invalid month"

#6 - Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

#7 - Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "No real solutions"
    
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)

    return x1, x2

#8 - Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

#9 - Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
def reverse_list(array):
    reversed_array = []

    for i in range(len(array) -1, -1, -1):
        reversed_array.append(array[i]) 

    return reversed_array

#10 - Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized = []

    for item in lst:
        capitalized.append(item.capitalize())

    return capitalized

#11 - Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
def add_item(lst, item):
    lst.append(item)
    return lst

#12 - Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst, item):
    lst.remove(item)
    return lst

#13 - Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
def sum_of_numbers(num):
    total = 0

    for i in range(num + 1):
        total += i

    return total

#14 - Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    total = 0

    for i in range(num + 1):
        if i % 2 != 0:
            total += i
        
    return total

#15 - Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    total = 0

    for i in range(num + 1):
        if i % 2 == 0:
            total += i

    return total

#Exercise Level 2
#1 - Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    # print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
def evens_and_odds(num):
    evens = 0
    odds = 0

    for i in range(num + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    return f"The number of odds are {odds}. \nThe number of evens are {evens}."    

#i - Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

#ii - Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    return len(value) == 0

#iii - Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    lst.sort()
    middle = len(lst) // 2

    if len(lst) % 2 == 0:
        return (lst[middle - 1] + lst[middle]) / 2
    else:
        return lst[middle]
    
def calculate_mode(lst):
    most_common = lst[0]
    highest_count = 0

    for item in lst:
        count = lst.count(item)

        if count > highest_count:
            highest_count = count
            most_common = item

    return most_common

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    mean = calculate_mean(lst)
    total = 0

    for num in lst:
        total += (num - mean) ** 2

    return total / len(lst)

def calculate_std(lst):
    return calculate_variance(lst) ** 0.5

#iv - Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
    # greet()
    # "Hello, Guest!
    # greet("Alice")
    # "Hello, Alice!"
def greet(name = "Guest"):
    print(f"Hello, {name}!")

#1 - Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
def show_args(**kwargs):
    print("Received:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

#Exercise Level 3
#1 - Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

#2 - Write a functions which checks if all items are unique in the list.
def all_items_unique(lst):
    for item in lst:
        if lst.count(item) > 1:
            return False
        
    return True

#3 - Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst):
    first_type = type(lst[0])

    for item in lst:
        if type(item) != first_type:
            return False
        
    return True

#4 - Write a function which check if provided variable is a valid python variable
def is_valid_variable(variable):
    return variable.isidentifier()