GCCFLAGS = -Wall -Wextra -O3
RM = rm -rf
EXECUTABLES = experiment

.PHONY: all
all: $(EXECUTABLES)

.c.o:
	gcc -c $< $(GCCFLAGS)

experiment: experiment.o
	gcc -o $@ $^ $(GCCFLAGS)

.PHONY: clean
clean:
	$(RM) *.o $(EXECUTABLES)
