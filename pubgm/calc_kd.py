#!/usr/bin/env python3
import pandas as pd
import numpy as np
from scipy import stats


def main():
    df = pd.read_csv("kill.csv")
    # print(df)
    kill_mean = df["kill"].mean()
    kill_var = df["kill"].var()
    n = df.shape[0]
    # print(kill_var)
    # print(stats.tvar(df["kill"]))
    print(stats.norm.interval(confidence=0.95,
          loc=kill_mean, scale=np.sqrt(kill_var / n)))


if __name__ == "__main__":
    main()
