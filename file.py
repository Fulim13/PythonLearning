from pathlib import Path
from time import ctime
import shutil

path = Path("module/ecommerce/__init__.py")

print(path.exists())  # True
# path.rename("init.txt")
# path.unlick()

print(path.stat())
# os.stat_result(st_mode=33206, st_ino=51509920738088448, st_dev=1652677552, st_nlink=1, st_uid=0, st_gid=0,
# st_size=33, st_atime=1674983231, st_mtime=1674828118, st_ctime=1674826942)
# size, last acess time , last modified time ,  creation time

print(ctime(path.stat().st_ctime))
# Fri Jan 27 21:42:22 2023

# take care open and closing the file, you dont need to do it manuarlly like file.close
# return content of the file as byte object to representing binary data
print(path.read_bytes())  # b'print("Eccommerce initialized")\r\n'
# return content of the file as string
print(path.read_text())  # print("Eccommerce initialized")

# path.write_text("....")
# path.write_bytet("")

source = Path("module/ecommerce/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)
target.write_text(source.read_text())
