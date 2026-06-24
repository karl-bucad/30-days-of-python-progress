#Day 8 Exercises
#1 - Create an empty dicitonary called dog
dog = {}

#2 - Add name, color, breed, legs, age to the dog dictionary
dog = {"name":"Hazel", "color":"blonde", "breed":"shihpoo", "legs":4, "age":9}

#3 - Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dictionary = {"first_name":"Karl", 
                      "last_name":"Bucad",
                      "gender":"Male", 
                      "age":21, 
                      "marital_status":"Single",
                      "skills": ["Python", "C++"],
                      "country":"USA", 
                      "city":"Sterling Heights", 
                      "address":{
                          "street":"Helena Ave",
                          "zipcode":"48313"
                      }
                      }

#4 - Get the length of the student dictionary
print(len(student_dictionary))

#5 - Get the value of skills and check the data type, it should be a list
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))

#6 - Modify the skills values by adding one or two skills
student_dictionary["skills"].append("Git")
student_dictionary["skills"].append("GitHub")

print(student_dictionary)

#7 - Get the dictionary keys as a list
keys = student_dictionary.keys()
print(keys)

#8 - Get the dictionary values as a list
values = student_dictionary.values()
print(values)

#9 - Change the dictionary to a list of tuples using items() method
print(student_dictionary.item())

#10 - Delete one of the items in the dictionary
student_dictionary.pop("first_name")
print(student_dictionary)

#11 - Delete one of the dictionaries
del dog