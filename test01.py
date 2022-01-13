#!/usr/bin/python3
import sys
import time
import random as rd

r = 0

try:
    for i in range(1000000):
        time.sleep(1)
        print(i)
        print(sys.version)
        r = rd.randint(0, 19)
        print(r)
        if r == 0:
            break

except KeyboardInterrupt:
    pass

sys.exit(i & 0xff)
