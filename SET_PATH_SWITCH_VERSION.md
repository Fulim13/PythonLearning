# Set path and Switch Between Different Version (WINDOW)

# STEP 1 : INSTALL PYTHON VERSION you want to download

[Welcome to Python.org](https://www.python.org/)

you can run the python file directly in the command line by typing

```bash
> C:\Users\ASUS\AppData\Local\Programs\Python\Python310\python
```

Go to environment variable > User variable > Path

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3bb3e87f-8249-4353-a406-ad0b87527a66/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/98cf36bc-c6ea-4128-8261-75e0c76fc406/Untitled.png)

because the python 310 is above python 311

Scripts - is to run pip.exe

```bash
> python # go to python shell
import sys
sys.executable # to konw which python is running
quit()
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c42e1026-8f79-4e5e-bbbc-ec7fd595d54b/Untitled.png)

```bash
echo %path% #all the path
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/50675a2c-fd0b-4878-90a9-f22f1b7fe81c/Untitled.png)

when cannot import django

```bash
you need to use
pip show django
then the folder must be same as the sys.executable
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d660cdbf-451b-4752-8620-64d4211ce258/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1d93bd62-3778-4bf9-98b4-73bc1b725a80/Untitled.png)
