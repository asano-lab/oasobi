animal_shogi.exe: animal_shogi.c animal_shogi.h
	gcc animal_shogi.c -o animal_shogi.exe -Wall
fibo.exe: fibo.c
	gcc fibo.c -o fibo.exe -Wall
rubik.exe: rubik.c
	gcc rubik.c -o rubik.exe -Wall
rubik.so: rubik.c
	gcc rubik.c -o rubik.so -Wall -shared -fPIC
