# intra
# abs - recommend using
from ecommerce.customer import contact

# relative
# from ..customer import contact

contact.contact_customer()

#


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
