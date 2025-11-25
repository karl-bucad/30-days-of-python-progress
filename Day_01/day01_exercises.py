#Exercise Level 1
#1 - Check the python version you are using (done)

#2 - Open the python interactive shell and do the following operations. The operands are 3 and 4
print(3 + 4)   #addition
print(3 - 4)   #subtraction
print(3 * 4)   #multiplication
print(3 % 4)   #modulus(remainder)
print(3 / 4)   #division
print(3 ** 4)  #exponential
print(3 // 4)  #floor division operator(rounds down)

#3 - Write strings on the python interactive shell. The strings are your name, your family name, your country, and I am enjoying 30 days of python
print("Karl")
print("Bucad")
print("Philippines")
print("I am enjoying 30 days of python")

#4 - Check the data types of the data 10, 9.8, 3.14, 4 - 4j, ['Asbaneh', 'Python', 'Finland'], your name, your family name, and your country
print(type(10)) #int
print(type(9.8)) #float
print(type(3.14)) #float
print(type(4 - 4j)) #complex
print(type(['Asbaneh', 'Python', 'Finland'])) #list
print(type("Karl")) #string
print(type("Bucad")) #string
print(type("Philippines")) #string

#Exercise Level 2
#1 (done)

#Exercise Level 3
#1 - Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary
print(6 - 4j) #Number
print("Karl Bucad") #String
print(3 == 3) #Boolean
print([1, 2, 3 ,4 ,5]) #List
print(('Michael Jordan', 'Lebron James', 'Kareem Abdul-Jabbar', 'Magic Johnson', 'Bill Russel')) #Tuple
print({1, 2, 3, 4, 5}) #Set
print({'First Name':'Karl'}) #Dictionary

#2 - Find an Euclidian distance between (2, 3) and (10, 8)
x1 = 2
y1 = 3
x2 = 10
y2 = 8

euclidian_distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(euclidian_distance)