# intra
# from ecommerce.customer import contact
# abs - recommend using

# relative
# from ..customer import contact

# contact.contact_customer()

import sys
print(sys.path)
# ['c:\\Users\\ASUS\\Desktop\\PythonLearning\\module\\ecommerce\\shopping', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib', 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310', 'C:\\Users\\ASUS\\.virtualenvs\\PythonLearning-ic4l0W3s', 'C:\\Users\\ASUS\\.virtualenvs\\PythonLearning-ic4l0W3s\\lib\\site-packages']
# it only find in shopping folder, so it can not found the package, so you need to download it


def calc_tax():
    pass


def calc_shipping():
    pass


print("Sales initialized", __name__)

# Sales initialized __main__


# this only run when i run this file,so that when i run the main, this code will not run
if __name__ == "__main__":
    print("Sales started")
    calc_tax
