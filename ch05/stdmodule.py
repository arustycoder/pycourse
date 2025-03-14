import time
now = time.localtime()
print(now.tm_hour,":",now.tm_min, ":", now.tm_sec, sep="")
time.sleep(1)
now = time.localtime()
print(now.tm_hour,":",now.tm_min, ":", now.tm_sec, sep="")

import random
num_seconds = random.randint(0, 10)
#print(now.tm_hour,":",now.tm_min, ":", now.tm_sec, sep="")
print("Sleeping for another", num_seconds, "seconds")
time.sleep(num_seconds)
now = time.localtime()
print(now.tm_hour,":",now.tm_min, ":", now.tm_sec, sep="")

