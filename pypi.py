# https://pypi.org/ - package for python, like node package in js

# RUN THE COMMAND
# WINDOW pip
# MAC pip3

# INSTALL
# pip install requests


# pip is version different from python, so we need to update
# UPDATE
# pip install --upgrade pip

# package installed in my machine
# pip list

# Package              Version
# -------------------- -----------
# argon2-cffi          21.3.0
# argon2-cffi-bindings 21.2.0
# astroid              2.11.5
# asttokens            2.0.5
# attrs                21.4.0
# autopep8             2.0.1
# backcall             0.2.0
# beautifulsoup4       4.11.1
# bleach               5.0.0
# certifi              2022.5.18.1
# cffi                 1.15.0
# charset-normalizer   2.0.12
# colorama             0.4.4
# debugpy              1.6.0
# decorator            5.1.1
# defusedxml           0.7.1
# dill                 0.3.5
# distlib              0.3.6
# entrypoints          0.4
# et-xmlfile           1.1.0
# executing            0.8.3
# fastjsonschema       2.15.3
# filelock             3.9.0
# flake8               6.0.0
# idna                 3.3
# ipykernel            6.13.0
# ipython              8.3.0
# ipython-genutils     0.2.0
# isort                5.10.1
# jedi                 0.18.1
# Jinja2               3.1.2
# jsonschema           4.5.1
# jupyter-client       7.3.1
# jupyter-core         4.10.0
# jupyterlab-pygments  0.2.2
# lazy-object-proxy    1.7.1
# MarkupSafe           2.1.1
# matplotlib-inline    0.1.3
# mccabe               0.7.0
# mistune              0.8.4
# mypy                 0.991
# mypy-extensions      0.4.3
# nbclient             0.6.3
# nbconvert            6.5.0
# nbformat             5.4.0
# nest-asyncio         1.5.5
# notebook             6.4.11
# openpyxl             3.0.10
# packaging            21.3
# pandocfilters        1.5.0
# parso                0.8.3
# pickleshare          0.7.5
# pip                  22.3.1
# pipenv               2022.12.19
# platformdirs         2.5.2
# prometheus-client    0.14.1
# prompt-toolkit       3.0.29
# psutil               5.9.0
# pure-eval            0.2.2
# pycodestyle          2.10.0
# pycparser            2.21
# pyflakes             3.0.1
# Pygments             2.12.0
# pylint               2.13.9
# pyparsing            3.0.9
# pyrsistent           0.18.1
# python-dateutil      2.8.2
# pywin32              304
# pywinpty             2.0.5
# pyzmq                23.0.0
# requests             2.27.1
# Send2Trash           1.8.0
# setuptools           58.1.0
# six                  1.16.0
# soupsieve            2.3.2.post1
# stack-data           0.2.0
# terminado            0.15.0
# tinycss2             1.1.1
# tomli                2.0.1
# tornado              6.1
# traitlets            5.2.1.post0
# typing_extensions    4.4.0
# urllib3              1.26.9
# virtualenv           20.17.1
# virtualenv-clone     0.5.7
# wcwidth              0.2.5
# webencodings         0.5.1
# wrapt                1.14.1

# semantic version, first one is major version, second is minor version, thrid is patch or bugfix


# INSTALL SPECIFY VERSION
# pip install requests==2.9.0

# INSTALL LATEST VERSION (PATCH) OF 2.9
# pip install requests==2.9.*
# same as
# pip install requests~=2.9.0

# INSTALL LATEST VERSION (MINOR)
# pip install requests==2.*

# UNINSTALL PACKAGE
# pip uninstall requests

# now we can use the package
import requests
response = requests.get("http://google.com")
print(response)  # <Response [200]> - success
