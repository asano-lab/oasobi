import pyperclip
import re

if __name__ == "__main__":
    prev_title_flag = False
    moji = pyperclip.paste()
    for i in moji.split("\r\n"):
        m = re.match(r'\d+/\d+', i)
        if m is not None:
            pass
        if i == "https://policies.google.com/privacy":
            prev_title_flag = True
        elif prev_title_flag and i:
            prev_title_flag = False
            print(i)
        # print(i)
