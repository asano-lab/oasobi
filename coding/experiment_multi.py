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
CPU_COUNT = os.cpu_count()


class RangeCheck(object):
    def __init__(self, low_limit=None, high_limit=None, vtype="integer"):
        self.min = low_limit
        self.max = high_limit
        self.type = vtype

    def __contains__(self, val):
        ret = True
        if self.min is not None:
            ret = ret and (val >= self.min)
        if self.max is not None:
            ret = ret and (val <= self.max)
        return ret

    def __iter__(self):
        low = self.min
        if low is None:
            low = "-inf"
        high = self.max
        if high is None:
            high = "+inf"
        l1 = self.type
        l2 = f" {low} <= x <= {high}"
        return iter((l1, l2))


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
    parser.add_argument(
        "-E", "--expected",
        help="符号なしでビット誤り数の期待値が一定になるようにループ数を動的に変える (デフォルト)",
        type=int, choices=RangeCheck(low_limit=4), default=400)
    parser.add_argument("-s", "--samples", help="試行回数", type=int, default=10)
    parser.add_argument("--static", help="静的にループ数を指定したい場合",
                        type=int)
    parser.add_argument("-T", "--threads", help="同時に動かすスレッド数. メインは含まず, デフォルトは制限なし.",
                        type=int, choices=RangeCheck(low_limit=1), default=0x7fffffff)
    args = parser.parse_args()

    subprocess.run(["make", "experiment"])

    if not os.path.isdir(DAT_DIR):
        os.mkdir(DAT_DIR)

    # 識別子
    timestamp = datetime.datetime.now(JST).strftime("%y%m%d%H%M%S")

    th_list = []
    t0 = time.time()
    # 検証する誤り率の配列
    e_prob_arr = np.logspace(-6, -0.5, 12)

    for e_prob in e_prob_arr:
        count = round(args.expected / (4 * e_prob))
        fnamew = f"dat/bes_p{e_prob:.4e}_c{count}_{timestamp}.csv"
        with open(fnamew, "w", encoding="UTF-8") as f:
            print("nothing,repetition,hamming", file=f)
        for j in range(args.samples):
            tmp_th = ExpThred(e_prob, count, fnamew,
                              f"th{e_prob:.4e}_{j}")
            tmp_th.start()
            th_list.append(tmp_th)
            while threading.active_count() >= args.threads + 1:
                time.sleep(1)
    while threading.active_count() > 1:
        time.sleep(1)
    print(time.time() - t0)


if __name__ == "__main__":
    main()
