# Makefile

objs = hello.o print.o

.PHONY: all
all: hello som main

main: main.o
	gcc -o main main.o
main.o: main.c
	gcc -c main.c
main.o: str.h

hello: $(objs)
	gcc -Wall -O2 -o hello $(objs)
som: som.o
	gcc -Wall -O2 -o som som.o
som.o: som.c
	gcc -c som.c
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
.PHONY: clean
clean:
	rm -f hello $(objs) som som.o main main.o