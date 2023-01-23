# Defining Functions
def greet():
    print("Hello")


greet()  # Hello

####################################################################################
# Arguments


def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


greet("Fu Lim", "Wong")  # Hello, Fu Lim Wong
# REUSABLE
greet("Lebron", "James")  # Hello, Lebron James

# Aruguemnts is the actual value of passing to fucntion, in this case "Fu Lim","Wong"
# Parameter is the input you defined for your function , in this case is first_name, last_name

####################################################################################
# Types of Functions
# 1 - Peform a task


def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")


# 2 Return a value
round(1.9)


def get_greeting(name):
    return f"Hello {name}"


greeting = get_greeting("Fu Lim")
print(greeting)  # Hello Fu Lim


def greet(name):
    print(f"Hi {name}")


# None by default all the function return None if not specified
print(greet("Fulim"))


####################################################################################
# Keyword Arguments
def increment(number, by):
    return number + by


print(increment(2, by=1))  # 3

####################################################################################
# Default Arguments


def decrement(number, by=1):
    return number - by


print(decrement(2, 2))  # 0
print(decrement(2))  # 1

# default/optional parameter should after require parammeter
# def decrement(number, by=1 , another):
# another is invalid because it is require parameter and it is after the optional parameter by

####################################################################################
# xargs


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)
# (2,3,4,5) tuple (cannot modify this tuple ,add and edit)


def multiply2(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


multiply2(1, 2, 3, 4)  # 24

####################################################################################
# xxargs


def save_user(**user):
    print(user)
    print(user["id"])


save_user(id=1, name="John", age=22)
# {'id': 1, 'name': 'John', 'age': 22} # dictionary
# 1

####################################################################################
# Scope
# Global
message = "a"  # can be used by all code


def greet():
    global message
    message = "b"  # change the global
# Local


def local1(name):
    mes = "a"
    # both local and name are only can be used within this function


def local2(name):
    mes = "b"
####################################################################################
