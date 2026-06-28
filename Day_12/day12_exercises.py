#Day 12 Exercises
import random
import string

#Exercise Level 1
#1 - Write a function which generates a six digit/character random_user_id
# print(random_user_id())
# '1ee33d'
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ""

    for i in range(6):
        user_id += random.choice(characters)

    return user_id

print(random_user_id())


#2 - Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated
# print(user_id_gen_by_user()) # user input: 5 5
# output:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr
def user_id_gen_by_user():
    characters = string.ascii_letters + string.digits

    length = int(input("Number of characters: "))
    amount = int(input("Number of IDs: "))

    for i in range(amount):
        user_id = ""

        for j in range(length):
            user_id += random.choice(characters)

        print(user_id)

user_id_gen_by_user() 

#3 - Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each)
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return f"rgb({r}, {g}, {b})"

print(rgb_color_gen())

#Exercise Level 2
#1 - Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples)
def list_of_hexa_colors(num):
    hex_digits = "0123456789abcdef"

    colors = []

    for i in range(num):
        color = "#"

        for j in range(6):
            color += random.choice(hex_digits)

        colors.append(color)

    return colors

print(list_of_hexa_colors(3))

#2 - Write a function list_of_rgb_colors which returns any number of RGB colors in an array
def list_of_rgb_colors(num):
    colors = []

    for i in range(num):
        colors.append(rgb_color_gen())

    return colors

print(list_of_rgb_colors(3))

#3 - Write a function generate_colors which can generate any number of hexa or rgb colors
 #  generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
 #  generate_colors('hexa', 1) # ['#b334ef']
 #  generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
 #  generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(color_type, num):
    if color_type == "hexa":
        return list_of_hexa_colors(num)
    
    elif color_type == "rgb":
        return list_of_rgb_colors(num)
    
    else:
        return "Invalid color type"
    
print(generate_colors("hexa", 3))
print(generate_colors("rgb", 3))

#Exercise Level 3
#1 - Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    shuffled = lst.copy()
    random.shuffle(shuffled)
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))

#2 - Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique
def unique_random_numbers():
    numbers = random.sample(range(10), 7)
    return numbers

print(unique_random_numbers())