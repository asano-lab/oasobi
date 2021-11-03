#!/bin/bash

for ((i = 0; i < 10; i++));
do
    python3 rubik.py >> bfs_log.txt
    echo >> bfs_log.txt
done
