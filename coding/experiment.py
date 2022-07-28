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
        self.daemon = True
    
    def run(self):
        print(fibo(35))

def main():
    th1 = MyThread()
    th1.start()
    th1.join()

if __name__ == "__main__":
    main()