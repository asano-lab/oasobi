#!/bin/bash

for ((i = 0; i < 360; i++));
do
    python3 rubik.py >> bfs_log.txt
    echo >> bfs_log.txt
done
