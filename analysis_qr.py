import urllib.parse
import base64
import re
import pandas as pd

url_df = pd.read_csv("qr_url.csv")

print(url_df)

for s_quote in url_df["url"]:
    b_unquote = urllib.parse.unquote_to_bytes(s_quote).decode()

    print(b_unquote)

    m = re.search(r'1_(.*)$', b_unquote)
    if m:
        b64_block = m.groups()[0]
        print(b64_block)
        b64_decoded = base64.b64decode(b64_block)

        print(b64_decoded)
        print(type(b64_decoded))
        for i in b64_decoded:
            print(format(i, "08b"), format(i, "02x"))
