#!/usr/bin/python3
import sys
import time

try:
    for i in range(1000000):
        print(i)
        print(sys.version)
        time.sleep(1)

except KeyboardInterrupt:
    pass

sys.exit(i & 0xff)
