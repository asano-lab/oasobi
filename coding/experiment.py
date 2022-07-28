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
    def __init__(self, e_prob, count, name=""):
        super().__init__()
        self.name = name
        self.e_prob = e_prob
        self.count = count
        self.fname = f"dat/bes_p{self.e_prob:.4e}_s{self.count}.csv"
        self.daemon = True
    
    def run(self):
        subprocess.run(["./experiment", self.fname, f"{self.e_prob}", f"{self.count}"])

def main():
    th_list = []
    t0 = time.time()
    for i in range(1):
        tmp_th = MyThread(0.01, 1000000, str(i))
        tmp_th.run()
    while threading.active_count() > 1:
        time.sleep(1)
    print(time.time() - t0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="ループ数", type=int, default=10000)
    args = parser.parse_args()

    subprocess.run(["make", "experiment"])
    # print(args.count)
    main()
    # print(np.logspace(-6, -0.5, 12))
