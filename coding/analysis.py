#!/usr/bin/env python3
import re
import glob
import subprocess
import argparse
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import pyper

r = pyper.R(use_pandas=True)


def t_test_R(d1, d2):
    r.assign("d1", d1)
    r.assign("d2", d2)
    # print(r("summary(d1)"))
    # print(r("summary(d2)"))
    d1_t_result = r("t.test(d1)")
    # print(d1_t_result)
    mg1 = re.findall(
        r'interval:\n *([e\d\.\-]+) ([e\d\.\-]+).*\nsample', d1_t_result)
    mg2 = re.findall(r'mean of x.*\n *([e\d\.\-]+)', d1_t_result)
    sample_mean = float(mg2[0])
    if mg1:
        le = float(mg1[0][0])
        ue = float(mg1[0][1])
    else:
        le = np.nan
        ue = np.nan
    print(sample_mean, le, ue)
    # print(d1_t_result.split(" "))


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

    for i, k in enumerate(sorted_keys):
        e_prob_df = fnamer_dict[k]["df"]
        t_test_R(e_prob_df["repetition"], e_prob_df["hamming"])
        # print(e_prob_df)
        validity_sr = (e_prob_df != 0).any()
        for col in e_prob_df.columns:
            # print(sample_var)
            if validity_sr[col]:
                sample_mean = e_prob_df[col].mean()
                sample_var = stats.tvar(e_prob_df[col])
                error_interval = stats.norm.interval(
                    alpha=0.95, loc=0, scale=np.sqrt(sample_var/e_prob_df[col].size)
                )
                sample_error = error_interval[1]
            else:
                sample_mean = np.nan
                sample_error = np.nan
            col_dict[col]["mean"].append(sample_mean)
            col_dict[col]["error"].append(sample_error)

    print(col_dict)
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(p_bsc, col_dict["repetition"]["mean"])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid()

    # plt.show()


if __name__ == "__main__":
    main()
