#!/usr/bin/env python3
import subprocess
import time
import numpy as np


def main():
    subprocess.run(["make", "experiment"])

    t0 = time.time()
    subprocess.run(["./experiment", "test.csv", "4.64e-6", "20000000000"])
    print(time.time() - t0)


if __name__ == "__main__":
    main()
    # print(np.power(10, -5-1/3))
