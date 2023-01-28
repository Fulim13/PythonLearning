from pathlib import Path

path = Path("module/ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("module/ecoommerce2

print(path.iterdir())
# <generator object Path.iterdir at 0x00000283CA120510>
# generator obj - return new value every time it iterate,
# large list of item - generator

for p in path.iterdir():
    print(p)

# module\ecommerce\customer
# module\ecommerce\package.txt
# module\ecommerce\shopping
# module\ecommerce\__init__.py
# module\ecommerce\__pycache__

paths = [p for p in path.iterdir()]
print(paths)
# [WindowsPath('module/ecommerce/customer'),
# WindowsPath('module/ecommerce/package.txt'),
#  WindowsPath('module/ecommerce/shopping'),
# WindowsPath('module/ecommerce/__init__.py'),
# WindowsPath('module/ecommerce/__pycache__')]

# get an array of WindowPath object - Path class we import is a base class of WindowPath and PosizPath(Linux base)

filter_dir_paths = [p for p in path.iterdir() if p.is_dir()]
print(filter_dir_paths)
# [WindowsPath('module/ecommerce/customer'),
#  WindowsPath('module/ecommerce/shopping'),
# WindowsPath('module/ecommerce/__pycache__')]

# can  search file , and put the pattern you want to search

py_files = [p for p in path.glob("*.py")]
print(py_files)
# [WindowsPath('module/ecommerce/__init__.py')]

# recursive search file
py_files = [p for p in path.rglob("*.py")]
print(py_files)
# [WindowsPath('module/ecommerce/__init__.py'),
# WindowsPath('module/ecommerce/customer/contact.py'),
# WindowsPath('module/ecommerce/customer/__init__.py'),
# WindowsPath('module/ecommerce/shopping/sales.py'),
# WindowsPath('module/ecommerce/shopping/__init__.py')]
