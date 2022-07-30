#!/usr/bin/env python3
import subprocess
import time
import numpy as np


def main():
    subprocess.run(["make", "experiment"])

    p_bsc = np.power(10, -4 - 1 / 3)
    ev = 20000
    count = ev / p_bsc / 4

    test_path = "test.csv"

    with open(test_path, "a", encoding="UTF-8") as f:
        print(f"p_bsc={p_bsc},loop={count}", file=f)

    t0 = time.time()
    subprocess.run(["./experiment", test_path, str(p_bsc), str(count)])
    print(time.time() - t0)


if __name__ == "__main__":
    main()
