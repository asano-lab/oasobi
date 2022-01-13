#!/usr/bin/python3
import sys
import time

try:
    while True:
        print(sys.version)
        time.sleep(1)

except KeyboardInterrupt:
    pass

sys.exit(-1)
