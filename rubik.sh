#!/bin/bash

for ((i = 0; i < 200; i++));
do
    python3 rubik.py >> bfs_log.txt
done
