#!/usr/bin/env python3
import subprocess
import threading
import argparse
import time

def fibo(x):
    if x <= 0:
        y = 0
    elif x == 1:
        y = 1
    else:
        y = fibo(x - 2) + fibo(x - 1)
    return y

class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        
        # self.daemon = True
    
    def run(self):
        print(fibo(30))

def main():
    th_list = []
    t0 = time.time()
    for _ in range(50):
        print(fibo(31))
    #     tmp_th = MyThread()
    #     tmp_th.start()
    #     th_list.append(tmp_th)
    #     # print(end=f"{threading.active_count()},", flush=True)
    # while threading.active_count() > 1:
    #     time.sleep(0.1)
    print()
    print(time.time() - t0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="符号の実験")
    parser.add_argument("-c", "--count", help="ループ数", type=int, default=10000)
    args = parser.parse_args()
    # print(args.count)
    main()