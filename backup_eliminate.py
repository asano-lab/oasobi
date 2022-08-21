#!/usr/bin/env python3
import os

DIRNAME = "/home/sonoda/backups"

fname_list = [os.path.join(DIRNAME, i) for i in os.listdir(DIRNAME)]
fname_list.sort(key=os.path.getmtime)
print(fname_list)
