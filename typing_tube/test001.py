import pyperclip
import re

if __name__ == "__main__":
    moji = pyperclip.paste()
    for i in moji.split("\r\n"):
        m = re.match(r'\d+/\d+', i)
        if m is not None:
            pass
        print(i)
