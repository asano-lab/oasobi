#!/usr/bin/env python3
import re
import glob
import subprocess
import argparse
import time
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="1試行あたりのループ数", type=int, default=10000)
    args = parser.parse_args()

    fnamer_list = glob.glob(f"dat/*c{args.count}.csv")
    # print(fnamer_list)
    fnamer_dict = {}
    for fnamer in fnamer_list:
        mg = re.findall(r'p([0-9\.e\-]+)_c', fnamer)
        fnamer_dict[fnamer] = float(mg[0])
    print(fnamer_dict)

if __name__ == "__main__":
    main()
