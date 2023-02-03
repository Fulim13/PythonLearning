# Variable name - reference(pointer) to the value that store in memory
# lowercase and seperated with _
# Eg
# String
import math  # math is object (object can call method)
student_name = "Wong Fu Lim"  # can used "double quote" or 'single quote' or """ for long stirng or commet """
# Number
money = 1000  # Integer
rating = 4.99  # Floating Point Number
# Boolean
is_running = True
is_walking = False

############################################################################################
# Espression - a thing can become a value
# 2 + 2
# variable_name
# 2 > 1 (Boolean Value True)

############################################################################################
# String
programming_language = "Python Programming"

print(len(programming_language))  # 18
print(programming_language[0])  # P
print(programming_language[-1])  # g
print(programming_language[0:3])  # Pyt
print(programming_language[0:])  # Python Programming
print(programming_language[:3])  # Pyt

############################################################################################
# Escape Sequences
# // = /
# /" = "
# /' = /'
# /n = newline

my_name = "Wong\n \"Fu\' L\\im"
print(my_name)
# Wong
# "Fu' L\im

############################################################################################
# Formatted String (> version Python 3.6)
first_name = "Fu Lim"
last_name = "Wong"

full_name = first_name + " " + last_name
print(full_name)  # Fu Lim Wong

full_name_f = f"{first_name} {last_name}"
print(full_name_f)  # Fu Lim Wong

# in f , we can put expression
expression_f = f"{2+2} {2>1} {len(full_name)}"  # 4 True 11
print(expression_f)

############################################################################################
# String Method
# everything in python is object , string is an object , so an object can call the method which means string can call method
course = "python Course"

# below method will not affect the original string (will return a new uppercase value so can store in variable)
print(course.upper())  # PYTHON COURSE
print(course.lower())  # python course
print(course.title())  # Python Course

print(course.find("hon"))  # return the first letter index it find which is 3
# Case Sensitive
print(course.find("Hon"))  # cant find return -1


print(course.replace("o", "k"))  # pythkn Ckurse

# return Boolean
print("pyt" in course)  # True
print("swift" not in course)  # True

print(course)  # python Course


course_space = "      Python     "
print(course_space.strip())  # strip start space and end space
# Python
print(course_space.lstrip())  # left strip
# Python[][][][][]
print(course_space.rstrip())  # right strip
# [][][][][][]Python

print(course_space)  # [][][][][][]Python[][][][][]

###################################################################################
# Number
x = 1  # Integer
x = 1.1  # Floating Point Number
x = 1 + 2j  # complex number (i is imaginary number )

# Addition
print(10 + 3)  # 13
# Subtration
print(10 - 3)  # 7
# Multiplcation
print(10 * 3)  # 30
# Division - return floating
print(10 / 3)  # 3.3333333333333335
# Division Integer - return integer
print(10 // 3)  # 3
# Modulus
print(10 % 3)  # remaider 1
print(10**3)  # 1000


x = 10
x = x + 3  # 13
x += 3  # 16
print(x)  # 16


print(round(2.9))  # 3
print(abs(-2.9))  # 2.9

# math modules (modules is a seperated file )

print(math.ceil(2.2))  # 3
print(math.floor(2.2))  # 2
# REFERENCE
# https://docs.python.org/3/library/math.html

####################################################################################
# Type Conversion
# x = input("x: ")  # this will become string
# print(x)  # "5"
# print(type(x))  # str
# # y = x + 1 # "1" + 1
# # #Traceback (most recent call last):
# #   File "C:\Users\ASUS\Desktop\Python\app.py", line 132, in <module>
# #     y = x + 1
# # TypeError: can only concatenate str (not "int") to str

# y = int(x) + 1
# print(f"x: {x}, y: {y}")  # x: 5 y: 6

# Convert
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy
# ""
# 0
# None

# everythong else will be true
# eg
print(bool(None))  # False
print(bool("Hi"))  # True
