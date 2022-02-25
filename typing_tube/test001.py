import pyperclip
import re

if __name__ == "__main__":
    c = 0
    c_max = 0
    moji = pyperclip.paste()
    for i in moji.split("\r\n"):
        m = re.match(r'\d+/\d+', i)
        if m is not None:
            pass
        if i == "":
            pass
        else:
            print(i)
