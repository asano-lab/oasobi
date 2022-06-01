CC = gcc
GCCFLAGS = -Wall -Wextra -O0

EXES = opt

.PHONY: all
all: $(EXES)

.c.o:
	gcc -c $<

opt: opt.o
	gcc -o $@ $^

.PHONY: clean
clean:
	rm -rf *.o $(EXES)
