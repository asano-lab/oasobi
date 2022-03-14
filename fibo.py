#!/usr/bin/python3
import time

# フィボナッチ数列
def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

n = 37
t0 = time.time()
print("fibo(%d) = %d" % (n, fibo(n)))
print(time.time() - t0)
