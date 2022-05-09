# Makefile

OBJS = hello.o print.o
CC = gcc

.PHONY: all
all: hello som main

main: main.o
	$(CC) -o main main.o
main.o: main.c
	$(CC) -c main.c
main.o: str.h

hello: $(OBJS)
	$(CC) -Wall -O2 -o hello $(OBJS)
som: som.o
	$(CC) -Wall -O2 -o som som.o
som.o: som.c
	$(CC) -c som.c
hello.o: hello.c
	$(CC) -c hello.c
print.o: print.c
	$(CC) -c print.c
convertcsv: convertcsv.c
	$(CC) convertcsv.c -o convertcsv -Wall
convertcsv_v2: convertcsv_v2.c mylib.o
	$(CC) convertcsv_v2.c mylib.o -o convertcsv_v2 -Wall
mylib.o: lib/mylib.c lib/mylib.h
	$(CC) lib/mylib.c -c
.PHONY: clean
clean:
	$(RM) hello $(OBJS) som som.o main main.o