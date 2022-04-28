import urllib.parse
import base64
import re

s_quote = "https://qr-tsc.shinshu-u.ac.jp/qr/?param=1_bOIQMb6GWrL91OcipkCPjg%3D%3D"

b_unquote = urllib.parse.unquote_to_bytes(s_quote).decode()

print(b_unquote)

m = re.search(r'1_(.*)$', b_unquote)
if m:
    print(m.groups())

# b64_decoded = base64.b64decode(b_unquote.decode())

# print(b64_decoded)
