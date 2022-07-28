#!/usr/bin/env python3
import subprocess
import threading
import argparse
import time
import numpy as np


class MyThread(threading.Thread):
    def __init__(self, e_prob, count, fnamea, name=""):
        super().__init__()
        self.e_prob = e_prob
        self.count = count
        self.fnamea = fnamea
        self.name = name
        self.daemon = True
    
    def run(self):
        print(f"{self.name} start.")
        subprocess.run(["./experiment", self.fnamea, f"{self.e_prob}", f"{self.count}"])
        print(f"{self.name} stop.")

def main():
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="ループ数", type=int, default=10000)
    args = parser.parse_args()

    subprocess.run(["make", "experiment"])

    th_list = []
    t0 = time.time()
    e_prob_arr = [0.01]
    for e_prob in e_prob_arr:
        fnamew = f"dat/bes_p{e_prob:.4e}_c{args.count}.csv"
        for j in range(10):
            tmp_th = MyThread(e_prob, args.count, fnamew, f"th{e_prob:.4e}_{j}")
            tmp_th.run()
            th_list.append(tmp_th)
    while threading.active_count() > 1:
        time.sleep(1)
    print(time.time() - t0)

if __name__ == "__main__":
    # print(args.count)
    main()
    # print(np.logspace(-6, -0.5, 12))
