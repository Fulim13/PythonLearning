import random
import string

# return value [0,1) - not include 1
print(random.random())  # 0.4583340232831056

# generate value [1,10] - include both 1, 10
print(random.randint(1, 10))  # 6

# select one value from list of choice(iterables)
print(random.choice([1, 2, 3, 4]))  # 3

# select list of k value from list of choice (iterables)
print(random.choices([1, 2, 3, 4], k=2))  # [4, 1]


print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# generate random password
combined = string.ascii_letters + string.digits + string.punctuation
print("".join(random.choices(combined, k=8)))
# NzMI,&E1


# shuffering list
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)  # [2, 1, 4, 3]
