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

# try:
#     age = int(input("Age: "))
#     xfactro = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't eneter a value age")
# else:
#     print(age)
#######################################################################
# finally
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactro = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't eneter a value age")
# else:
#     print(age)
# finally:
#     # to close file, close db connection, network connection
#     # it will run no matter it have exception or nto
#     file.close()
######################## c###############################################
# with statement

# try:
#     with open("app.py") as file, open("another.txt") as target:
#         print("File opened")
#         # with will auto close the file, clean up the resource , not need finally block
#         # if the object have file.__enter__ or file.__exit__, it can use with method.
#         age = int(input("Age: "))
#     xfactro = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't eneter a value age")
# else:
#     print(age)
######################## c###############################################
# Raising Exception


# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less")
#     return 10/age


# try:
#     calculate_xfactor(-1)
# except ValueError as err:
#     print(err)

# Age cannot be 0 or less
# https://docs.python.org/3/library/exceptions.html
#######################################################################
# Cost of Raising Exception
from timeit import timeit
code1 = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as err:
    pass

    """

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age



xfactor =  calculate_xfactor(-1)
if xfactor == None:
    pass
"""


# run 10000 times
print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
# first code= 0.003167599905282259
# second code= 0.0014702000189572573

# if can use if statement , then dont use exception handling
