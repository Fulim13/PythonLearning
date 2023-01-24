# List - can have any types , not need to same type

from array import array
from collections import deque
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

combined = zeros + letters
print(combined)  # [0, 0, 0, 0, 0, 'a', 'b', 'c']

# Seq of num to list
numbers = list(range(20))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(numbers)

# Str to List
chars = list("Hello World")
print(chars)
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

print(len(chars))  # 11

# Accessing Item
print(letters[0])  # a
print(letters[-1])  # c

# Editing Item
letters[0] = "A"
print(letters)  # ['A', 'b', 'c']

# Slice
print(letters[0:2])  # ['A', 'b']
print(letters[:3])  # ['A', 'b', 'c']
print(letters[0:])  # ['A', 'b', 'c']

numbers = list(range(20))
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[::-1])
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Unpacking
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

first, second, third = numbers
print(first, second, third)  # 1 2 3

infinite_num = [1, 23, 5, 5, 5, 2, 56, 21, 5]
first, second, *other, last = infinite_num
print(first)  # 1
print(other)  # [5, 5, 5, 2, 56, 21]
print(last)  # 5

# Loop over list
letters = ["a", "b", "c"]
for letter in letters:
    print(letter)

# a
# b
# c

# get the tuple
for tup_letter in enumerate(letters):
    print(tup_letter)
    print(tup_letter[0], tup_letter[1])

# (0, 'a')
# 0 a
# (1, 'b')
# 1 b
# (2, 'c')
# 2 c

# unpacking
for index, letter in enumerate(letters):
    print(index, letter)

# 0 a
# 1 b
# 2 c


# Adding or Removing Items

# Add
letters = ["a", "b", "c"]
letters.insert(0, "-")
letters.append("d")  # add at back
print(letters)  # ['-', 'a', 'b', 'c', 'd']

# Remove
letters.pop()  # last itme
print(letters)  # ['-', 'a', 'b', 'c']
letters.pop(0)
print(letters)  # ['a', 'b', 'c']
# first b delete,if you want to remove all b, loop over whnole list to remove
letters.remove("b")
print(letters)  # ['a', 'c']

letters.append("d")
del letters[0:2]
print(letters)  # ['d']

letters.clear()
print(letters)  # []

# Find item
letters = ["a", "b", "c"]
print(letters.index("a"))  # 0
# print(letters.index("d"))
# Traceback (most recent call last):
# File "c:\Users\ASUS\Desktop\Python\data_structures.py", line 113, in <module >
# print(letters.index("d"))
# ValueError: 'd' is not in list

if "d" in letters:
    print(letter.index("d"))


print(letters.count("d"))  # 0

# Sorting List - will affect the original list
numbers = [1, 9, 8, 7, 2, 6]
numbers.sort()
print(numbers)  # [1, 2, 6, 7, 8, 9]
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 7, 6, 2, 1]

# this will not modify the original list
numbers = [1, 9, 8, 7, 2, 6]
print(sorted(numbers, reverse=True))  # [1, 2, 6, 7, 8, 9]
print(numbers)  # [9, 8, 7, 6, 2, 1]

items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 18),
]

items.sort()
print(items)  # Not changed, because python dont know how to sort
# [('Product1', 10), ('Product2', 20), ('Product3', 18)]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# [('Product1', 10), ('Product3', 18), ('Product2', 20)]

######################################################################################
# Lambda(annomynous) function

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)  # [('Product2', 9), ('Product1', 10), ('Product3', 12)]

items.sort(key=lambda item: item[1])
print(items)  # [('Product2', 9), ('Product1', 10), ('Product3', 12)]

######################################################################################
# Map Function
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# Transfer the tuple of items to list of price
# Harder
prices = []
for item in items:
    prices.append(item[1])

print(prices)  # [10, 9, 12]

map_object = map(lambda item: item[1], items)
print(map_object)  # <map object at 0x0000026C5BF53EE0> , map object are iterables

for item in map_object:
    print(item)
# 10
# 9
# 12

# More simpler way
prices = list(map(lambda item: item[1], items))
print(prices)  # [10, 9, 12]

######################################################################################
# Filter function
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# Harder
filtered = []
for item in items:
    if item[1] >= 10:
        filtered.append(item)

print(filtered)  # [('Product1', 10), ('Product3', 12)]

filter_object = filter(lambda item: item[1] >= 10, items)
# <filter object at 0x0000017F846B3E50> , filter object also iterables(can run in for loop or using list function)
print(filter_object)

item_greater10 = list(filter(lambda item: item[1] >= 10, items))
print(item_greater10)  # [('Product1', 10), ('Product3', 12)]

######################################################################################
# List Comprehensions
# [expression for item in items]

items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

prices = list(map(lambda item: item[1], items))
print(prices)  # [10, 9, 12]
prices = [item[1] for item in items]
print(prices)  # [10, 9, 12]

item_greater10 = list(filter(lambda item: item[1] >= 10, items))
print(item_greater10)  # [('Product1', 10), ('Product3', 12)]
item_greater10 = [item for item in items if item[1] >= 10]
print(item_greater10)  # [('Product1', 10), ('Product3', 12)]

######################################################################################
# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# [(1.10),(2.20),(3.30)]

print(zip(list1, list2))
# <zip object at 0x000001A940A09400> , zip object also iterables

print(list(zip("abc", list1, list2)))
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]


######################################################################################
# Stacks
# LIFO Last In - First Out
# Book Stack

# Browsing History, back button, back to last one you visit
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)


# our browsing stack
print(browsing_session)  # [1,2,3]

last = browsing_session.pop()
print(last)  # 3
print(browsing_session)  # [1,2]

print("redirect", browsing_session[-1])  # 2

# if the list is empty, disable the session
if not browsing_session:
    print("disable")
else:
    print("redirect", browsing_session[-1])  # 2


######################################################################################
# Queues
# FIFO - First In First Out

# Queue of people

# why use deque, because , if we use the original method, if we remove the first one in the list , all other item in the list need to shift one to forward the list
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)  # deque([2, 3])

if not queue:
    print("empty")

######################################################################################
# Tuple - Read only list , canont remove and add and modify

point = 1,
print(type(point))  # <class 'tuple'>

point = 1, 2
print(type(point))  # <class 'tuple'>

point = ()
print(type(point))  # <class 'tuple'>

# Concate tuples
point = (1, 2) + (3, 4)
print(point)  # (1, 2, 3, 4)

# Repeat tuples
point = (1, 2) * 3
print(point)  # (1, 2, 1, 2, 1, 2)

# Convert list to tuple
point = tuple([1, 2])
print(point)  # (1, 2)

# Convert String (iterables) to tuple
print(tuple("Hello World"))
# ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

# Access item in tuple
point = (1, 2, 3)
print(point[0])  # 1

# slice
print(point[0:2])  # (1,2)

# unpack
x, y, z = point
print(x, y, z)  # 1 2 3

if 10 in point:
    print("exists")


# tuple are immutable(cannot add , remove ,change)
# point[0] = 10
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\data_structures.py", line 336, in <module>
#     point[0] = 10
# TypeError: 'tuple' object does not support item assignment

######################################################################################
# Swapping Variables
x = 10
y = 11

temp = x
x = y
y = temp


print("x :", x)  # x : 11
print("y :", y)  # y : 10

x, y = y, x
# Same as
# x, y - (10, 11)
print("x :", x)  # x : 10
print("y :", y)  # y : 11

# so we can set the multiple value to varaible in one line
a, b = 1, 2
print(a, b)  # 1 2

######################################################################################
# Array - using by last list of numbers, more memory efficient


# Typecode
# https://docs.python.org/3/library/array.html
numbers = array("i", [1, 2, 3])
print(numbers)
numbers.append(4)
print(numbers)  # array('i', [1, 2, 3])

numbers.insert(4, 5)
print(numbers)  # array('i', [1, 2, 3, 4, 5])
numbers.pop()
print(numbers)  # array('i', [1, 2, 3, 4])
print(numbers[0])  # 1

# unlike list , the object in this array must be same type, in this case "i" is integer
# numbers[0] = 1.0
# #Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\data_structures.py", line 384, in <module>
#     numbers[0] = 1.0
# TypeError: 'float' object cannot be interpreted as an integer


######################################################################################
# Sets - Collection not duplicate
numbers = [1, 1, 2, 3, 3, 4]
uniques = set(numbers)
print(uniques)  # {1, 2, 3, 4}

second = {1, 4}
print(second)  # {1, 4}

second.add(5)
print(second)  # {1, 4, 5}

second.remove(1)
print(second)  # {4, 5}

print(len(second))  # 2

# Union
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# union of two set
print(first | second)  # {1, 2, 3, 4, 5}

# intercep between two set
print(first & second)  # {1}

# in second set , we dont have this set of number in first set
print(first - second)  # {2,3,4}

# return set , will either in first set or second set but not both
print(first ^ second)  # {2, 3, 4, 5}


# cannot access , set does not use indexing
# print(first[0])
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\data_structures.py", line 425, in <module>
#     print(first[0])
# TypeError: 'set' object is not subscriptable

if 1 in first:
    print("yes")

# yes
######################################################################################
# Dictionary - collecion of key value pair
# phone book
# key -> value
# name -> contact

point = {"x": 1, "y": 2}
# only can use immutable type for the key, like String or numbers
# value can be any type
list()
tuple()
set()
point = dict(x=1, y=2)

# using key to find value
print(point["x"])  # 1
point["x"] = 10

# change the value using key
print(point)  # {'x': 10, 'y': 2}

# add new key value pair
point["z"] = 20
print(point)  # {'x': 10, 'y': 2, 'z': 20}

# Did not exist key
# print(point["a"])
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\data_structures.py", line 463, in <module>
#     print(point["a"])
# KeyError: 'a'

# check existence of the key first , before access the key
if "a" in point:
    print(point["a"])

# if the key does not exist , it will return None
print(point.get("a"))  # None

# change None to something
print(point.get("a", 0))  # 0

# delete item
del point["x"]
print(point)  # {'y': 2, 'z': 20}

# Loop over dict
for key in point:
    print(key, point[key])

# y 2
# z 20

# .items() will make it become tuple of key value pair, so can unpacking
for key, value in point.items():
    print(key, value)

# y 2
# z 20

######################################################################################
# Dicionary Comprehension

# Loop
values = []
for x in range(5):
    values.append(x*2)
print(values)  # [0, 2, 4, 6, 8]

# List Comprehension
values = [x*2 for x in range(5)]
print(values)  # [0, 2, 4, 6, 8]

# Set Comprehension
values = {x*2 for x in range(5)}
print(values)  # {0, 2, 4, 6, 8}

# Loop for Dic
values = {}
for x in range(5):
    values[x] = x*2

print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Dic Comprehension
values = {x: x*2 for x in range(5)}
print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Tuple Comprehension
values = (x*2 for x in range(5))
print(values)  # <generator object <genexpr> at 0x0000024360ED20A0>

######################################################################################
# Generator Expression

######################################################################################
# Unpacking Operator
