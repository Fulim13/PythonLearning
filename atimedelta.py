from datetime import datetime, timedelta

dt1 = datetime(2023, 1, 1) + timedelta(days=1, seconds=10000)
print(dt1)  # 2023-01-02 02:46:40
dt2 = datetime.now()

# timedelete obj
duration = dt2 - dt1
print(duration)  # 28 days, 18:19:43.787606
print("days", duration.days)  # days 28
print("seconds", duration.seconds)  # seconds 66017
print("seconds", duration.total_seconds())  # 2485250.229492
