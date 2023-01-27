# Class is blueprint to create new obj
# Object: instance of a class
# CLass : Human
# Objects : John,Mary,Smith


x = 1
print(type(x))  # <class 'int'>

#####################################################################################
# Creating a Class - naming(PascalCase)


class Point:
    # all functions in class should have at least one parameter which is self
    def draw(self):
        print("draw")


point = Point()
point.draw()  # draw
print(type(point))  # <class '__main__.Point'>
print(isinstance(point, Point))  # True
print(isinstance(point, int))  # False

#####################################################################################
# Contructor - special method will be called when create object


class Point:
    # Magic method
    # self is a reference to a current object(like java,javascript this )
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # use self to call the attribute x of current object
        print(f"Point ({self.x} ,{self.y})")


point = Point(1, 2)
print(point.x)  # 1
point.draw()  # Point (1 ,2)
# point.draw(point) , we dont need to pass the current object to the parameter, python intrepreter will help us do that
#####################################################################################
# Class vs Instance Attributes


class Point:
    # class attributes, (same for all object,shared by all instances)
    default_color = "red"

    def __init__(self, x, y):
        # x and y are instant attributes(every object can have differen value for this attributes0)
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x} ,{self.y})")


Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)  # yellow
print(Point.default_color)  # yellow
point.draw()  # Point (1 ,2)

another = Point(3, 5)
print(point.default_color)  # yellow
another.draw()  # Point (3 ,5)

#####################################################################################
# class vs Instance method


class Point:
    # instance method - called by instances(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class method
    # in runtime, python intrepreter will pass the Point class to cls, so it will becoem Point(0,0)
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # instance method
    def draw(self):
        print(f"Point ({self.x} ,{self.y})")


# same as below , but this always need to pass the contrustor
point = Point(0, 0)
# zero method are factory metohd, it always created a same Point(0,0)
point = Point.zero()
point.draw()  # Point (0 ,0)

#####################################################################################
# Magic method - have two underscore add beginning and end of name, and it will call by python automatically


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x} ,{self.y})")


point = Point(1, 2)
print(point)
# before not using __str__
# <__main__.Point object at 0x000002A49020FC70>
# namemodule.classname.addressofpointobjectinmemory

# after using __str
# (1, 2)

# convert Point obj to String
print(str(point))  # (1, 2)

# https://rszalski.github.io/magicmethods/

#####################################################################################
# Comparing object


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 2)
other = Point(1, 2)

print(point == other)  # False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)  # True

point = Point(10, 20)
other = Point(1, 2)
print(point > other)  # True
print(point < other)  # False (if use __gt__, python will figure out the __lt__)


# Performing Arithmetic Operation
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x, combined.y)  # 11 22

#####################################################################################
# Making Custom Container


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        # return an iterable object will give one item in each iteration
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)  # {'python': 3}

cloud["Java"] = 10
print(cloud.tags)  # {'python': 3, 'java': 10}
print(len(cloud))  # 2
print(cloud["python"])  # 3

for tag in cloud:
    print(tag)

# python
# java

#####################################################################################
# Private member
# self.__tags = {}
# __ is private
# f2 rename all
cloud2 = TagCloud()
cloud2.add("Python")
cloud2.add("python")
cloud2.add("python")
print(cloud2["PYTHON"])  # 3
# change tags to private ,so cannot access
print(cloud2.tags)
# {'python': 3, 'java': 10}
# print(cloud2.tags["PYTHON"])
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 236, in <module>
#     print(cloud.tags["PYTHON"])
# KeyError: 'PYTHON'


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # return an iterable object will give one item in each iteration
        return iter(self.__tags)


cloud2 = TagCloud()
cloud2.add("Python")
cloud2.add("python")
cloud2.add("python")
print(cloud2["PYTHON"])  # 3
# print(cloud2.tags)
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 270, in <module>
#     print(cloud2.tags)
# AttributeError: 'TagCloud' object has no attribute 'tags'

# Also got a way to access private in python

print(cloud2.__dict__)  # {'_TagCloud__tags': {'python': 3}}
print(cloud2._TagCloud__tags)  # {'python': 3}
#####################################################################################

# Propeties


class Product:
    def __init__(self, price):
        self.price = price


Product = Product(-50)
# not good to using contructor to initialize negative price
# we can use getter setter


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


# product = Product(-50)
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 308, in <module>
#     product = Product(-50)
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 297, in __init__
#     self.set_price(price)
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 304, in set_price
#     raise ValueError("Price cannot be negative")
# ValueError: Price cannot be negative

# property is a object sit in front of attribute allow us to get and set the value of attributes
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

    price = property(get_price, set_price)


product = Product(10)
print(product.price)  # 10
product.price = 20
print(product.price)  # 20


# we do not getter and setter be accessible
class Product:
    def __init__(self, price):
        self.__price = price
    # one solution is use __get_price
    # another

    @property
    def price(self):
        return self.__price

    # we can not need to set setter , only set getter
    # @price.setter
    # def price(self, value):
    #     if value < 0:
    #         raise ValueError("Price cannot be negative")
    #     self.__price = value


product = Product(10)
print(product.price)  # 10
# product.price = 20
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 343, in __init__
#     self.price = price
# AttributeError: can't set attribute 'price'

####################################################################################################################################################
# Inherintance - common behaviour in one class can inherit by other class


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal:Parent, Base
# Mammal:Child , Sub


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()  # eat
print(m.age)  # 1

####################################################################################################################################################
# The Object class
print(isinstance(m, Mammal))  # True
print(isinstance(m, Animal))  # True

# all the class inherit from object class
print(isinstance(m, object))  # True

print(issubclass(Mammal, Animal))  # True
print(issubclass(Mammal, object))  # True


####################################################################################################################################################
# Method overriding

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2

    def walk(self):
        print("walk")


m = Mammal()
print(m.weight)  # 2
# print(m.age)
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 428, in <module>
#     print(m.age)
# AttributeError: 'Mammal' object has no attribute 'age'

# m object do not have age attr cuz, Mammal contructor have called, so Animal contructor will not called, if Mammal class do not have contructor, then it will call the parent class contructor


# Use super to call the parent contructor
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2
        print("Mammal Constructor")

    def walk(self):
        print("walk")


m = Mammal()
# Animal Constructor
# Mammal Constructor
print(m.weight)  # 2
print(m.age)  # 1
####################################################################################################################################################

# Multi-level Inherintance - increase complexity and raise various problem


class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# chicken cannot fly,although chicken is Bird
# Employee - Person -LivindCreature - Thing : too complicated

# usually one level inheritance should be enough, dont multi level
####################################################################################################################################################
# Multiple Inheritance

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()  # Employee Greet
# Python intrepreter will run the first look at Manager class got greet or not , if not it will look at first base class then second base class

# sometime this are bad,cuz when change the order or two Base class will create issue
# if the two base class have nothing simmlariry, and you want the child class get the attr and method from both parent class , this is the time use multipler inheritance

# Good Example


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass

####################################################################################################################################################

# Good Example of Inheritance
# All exception class should end with Error(convention)


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


####################################################################################################################################################
# Abstract base class

# there are problem with above class, because we can create Stream object and call the method
stream = Stream()
stream.open()

# because stream itself confuse, what stream do we need to work here, file or network, it is better to use FileStream or NetworkStream class to create object
# if we dont want the parent can create the object, we can set the parent class to abstract
from abc import ABC, abstractmethod

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close")
        self.opened = False

    # abstract method no need implementaion
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    pass

# cannot instantiace
# stream = Stream()
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 602, in <module>
#     stream = Stream()
# TypeError: Can't instantiate abstract class Stream with abstract method read


# stream = MemoryStream()
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 613, in <module>
#     stream = MemoryStream()
# TypeError: Can't instantiate abstract class MemoryStream with abstract method read

# you must declare the read abstract method in MemoryStream


####################################################################################################################################################
# Polymorphism - many form
from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
isinstance(ddl, UIControl)  # True


textbox = TextBox()
draw([ddl, textbox])
# DropDownList
# TextBox

####################################################################################################################################################
# Duck Typing - no need base class also can, as long the class have draw method


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
isinstance(ddl, UIControl)  # True


textbox = TextBox()
draw([ddl, textbox])
# DropDownList
# TextBox

####################################################################################################################################################
# Extending Built it Type


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
# original method of string
print(text.capitalize())  # Python

# my method
print(text.duplicate())  # PythonPython


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")  # Append called

####################################################################################################################################################
# Data Classes - only data class


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
# Not using __eq__
# False - two object store in different memory location

# memory location of object
print(id(p1))
# 1859505954176
print(id(p2))
# 1859505954080

from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
print(p1.x)  # 1
p2 = Point(x=1, y=2)


# not need to implement magin method __eq__
print(p1 == p2)

# but we cannot immutable, we cannot modify it once we set it
# p1.x = 10
# Traceback (most recent call last):
#   File "c:\Users\ASUS\Desktop\Python\classes.py", line 742, in <module>
#     p1.x = 10
# AttributeError: can't set attribute

# if you want to change the value , create a new one
p1 = Point(x=10, y=20)
