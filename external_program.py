import subprocess
# RUN python external_program.py at bash shell

completed = subprocess.run(["ls", "-l"])
print(type(completed))  # <class 'subprocess.CompletedProcess'>
print("args", completed.args)  # args ['ls', '-l']
print("return code", completed.returncode)  # return code 0
# 0 means sucess, any nonzero value is failed
print("stderr", completed.stderr)  # stderr None
# standard Error are none
print("stdout", completed.stdout)  # stdout None


completed = subprocess.run(["ls", "-l"], capture_output=True)
print("stdout", completed.stdout)
# stdout b'total 150\n-rw-r--r-- 1 ASUS 197609   808 Jan 29 18:32 acsv.py\n-rw-r--r-- 1 ASUS 197609   623 Jan 29 18:32 adatetime.py\n-rw-r--r-- 1 ASUS 197609
#   826 Jan 29 18:32 ajson.py\n-rw-r--r-- 1 ASUS 197609   978 Jan 29 22:59 arandom.py\n-rw-r--r-- 1 ASUS 197609  1122 Jan 29 18:32 asqlite.py\n-rw-r--r-- 1 ASUS 197609   407 Jan 29 18:32 atimedelta.py\n-rw-r--r-- 1 ASUS 197609   274 Jan 29 18:32 atimestamp.py\n-rw-r--r-- 1 ASUS 197609 19081 Jan 29 18:32 classes.py\n-rw-r--r-- 1 ASUS 197609   268 Jan 29 23:40 command_line.py\n-rw-r--r-- 1 ASUS 197609   348 Jan 29 23:40 content.txt\n-rw-r--r-- 1 ASUS 197609  4300 Jan
# 29 18:32 control.py\n-rw-r--r-- 1 ASUS 197609    52 Jan 29 18:32 data.csv\n-rw-r--r-- 1 ASUS 197609 14562 Jan 29 18:32 data_structures.py\n-rw-r--r-- 1 ASUS 197609 12288 Jan 29 18:32 db.sqlite3\n-rw-r--r-- 1 ASUS 197609   756 Jan 29 18:32 debugging.py\n-rw-r--r-- 1 ASUS 197609  1727 Jan 29 18:32 directories.py\n-rw-r--r-- 1 ASUS 197609  4049 Jan 29 18:32 exception.py\n-rw-r--r-- 1 ASUS 197609   528 Jan 29 23:47 external_program.py\ndrwxr-xr-x 1 ASUS 197609     0 Jan 29 18:32 extract\n-rw-r--r-- 1 ASUS 197609  1064 Jan 29 18:32 file.py\n-rw-r--r-- 1 ASUS 197609  3707 Jan 29 18:32 files.zip\n-rw-r--r-- 1 ASUS 197609  2822 Jan 29 18:32 function.py\ndrwxr-xr-x 1 ASUS 197609     0 Jan 29 18:32 module\n-rw-r--r-- 1 ASUS 197609   102 Jan 29 18:32 movies.json\n-rw-r--r-- 1 ASUS 197609    90 Jan 29 23:01 open_browser.py\n-rw-r--r-- 1 ASUS 197609  1223 Jan 29 18:32 path.py\n-rw-r--r-- 1 ASUS 197609  4244 Jan 29 18:32 primitive.py\n-rw-r--r-- 1 ASUS 197609   309 Jan 29 18:32 README.md\n-rw-r--r-- 1 ASUS 197609  1039 Jan 29 23:30 send_email.py\n-rw-r--r-- 1 ASUS 197609   134 Jan 29 23:35 templates.html\n-rw-r--r-- 1 ASUS 197609  1240 Jan 29 23:36 templates.py\n-rw-r--r-- 1 ASUS 197609  1219 Jan 29 18:32 zfile.py\n-rw-r--r-- 1 ASUS 197609  9987 Jan 29 23:29 zoro.png\n'

# b- binary

completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("stdout", completed.stdout)
# stdout total 153
# -rw-r--r-- 1 ASUS 197609   808 Jan 29 18:32 acsv.py
# -rw-r--r-- 1 ASUS 197609   623 Jan 29 18:32 adatetime.py
# -rw-r--r-- 1 ASUS 197609   826 Jan 29 18:32 ajson.py
# -rw-r--r-- 1 ASUS 197609   978 Jan 29 22:59 arandom.py
# -rw-r--r-- 1 ASUS 197609  1122 Jan 29 18:32 asqlite.py
# -rw-r--r-- 1 ASUS 197609   407 Jan 29 18:32 atimedelta.py
# -rw-r--r-- 1 ASUS 197609   274 Jan 29 18:32 atimestamp.py
# -rw-r--r-- 1 ASUS 197609 19081 Jan 29 18:32 classes.py
# -rw-r--r-- 1 ASUS 197609   268 Jan 29 23:40 command_line.py
# -rw-r--r-- 1 ASUS 197609   348 Jan 29 23:40 content.txt
# -rw-r--r-- 1 ASUS 197609  4300 Jan 29 18:32 control.py
# -rw-r--r-- 1 ASUS 197609    52 Jan 29 18:32 data.csv
# -rw-r--r-- 1 ASUS 197609 14562 Jan 29 18:32 data_structures.py
# -rw-r--r-- 1 ASUS 197609 12288 Jan 29 18:32 db.sqlite3
# -rw-r--r-- 1 ASUS 197609   756 Jan 29 18:32 debugging.py
# -rw-r--r-- 1 ASUS 197609  1727 Jan 29 18:32 directories.py
# -rw-r--r-- 1 ASUS 197609  4049 Jan 29 18:32 exception.py
# -rw-r--r-- 1 ASUS 197609  2601 Jan 29 23:48 external_program.py
# drwxr-xr-x 1 ASUS 197609     0 Jan 29 18:32 extract
# -rw-r--r-- 1 ASUS 197609  1064 Jan 29 18:32 file.py
# -rw-r--r-- 1 ASUS 197609  3707 Jan 29 18:32 files.zip
# -rw-r--r-- 1 ASUS 197609  2822 Jan 29 18:32 function.py
# drwxr-xr-x 1 ASUS 197609     0 Jan 29 18:32 module
# -rw-r--r-- 1 ASUS 197609   102 Jan 29 18:32 movies.json
# -rw-r--r-- 1 ASUS 197609    90 Jan 29 23:01 open_browser.py
# -rw-r--r-- 1 ASUS 197609  1223 Jan 29 18:32 path.py
# -rw-r--r-- 1 ASUS 197609  4244 Jan 29 18:32 primitive.py
# -rw-r--r-- 1 ASUS 197609   309 Jan 29 18:32 README.md
# -rw-r--r-- 1 ASUS 197609  1039 Jan 29 23:30 send_email.py
# -rw-r--r-- 1 ASUS 197609   134 Jan 29 23:35 templates.html
# -rw-r--r-- 1 ASUS 197609  1240 Jan 29 23:36 templates.py
# -rw-r--r-- 1 ASUS 197609  1219 Jan 29 18:32 zfile.py
# -rw-r--r-- 1 ASUS 197609  9987 Jan 29 23:29 zoro.png


completed = subprocess.run(["python", "other.py"],
                           capture_output=True, text=True)
print(type(completed))  # <class 'subprocess.CompletedProcess'>
print("args", completed.args)  # args ['python', 'other.py']
print("return code", completed.returncode)  # return code 0
# 0 means sucess, any nonzero value is failed
print("stderr", completed.stderr)  # stderr
# standard Error are none
print("stdout", completed.stdout)  # stdout Here is complicated script


completed = subprocess.run(["false"],
                           capture_output=True, text=True)
print(type(completed))  # <class 'subprocess.CompletedProcess'>
print("args", completed.args)  # args ['args ['false']]
print("return code", completed.returncode)  # return code 1
# 0 means sucess, any nonzero value is failed
print("stderr", completed.stderr)  # stderr
# standard Error are none
print("stdout", completed.stdout)  # stdout
if completed.returncode != 0:
    print(completed.stderr)
    print("Error")  # Error

try:
    completed = subprocess.run(["false"],
                               capture_output=True, text=True, check=True)
    print(type(completed))  # <class 'subprocess.CompletedProcess'>
    print("args", completed.args)  # args ['args ['false']]
    print("return code", completed.returncode)  # return code 1
    # 0 means sucess, any nonzero value is failed
    print("stderr", completed.stderr)  # stderr
    # standard Error are none
    print("stdout", completed.stdout)  # stdout
except subprocess.CalledProcessError as ex:
    print(ex)  # Command '['false']' returned non-zero exit status 1.
