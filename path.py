from pathlib import Path

# WINDOW
# r - raw string, \ is not a ecape character
# Path("C:\\Program Files\\Microsoft")
# Path(r"C:\Program Files\Microsoft")

# MAC / LINUX
# Path("/usr/local/bin")

# represent current folder
print(Path())  # .


# relative path
print(Path("ecommerce/__init.py"))  # ecommerce\__init.py


# combine path obj
print(Path() / Path("ecommmerce"))  # ecommmerce
print(Path() / "ecommerce" / "__init__.py")  # ecommerce\__init__.py


# home directory of current user
print(Path.home())  # C:\Users\ASUS


path = Path("module/ecommerce/__init__.py")

# check the file/folder exist or not
print(path.exists())  # True
print(path.is_file())  # True
print(path.is_dir())  # False

# file name
print(path.name)  # __init__.py

# file name without extension
print(path.stem)  # __init__


# extension
print(path.suffix)  # .py

# parent of the path
print(path.parent)  # module\ecommerce

# change the file name
path = path.with_name("file.txt")
print(path)  # module\ecommerce\file.txt


print(path.absolute())
# c:\Users\ASUS\Desktop\Python\module\ecommerce\file.txt

path = path.with_suffix(".java")
print(path)  # module\ecommerce\file.java
