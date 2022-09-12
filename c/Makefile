CC = gcc
GCCFLAGS = -Wall -Wextra -O3

EXES = opt

.PHONY: all
all: $(EXES)

primality_test.s: primality_test.c
	$(CC) -S $< $(GCCFLAGS)

opt: opt.o
	gcc -o $@ $^

.PHONY: clean
clean:
	rm -rf *.o $(EXES)
