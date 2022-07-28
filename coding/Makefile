GCCFLAGS = -Wall -Wextra -O3
RM = rm -rf
EXECUTABLES = experiment
CC = gcc

.PHONY: all
all: $(EXECUTABLES)

.c.s:
	$(CC) -S $<

experiment.o: experiment.s
	as -o $@ $^

experiment: experiment.o
	$(CC) -o $@ $^ $(GCCFLAGS)

.PHONY: clean
clean:
	$(RM) *.o $(EXECUTABLES)
