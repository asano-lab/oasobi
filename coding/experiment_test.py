#!/usr/bin/env python3
import subprocess
import time
import numpy as np


def main():
    subprocess.run(["make", "experiment"])

    p_bsc = np.power(10, -4 - 1 / 3)
    ev = 2000000
    count = ev / p_bsc / 4
    print(p_bsc, ev, count)
    return

    with open("test.csv", "a", encoding="UTF-8") as f:
        print()
    t0 = time.time()
    subprocess.run(["./experiment", "test.csv", "4.64e-5", "20000000000"])
    print(time.time() - t0)


if __name__ == "__main__":
    main()
