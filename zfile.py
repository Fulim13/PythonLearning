from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")
# for path in Path("module/ecommerce").rglob("*.*"):
#     zip.write(path)
# zip.close()


# another method - with with method, with will auto close the file
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("module/ecommerce").rglob("*.*"):
#         zip.write(path)

# print the file name of zip file
with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("module/ecommerce/package.txt")
    print(info.file_size)  # 157
    print(info.compress_size)  # 157
    zip.extractall("extract")

# ['module/ecommerce/package.txt',
# 'module/ecommerce/__init__.py',
# 'module/ecommerce/customer/contact.py',
# 'module/ecommerce/customer/__init__.py',
# 'module/ecommerce/customer/__pycache__/contact.cpython-310.pyc',
# 'module/ecommerce/customer/__pycache__/__init__.cpython-310.pyc',
# 'module/ecommerce/shopping/sales.py',
# 'module/ecommerce/shopping/__init__.py',
# 'module/ecommerce/shopping/__pycache__/sales.cpython-310.pyc', '
# module/ecommerce/shopping/__pycache__/__init__.cpython-310.pyc',
# 'module/ecommerce/__pycache__/__init__.cpython-310.pyc']
