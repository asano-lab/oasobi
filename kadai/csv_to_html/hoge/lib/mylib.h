#ifndef MYLIB_H
#define MYLIB_H

#include <stdio.h>
#include <string.h>

char *strtokc(char *str1, char *str2);

void strrep(char *str, const char *strsearch, const char *strnew);

int strcount(char str[], char strsearch);

void tok2str(char *str, char *tok);

void printtd(char *str, char *tok);

#endif
