CC = gcc

CFLAGS = -Wall -Wextra -O0 -g

ODAKEDIR = odake/csvToHTML

SUBDIRS = $(ODAKEDIR)

.c.o:
	$(CC) -c $< $(CFLAGS)

csv_to_html: csv_to_html.o
	$(CC) -o $@ $(ODAKEDIR)/$< $(CFLAGS)

csv2html_urano: csv2html_urano.o
	$(CC) -o $@ $^ $(CFLAGS)

csv_to_html_remus0316: csv_to_html_remus0316.o
	$(CC) -o $@ $^ $(CFLAGS)

csv_to_html.o:
	@for i in $(SUBDIRS);\
	do\
		$(MAKE) -C $$i;\
	done\

.PHONY: clean
clean:
	@rm -rf *.o
	@for i in $(SUBDIRS);\
	do\
		rm -rf $$i/*.o;\
	done\
