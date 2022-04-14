#!/usr/bin/python3
import time
import sys
import argparse

parser = argparse.ArgumentParser(description="フィボナッチ数列の計算時間を計測")
parser.add_argument("integers", metavar='N', type=int, help="フィボナッチ数列の入力")

args = parser.parse_args()

# フィボナッチ数列
def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

n = args.integers
print(sys.version)
t0 = time.time()
print("fibo(%d) = %d" % (n, fibo(n)))
print(time.time() - t0, "秒")
