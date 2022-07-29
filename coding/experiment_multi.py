#!/usr/bin/env python3
import datetime
import os
import subprocess
import threading
import argparse
import time
import numpy as np

SRC_DIR = os.path.abspath(os.path.dirname(__file__))
DAT_DIR = f"{SRC_DIR}/dat/"

JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")


class ExpThred(threading.Thread):
    def __init__(self, e_prob, count, fnamea, name=""):
        super().__init__()
        self.e_prob = e_prob
        self.count = count
        self.fnamea = fnamea
        self.name = name
        self.daemon = True

    def run(self):
        print(f"{self.name} start.")
        t0 = time.time()
        subprocess.run(["./experiment", self.fnamea,
                       f"{self.e_prob}", f"{self.count}"])
        print(f"{self.name} stop. ({time.time() - t0:.2f} sec)")


def main():
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="1試行あたりのループ数",
                        type=int, default=10000)
    parser.add_argument("-s", "--samples", help="試行回数", type=int, default=10)
    args = parser.parse_args()

    subprocess.run(["make", "experiment"])

    if not os.path.isdir(DAT_DIR):
        os.mkdir(DAT_DIR)

    timestamp = datetime.datetime.now(JST).strftime("%y%m%d%H%M%S")
    print(timestamp)
    return -1

    th_list = []
    t0 = time.time()
    # 検証する誤り率の配列
    e_prob_arr = np.logspace(-6, -0.5, 12)
    for e_prob in e_prob_arr:
        fnamew = f"dat/bes_p{e_prob:.4e}_c{args.count}.csv"
        with open(fnamew, "w", encoding="UTF-8") as f:
            print("nothing,repetition,hamming", file=f)
        for j in range(args.samples):
            tmp_th = ExpThred(e_prob, args.count, fnamew,
                              f"th{e_prob:.4e}_{j}")
            tmp_th.start()
            th_list.append(tmp_th)
    while threading.active_count() > 1:
        time.sleep(1)
    print(time.time() - t0)


if __name__ == "__main__":
    main()
