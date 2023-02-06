Python have language itself and implementation
language is the rules(like grammar to write python code)
implementation is the program understand those rules and execute

- default implementation is CPython
  - other implementation include Jython(Written in JAVA), IRONPYTHON (C#), PyPy(Subset of Python)

<!--  -->

C > Compiler > Machine Code > Processor - But the Machine Code specific to the type of Processor,OS
JAVA > Compiler > JavaByteCode > (WINDOW JVM > WINDOW MACHINE)JVM(RUNTIME) > Machine Code - so is code independent for JavaByteCode ((WINDOW JVM > WINDOW MACHINE CODE))

Python > Cpython(Compiler) - Check Syntax > PythonByteCode > Python Virtual Machine(Interpreter) (Run)> Machine Code

Other implementation
Python > Jython > JavaBytecode > JVM > Machine Code

- this lead to you can Write Java Code in Python, because the result for Python and Java both will become JavaBytecode
