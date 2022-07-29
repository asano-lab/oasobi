#!/usr/bin/env python3
import re
import glob
import subprocess
import argparse
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="1試行あたりのループ数",
                        type=int, default=10000)
    args = parser.parse_args()

    fnamer_list = glob.glob(f"dat/*c{args.count}.csv")
    # print(fnamer_list)
    fnamer_dict = {}
    for fnamer in fnamer_list:
        mg = re.findall(r'p([0-9\.e\-]+)_c', fnamer)
        tmp_dict = {}
        tmp_dict["path"] = fnamer
        tmp_dict["df"] = pd.read_csv(fnamer) / (4 * args.count)
        fnamer_dict[mg[0]] = tmp_dict
    # print(fnamer_dict)
    sorted_keys = sorted(fnamer_dict.keys(), key=float)
    p_bsc = [float(i) for i in sorted_keys]
    # print(p_bsc)
    col_list = tmp_dict["df"].columns.tolist()

    col_dict = {i: {"mean": [], "error": []} for i in col_list}

    fig = plt.figure(figsize=(12, 8))
    for i, k in enumerate(sorted_keys):
        e_prob_df = fnamer_dict[k]["df"]
        # print(e_prob_df)
        validity_sr = (e_prob_df != 0).any()
        # print(validity_df)
        for col in e_prob_df.columns:
            print(col)
            print(validity_sr[col])


if __name__ == "__main__":
    main()
