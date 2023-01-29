from datetime import datetime
import time

# specify datetime
dt1 = datetime(2023, 1, 1)
print(dt1)  # 2023-01-01 00:00:00

# current datetime
dt2 = datetime.now()
print(dt2)  # 2023-01-29 18:15:05.688339

# convert string to date obj
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
print(dt)  # 2018-01-01 00:00:00

# convert timestamp to datatime obj
dt = datetime.fromtimestamp(time.time())
print(dt)  # 2023-01-29 18:15:05.703319

print(f"{dt.year}/{dt.month}")  # 2023/1

# convert dattime obj to timestamp
print(dt.strftime("%Y/%m"))  # 2023/01

# compare datetime
print(dt2 > dt1)  # True
