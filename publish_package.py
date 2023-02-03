# Step 1 : Log in or Register account at
# https://pypi.org/

# Step 2: Install package needed for public package
# pip install setuptools wheel twine

# Step 3: Create new package (limpdf)
# mkdir limpdf
# cd lim pdf

# see limpdf folder

# Step 4:
# Create data , test and limpdf folder (packages folder)
# setup.py to setup publish, adn README for description, LICENSE in https://choosealicense.com/

# Step 5 :
# generate distribution package
# python setup.py sdist bdist_wheel 
# sdist - source distribution , bdist_wheel - build distribution

# Step 6: upload package
# twine upload dist/*