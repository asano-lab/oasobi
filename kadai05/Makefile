# Makefile2
hello: hello.o print.o
	gcc -Wall -O2 -o hello hello.o print.o
hello.o: hello.c
	gcc -c hello.c
print.o: print.c
	gcc -c print.c
convertcsv: convertcsv.c
	gcc convertcsv.c -o convertcsv -Wall
convertcsv_v2: convertcsv_v2.c mylib.o
	gcc convertcsv_v2.c mylib.o -o convertcsv_v2 -Wall
mylib.o: lib/mylib.c lib/mylib.h
	gcc lib/mylib.c -c