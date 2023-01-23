# Comparison Operator
10 > 3  # True
10 >= 3  # True
10 < 20  # True
10 <= 20  # True
10 == 10  # True
10 == "10"  # False
10 != "10"  # True

"bag" > "apple"  # True (b > a in ascii )
"bag" > "Bag"  # False (B > b in ascii)
ord("b")  # 98
ord("B")  # 66

# Conditional Statement
temperature = 35
if temperature > 30:
    print("It is warm")
    print("Drink water")
elif temperature > 20:
    print("It is nice")
else:
    print("It is cold")
print("Done")

#########################################################################################
# Tenary
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

print(message)  # Eligible

message2 = "Eligible" if age >= 18 else "Not eligible"
print(message2)  # Eligible

#########################################################################################
# Logical operators
# and - both need to be true
high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# "Not eligible

# or - one of it true then true
# not (convert True to False and vice versa)
student = False
if not student:
    print("Not Student")
else:
    print("Student")

# Not Student

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
# Eligible

#########################################################################################
# Short circuit
# when it is and operator , when it find one False, the entire expression is False
# when is is or operator , when it find one True, the entire expression is True

#########################################################################################
# Chainning Comparison Operators

# age should be between 18 and 65

# 18 <= age <65

if age >= 18 and age < 65:
    print("Young guys")

if 18 <= age < 65:
    print("Young guys")

#########################################################################################
# For Loop
for number in range(3):
    print("Attempt", number, (number+1) * ".")

# Attempt 0 .
# Attempt 1 ..
# Attempt 2 ...


for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
# Attempt 1 .
# Attempt 3 ...
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........

#########################################################################################
# For Else
sucessful = False

for number in range(3):
    print("Attempt", number+1)
    if sucessful:
        print("Successfull")
        break
else:
    # if it never break out of the for loop, then it will go to else statement (try to change successful to True and False and see the result)
    print("Attepted 3 times and  falied")

# When sucessful is True
# Attempt 1
# Successfull

# WHen sucessful is False
# Attepted 3 times and  falied

#########################################################################################
# Nested
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# (0,0)
# (0,1)
# (0,2)
# (1,0)
# (1,1)
# (1,2)
# (2,0)
# (2,1)
# (2,2)
# (3,0)
# (3,1)
# (3,2)
# (4,0)
# (4,1)
# (4,2)

#########################################################################################
# Iterables
print(type(5))  # <class 'int'>

print(type(range(5)))  # <class 'range'>

# range type are iterables - can be used in for loop(iterate)
# string also iterables

for x in "Python":
    print(x)

# P
# y
# t
# h
# o
# n

# list also iterables
for x in [1, 2, 3, 4]:
    print(x)

# 1
# 2
# 3
# 4

#########################################################################################
# While Loops

number = 100
while number > 0:
    print(number)
    number //= 2

# 100
# 50
# 25
# 12
# 6
# 3
# 1

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# >1
# ECHO 1
# >2
# ECHO 2
# >quit
# ECHO quit
# PS C:\Users\ASUS\Desktop\Python>

#########################################################################################
# Infinite Loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break
