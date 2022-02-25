import pyperclip
import re

from typer import edit

if __name__ == "__main__":
    prev_title_flag = 0
    moji = pyperclip.paste()
    for i, j in enumerate(moji.split("\r\n")):
        m = re.match(r'\d+/\d+', j)
        if m is not None:
            pass
        if j == "https://policies.google.com/privacy":
            prev_title_flag = 1
        elif prev_title_flag == 1 and j:
            prev_title_flag = 2
            title = j
        elif prev_title_flag == 2:
            prev_title_flag = 3
            editor = j
        elif j == "ranking":
            prev_title_flag = 4
        elif prev_title_flag == 4:
            prev_title_flag = 5
            score = float(j)
        elif prev_title_flag == 5:
            prev_title_flag = 6
            m = re.match(r'(\d+)miss$', j)
            if m is None:
                break
            miss = int(m.groups()[0])
        
    print(title)
    print(editor)
    print(score)
    print(miss)
