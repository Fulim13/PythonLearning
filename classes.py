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
        self.price = price
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
