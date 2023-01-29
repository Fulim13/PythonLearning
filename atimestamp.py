import time

# current time in second
print(time.time())
# 1674986876.3065445


def send_emails():
    for i in range(10000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)  # 0.0009915828704833984
