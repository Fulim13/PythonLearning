# Set path and Switch Between Different Version (WINDOW)

# STEP 1 : INSTALL PYTHON VERSION you want to download

[Welcome to Python.org](https://www.python.org/)

you can run the python file directly in the command line by typing

```bash
> C:\Users\ASUS\AppData\Local\Programs\Python\Python310\python
```

Go to environment variable > User variable > Path

![Untitled](https://github.com/Fulim13/PythonLearning/tree/main/image/env.png?raw=true)

![Untitled](https://github.com/Fulim13/PythonLearning/tree/main/image/pythonversion.png?raw=true)

because the python 310 is above python 311

Scripts - is to run pip.exe

```bash
> python # go to python shell
import sys
sys.executable # to konw which python is running
quit()
```

![Untitled](https://github.com/Fulim13/PythonLearning/tree/main/image/sysexecutable.png?raw=true)

```bash
echo %path% #all the path
```

![Untitled](https://github.com/Fulim13/PythonLearning/tree/main/image/echoPath.png?raw=true)

when cannot import django

```bash
you need to use
pip show django
then the folder must be same as the sys.executable
```

![Untitled](https://github.com/Fulim13/PythonLearning/tree/main/image/pipshow.png?raw=true)

![Untitled](https://github.com/Fulim13/PythonLearning/tree/main/image/sysexecutable_highlight.png?raw=true)
