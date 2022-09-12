CC = gcc
GCCFLAGS = -Wall -Wextra -O3 -lm

EXES = opt primality_test

.PHONY: all
all: $(EXES)

primality_test.s: primality_test.c
	$(CC) -S $< $(GCCFLAGS)

primality_test.o: primality_test.s
	as -o $@ $<

primality_test: primality_test.o
	$(CC) -o $@ $^ $(GCCFLAGS)

.PHONY: clean
clean:
	rm -rf *.o $(EXES)
