#!/usr/bin/env python3
import subprocess
import threading
import argparse
import time
import numpy as np

def fibo(x):
    if x <= 0:
        y = 0
    elif x == 1:
        y = 1
    else:
        y = fibo(x - 2) + fibo(x - 1)
    return y

class MyThread(threading.Thread):
    def __init__(self, name=""):
        super().__init__()
        self.setName(name)
        # self.daemon = True
    
    def run(self):
        print(self.name, fibo(31))

def main():
    th_list = []
    t0 = time.time()
    print(time.time() - t0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="ループ数", type=int, default=10000)
    args = parser.parse_args()
    # print(args.count)
    # main()
    print(np.logspace(-6, -0.5, 12))
