# exception happens, programming mistake. bad data send form user, resource is not avaiable
# OPEN FILE DOES NOT EXIST , OUR PROGRAM WILL CRASH


# numbers = [1, 2]
# Index Error
# print(numbers[3])
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\exception.py", line 6, in <module>
#     print(numbers[3])
# IndexError: list index out of range

# age = int(input("Age: "))
# Age: a
# Traceback (most recent call last):
#   File "C:\Users\ASUS\Desktop\Python\exception.py", line 13, in <module>
#     age = int(input("Age: "))
# ValueError: invalid literal for int() with base 10: 'a'


#######################################################################
# Handling Exception
# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't eneter a value age")
#     print(ex)
#     print(type(ex))
# else:
#     print(age)

# print("Execution continues")


# Age: a
# You didn't eneter a value age
# invalid literal for int() with base 10: 'a'
# <class 'ValueError'>
# Execution continues

# Age: a
# You didn't eneter a value age
# invalid literal for int() with base 10: 'a'
# <class 'ValueError'>
# Execution continues

# if you dont use tru block , the Execution continues will not print out

#######################################################################
# Handling different exception
# try:
#     age = int(input("Age: "))
#     xfactro = 10 / age
# except ValueError:
#     print("You didn't eneter a value age")
# except ZeroDivisionError:
#     print("You cannot enter 0")
# else:
#     print(age)

# Age: 0
# You cannot enter 0

try:
    age = int(input("Age: "))
    xfactro = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't eneter a value age")
else:
    print(age)
