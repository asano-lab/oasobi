CC = gcc

CFLAGS = -Wall -Wextra -O0 -g

ODAKEDIR = odake/csvToHTML
KOYANAGIDIR = kadai5_kt

SUBDIRS = $(ODAKEDIR) $(KOYANAGIDIR)

EXES = csv_to_html csv2html_urano csv_to_html_remus0316 csv_to_html_kt

RM = rm -rf

.PHONY: all
all: $(EXES)

.c.o:
	$(CC) -c $< $(CFLAGS)

csv_to_html: csv_to_html.o
	$(CC) -o $@ $(ODAKEDIR)/$< $(CFLAGS)

csv2html_urano: csv2html_urano.o
	$(CC) -o $@ $^ $(CFLAGS)

csv_to_html_remus0316: csv_to_html_remus0316.o
	$(CC) -o $@ $^ $(CFLAGS)

csv_to_html_kt: csv_to_html_kt.o
	$(CC) -o $@ $(KOYANAGIDIR)/$^ $(CFLAGS)

csv_to_html.o:
	$(MAKE) -C $(ODAKEDIR)

csv_to_html_kt.o:
	$(MAKE) -C $(KOYANAGIDIR)

.PHONY: clean
clean:
	$(RM) $(EXES)
	$(RM) *.o
	@for i in $(SUBDIRS);\
	do\
		$(MAKE) -C $$i clean;\
	done\
