CC = gcc

CFLAGS = -Wall -Wextra -O0 -g

ODAKEDIR = odake/csvToHTML

SUBDIRS = $(ODAKEDIR)

.c.o:
	$(CC) -c $< $(CFLAGS)

csv_to_html: csv_to_html.o
	$(CC) -o $@ $(ODAKEDIR)/$< $(CFLAGS)

csv_to_html.o:
	@for i in $(SUBDIRS);\
	do\
		$(MAKE) -C $$i;\
	done\

csv2html_urano: csv2html_urano.o
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean
clean:
	@rm -rf *.o
