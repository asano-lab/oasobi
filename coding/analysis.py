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

COLORS = [
    "#1f77b4", "#ffa500", "#32cd32", "#fa8072",
    "#20b2aa", "#adff2f", "#800080", "#8b4513"
]


def t_test_single(d):
    r.assign("d", d)
    t_result = r("t.test(d)")
    # print(t_result)
    mg1 = re.findall(
        r'interval:\n *([e\d\.\-]+) ([e\d\.\-]+).*\nsample', t_result)
    mg2 = re.findall(r'mean of x.*\n *([e\d\.\-]+)', t_result)
    mg3 = re.findall(r'p-value [<=] ([e\d\.\-]+)', t_result)
    sample_mean = float(mg2[0])
    if mg1:
        le = float(mg1[0][0])
        ue = float(mg1[0][1])
        # print(ue - sample_mean, sample_mean - le)
        # 丸め誤差があるので平均を取る?
        sample_error = (ue - le) / 2
    else:
        sample_error = np.nan
    if mg3:
        p_value = float(mg3[0])
    else:
        p_value = np.nan
    return (sample_mean, sample_error, p_value)


def t_test_R(d1, d2):
    r.assign("d1", d1)
    r.assign("d2", d2)
    # print(t_test_single(d1))
    # print(t_test_single(d2))
    t_result = r("t.test(d1, d2)")
    print(t_result)


def main():
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("time", help="時刻の一部")
    args = parser.parse_args()

    fnamer_list = glob.glob(f"dat/*{args.time}*.csv")

    fnamer_dict = {}
    for fnamer in fnamer_list:
        mg = re.findall(r'p([0-9\.e\-]+)_c(\d+)_', fnamer)
        tmp_dict = {}
        tmp_dict["path"] = fnamer
        tmp_dict["df"] = pd.read_csv(fnamer) / (4 * int(mg[0][1]))
        fnamer_dict[mg[0][0]] = tmp_dict
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
                # 標準誤差
                sem = stats.sem(e_prob_df[col])
                sample_count = e_prob_df[col].size
                # print(f"sem = {sem}")
                # print(
                #     f"sqrt(V/n) = {np.sqrt(e_prob_df[col].var() / sample_count)}")

                error_interval = stats.t.interval(
                    alpha=0.95, df=sample_count-1, loc=0, scale=sem
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

    # ax.scatter(p_bsc, col_dict["repetition"]["mean"])

    for i, col in enumerate(col_dict):
        ax.scatter(p_bsc, col_dict[col]["mean"], color=COLORS[i])

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid()

    plt.show()


if __name__ == "__main__":
    main()
