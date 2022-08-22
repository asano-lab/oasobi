#!/usr/bin/env python3
import glob
import os

N = 3

BACKUP_PATH_PATTERN = "/home/sonoda/backups/oasobi_backup*"

fname_list = glob.glob(BACKUP_PATH_PATTERN)
# fname_list = [os.path.join(DIRNAME, i) for i in os.listdir(DIRNAME)]

fname_list.sort(key=os.path.getmtime)
# print(fname_list)
# exit()

# 古い順に削除
for i in range(len(fname_list) - N):
    os.remove(fname_list[i])
