CC = gcc

CFLAGS = -Wall -Wextra -O2

ODAKEDIR = odake/csvToHTML

SUBDIRS = $(ODAKEDIR)

csv_to_html: csv_to_html.o
	$(CC) -o $@ $(ODAKEDIR)/$< $(CFLAGS)

csv_to_html.o:
	@for i in $(SUBDIRS);\
	do\
		$(MAKE) -C $$i;\
	done\
