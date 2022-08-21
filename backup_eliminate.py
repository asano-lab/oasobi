#!/usr/bin/env python3
import os

N = 3

DIRNAME = "/home/sonoda/backups"

fname_list = [os.path.join(DIRNAME, i) for i in os.listdir(DIRNAME)]
fname_list.sort(key=os.path.getmtime)
print(fname_list)

# 古い順に削除
for i in range(len(fname_list) - N):
    os.remove(fname_list[i])


fname_list = [os.path.join(DIRNAME, i) for i in os.listdir(DIRNAME)]
fname_list.sort(key=os.path.getmtime)
print(fname_list)
