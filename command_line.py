import sys

# RUN THIS COMMAND
# python command_line.py -a -b -c

print(sys.argv)
# ['command_line.py', '-a', '-b', '-c']

if len(sys.argv) == 1:
    print("USAGE: pthon app.py <password>")
else:
    password = sys.argv[1]
    print("Password", password)
