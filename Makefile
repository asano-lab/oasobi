animal_shogi.exe: animal_shogi.c animal_shogi.h
	gcc animal_shogi.c -o animal_shogi.exe -Wall
fibo.exe: fibo.c
	gcc fibo.c -o fibo.exe -Wall
zorome.exe: zorome.c
	gcc zorome.c -o zorome.exe -Wall
rubik.exe: rubik.c
	gcc rubik.c -o rubik.exe -Wall -fstack-usage
rubik_win.exe: rubik_win.c
	gcc rubik_win.c -o rubik_win.exe -Wall
rubik.so: rubik.c
	gcc rubik.c -o rubik.so -Wall -shared -fPIC
rubik_win.so: rubik_win.c
	gcc rubik_win.c -o rubik_win.so -Wall -shared -fPIC
