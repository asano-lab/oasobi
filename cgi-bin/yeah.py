#!/usr/bin/env python3

import cgi, cgitb
cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")
print("<html><body>\n")
print("<h3>Python CGI test</h3>")

# for var in form.keys():
#     val = form[var].value
#     print("%s = %s<br>" % (var, val))

# mode のみ取得
if "mode" not in form:
    mode = "notfound"
else:
    mode = str(form["mode"].value)

print("mode=%s" % mode)

print("</body></html>\n")