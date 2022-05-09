convertcsv: convertcsv.c
	gcc convertcsv.c -o convertcsv -Wall
convertcsv_v2: convertcsv_v2.c mylib.o
	gcc convertcsv_v2.c mylib.o -o convertcsv_v2 -Wall
mylib.o: lib/mylib.c lib/mylib.h
	gcc lib/mylib.c -c