# INSTALL pipenv (pip + env)
# pip install pipenv

# USING PIPENV TO AUTOMATICALLY CREATE virtual environment

# pipenv install requests
# we will have new Pipfile and Pipfile.lock

# our virtual environment is not stored here
# pipenv --venv

# open the ve
# open C:\Users\ASUS\.virtualenvs\PythonLearning-ic4l0W3s


# store here
# C:\Users\ASUS\.virtualenvs\PythonLearning-ic4l0W3s

# activate VE
# pipenv shell

# deactivate
# exit

# VS CODE PYTHON VE
# https://code.visualstudio.com/docs/python/environments


# INSTALL DEPENDENCIES if dont have ve
# pipenv install

# excact version
# pipenv install --ignore--pipfile


# pipenv graph
# requests==2.28.2
#   - certifi [required: >=2017.4.17, installed: 2022.12.7]
#   - charset-normalizer [required: >=2,<4, installed: 3.0.1]
#   - idna [required: >=2.5,<4, installed: 3.4]
#   - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.14]

# Unistall
# pipenv uninstall requests

# download the exact version
# pipenv install requests==2.9.*

# update all package (with *)
# pipenv update --outdated

# Skipped Update of Package requests: 2.9.2 installed, 2.9.2 required (==2.9.* set in Pipfile),
# 2.28.2 available.
# All packages are up to date!

# change 2.9.* to 2.* in Pipfile

# update all package (with *)
# pipenv update --outdated

# Package 'requests' out-of-date: '==2.9.2' installed, '==2.28.2' available.

# update specify package
# pipenv  update requests
