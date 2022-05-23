CC = gcc

CFLAGS = -Wall -Wextra -O0 -g

EXES = csv_to_html_odake csv_to_html_urano csv_to_html_remus0316

RM = rm -rf

.PHONY: all
all: $(EXES)

.c.o:
	$(CC) -c $< $(CFLAGS)

csv_to_html_odake: csv_to_html_odake.o
	$(CC) -o $@ $^ $(CFLAGS)

csv_to_html_urano: csv_to_html_urano.o
	$(CC) -o $@ $^ $(CFLAGS)

csv_to_html_remus0316: csv_to_html_remus0316.o
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean
clean:
	$(RM) $(EXES)
	$(RM) *.o
