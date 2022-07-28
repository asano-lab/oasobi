#!/usr/bin/env python3
import subprocess
import time

subprocess.run(["make", "experiment"])
subprocess.run(["./experiment", "0"])
# print("あいうえお")
