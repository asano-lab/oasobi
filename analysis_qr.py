import urllib.parse
import base64
import re
import pandas as pd

url_df = pd.read_csv("qr_url.csv")

# print(url_df)
hex_list = []

for idx, row in url_df.iterrows():
    s_quote = row["url"]
    b_unquote = urllib.parse.unquote_to_bytes(s_quote).decode()

    print(b_unquote)

    m = re.search(r'1_(.*)$', b_unquote)
    if m:
        b64_block = m.groups()[0]
        print(b64_block)
        b64_decoded = base64.b64decode(b64_block)

        print(b64_decoded)
        print(type(b64_decoded))
        
        bits = ""
        hexadecimal = ""
        for i in b64_decoded:
            bits += format(i, "08b")
            hexadecimal += format(i, "02x")
        
        print(bits)
        hex_list.append(hexadecimal)

url_df["hex"] = hex_list
print(url_df)

xor_df = pd.DataFrame(columns=hex_list, index=hex_list)
for col in xor_df.columns:
    for idx in xor_df.index:
        xor_num = int(col, 16) ^ int(idx, 16)
        print(bin(xor_num))
        xor_df[col][idx] = format(xor_num, "x")

print(xor_df)
