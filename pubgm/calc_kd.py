#!/usr/bin/env python3
import pandas as pd
import numpy as np
from scipy import stats


def calc_interval(ds: pd.Series, alpha=0.95):
    """
    平均値の信頼区間を求める
    """
    sample_mean = ds.mean()
    sample_var = ds.var()
    n = ds.shape[0]
    return stats.norm.interval(confidence=alpha,
                               loc=sample_mean, scale=np.sqrt(sample_var / n))


def main():
    df = pd.read_csv("kill.csv")
    alpha = 0.99
    print(calc_interval(df["kill"], alpha=alpha))
    print(calc_interval(df["damage"], alpha=alpha))


if __name__ == "__main__":
    main()
