#!/usr/bin/env python3
import pandas as pd
import numpy as np
from scipy import stats


def main():
    df = pd.read_csv("kill.csv")
    # print(df)
    kill_mean = df["kill"].mean()
    kill_var = df["kill"].var()
    print(kill_var)
    print(stats.tvar(df["kill"]))


if __name__ == "__main__":
    main()
