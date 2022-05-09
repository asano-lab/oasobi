# Makefile

OBJS = hello.o print.o
CC = gcc
GCCOPTIONS = -Wall -Wextra -g -O2
PROGRAM = hello

.SUFFIXES: .o .c

# プライマリターゲット
$(PROGRAM): $(OBJS)
	$(CC)  -o $@ $^ $(GCCOPTIONS)

.c.o:
	$(CC) $(CFLAGS) -c $<

# .PHONY: all
# all: $(PROGRAM) som main

# main: main.o
# 	$(CC) -o $@ main.o
# main.o: main.c
# 	$(CC) -c $<
# main.o: str.h

# som: som.o
# 	$(CC)  -o $@ $< $(GCCOPTIONS)
# som.o: som.c
# 	$(CC) -c $<
# hello.o: hello.c
# 	$(CC) -c $<
# print.o: print.c
# 	$(CC) -c $<
# convertcsv: convertcsv.c
# 	$(CC) convertcsv.c -o convertcsv -Wall
# convertcsv_v2: convertcsv_v2.c mylib.o
# 	$(CC) convertcsv_v2.c mylib.o -o convertcsv_v2 -Wall
# mylib.o: lib/mylib.c lib/mylib.h
# 	$(CC) lib/mylib.c -c
.PHONY: clean
clean:
	$(RM) $(PROGRAM) $(OBJS) som som.o main main.o