#!/usr/bin/env python3
import subprocess
import threading

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
        print(fibo(34))

def main():
    th_list = []
    for i in range(10):
        tmp_th = MyThread()
        tmp_th.start()
        th_list.append(tmp_th)
        print(threading.active_count())
    print("終わるまで待機")

if __name__ == "__main__":
    main()