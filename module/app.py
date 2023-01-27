from ecommerce.shopping.sales import calc_shipping, calc_tax
from ecommerce.shopping import sales


# not good use *
# from sales import *

calc_shipping()
calc_tax()

sales.calc_shipping()
sales.calc_tax()


print(dir(sales))

# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_shipping', 'calc_tax']

print(sales.__name__)  # ecommerce.shopping.sales
print(sales.__package__)  # ecommerce.shopping
print(sales.__file__)
# c:\Users\ASUS\Desktop\Python\module\ecommerce\shopping\sales.py


############################################
# when we run module/app.py, we will see __pycache__/sales.cpython-310.pyc
# sales.cpython-310.pyc is a complie version of sales module that we import to app.py
# the reason python store this complie file is to speed up module loading, so python will see whether it have the complie file, if got, python will load that file
# so it will skip compilation step , faster loading of module
# so it will check the datatime of the complie sales file and the sales module file, if the sales module file the modified datetime is older than complie sales module, it will run the compile file , else it will rerun the sale module and put the new complie file  back
# note that we dont have the compile app, because python always rerun the file (app.py) we run in command line , python module/app.py
