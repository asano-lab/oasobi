#!/usr/bin/env python3
import subprocess
import threading
import argparse
import time
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="1試行あたりのループ数", type=int, default=10000)
    parser.add_argument("-s", "--samples", help="試行回数", type=int, default=10)
    args = parser.parse_args()

    subprocess.run(["make", "experiment"])

    t0 = time.time()
    # 検証する誤り率の配列
    e_prob_arr = np.logspace(-6, -0.5, 12)
    for e_prob in e_prob_arr:
        fnamew = f"dat/bes_p{e_prob:.4e}_c{args.count}.csv"
        with open(fnamew, "w", encoding="UTF-8") as f:
            print("nothing,repetition,hamming", file=f)
        for j in range(10):
            thread_name = f"th{e_prob:.4e}_{j}"
            print(f"{thread_name} start.")
            t1 = time.time()
            subprocess.run(["./experiment", fnamew, f"{e_prob}", f"{args.count}"])
            print(f"{thread_name} stop. ({time.time() - t1:.2f} sec)")
    while threading.active_count() > 1:
        time.sleep(1)
    print(time.time() - t0)

if __name__ == "__main__":
    main()
