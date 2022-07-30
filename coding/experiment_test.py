#!/usr/bin/env python3
import subprocess
import time
import numpy as np


def main():
    subprocess.run(["make", "experiment"])

    p_bsc = np.power(10, -4.0-1/4)
    # ev = 2000
    # count = round(ev / p_bsc / 4)
    count = int(1e10)

    test_path = "test.csv"

    print(f"p_bsc={p_bsc},loop={count}")
    with open(test_path, "a", encoding="UTF-8") as f:
        print(f"p_bsc={p_bsc},loop={count}", file=f)

    t0 = time.time()
    subprocess.run(["./experiment", test_path, str(p_bsc), str(count)])
    print(time.time() - t0)


if __name__ == "__main__":
    main()
