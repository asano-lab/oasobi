# Makefile

OBJS = hello.o print.o
CC = gcc
GCCOPTIONS = -Wall -Wextra -g -O2
PROGRAM = hello

.SUFFIXES: .o .c

.PHONY: all
all: $(PROGRAM) som main convertcsv_v2 subsystem

subsystem:
	$(MAKE) -C lib

# プライマリターゲット
$(PROGRAM): $(OBJS)
	$(CC) -o $@ $^ $(GCCOPTIONS)
main: main.o
	$(CC) -o $@ $< $(GCCOPTIONS)
som: som.o
	$(CC) -o $@ $< $(GCCOPTIONS)
convertcsv_v2: convertcsv_v2.c lib/mylib.o
	$(CC) -o $@ $^

.c.o:
	$(CC) -c $< $(GCCOPTIONS)

# main.o: main.c
# 	$(CC) -c $<
# main.o: str.h

# som.o: som.c
# 	$(CC) -c $<
# hello.o: hello.c
# 	$(CC) -c $<
# print.o: print.c
# 	$(CC) -c $<
# convertcsv: convertcsv.c
# 	$(CC) convertcsv.c -o convertcsv -Wall
# mylib.o: lib/mylib.c lib/mylib.h
# 	$(CC) lib/mylib.c -c
.PHONY: clean
clean:
	$(RM) $(PROGRAM) $(OBJS) som som.o main main.o convertcsv_v2 lib/mylib.o