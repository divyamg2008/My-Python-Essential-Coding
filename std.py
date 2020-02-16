import sys
import os
import random
import datetime
v = sys.version_info
print(v)
print(*v)
print(sys.platform)
print(os.name)
print(os.getenv('PATH'))
print(os.getcwd())
print(os.urandom(20).hex())
print(random.random())
print(random.randint(1,100))

x = list(range(2,90,10))
print(x)
random.shuffle(x)
print(x)
now = datetime.datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second)