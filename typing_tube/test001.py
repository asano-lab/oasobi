import pyperclip
import re
import os

if __name__ == "__main__":
    if not os.path.isdir("records"):
        os.mkdir("records")
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
        elif prev_title_flag == 6:
            prev_title_flag = 7
            m = re.match(r'正確率:(.*)%', j)
            if m is None:
                break
            accuracy = float(m.groups()[0])
        elif prev_title_flag == 7:
            prev_title_flag = 8
            m = re.match(r'\d+/(\d+)combo', j)
            if m is None:
                break
            combo_max = int(m.groups()[0])
        elif prev_title_flag == 8:
            prev_title_flag = 9
            m = re.match(r'\d+/(\d+)打\[(\d+)\]esc', j)
            if m is None:
                break
            total_keys, escape_keys = m.groups()
    try:
        print(title)
        print(editor)
        print(score)
        print(miss)
        print(accuracy)
        print(combo_max)
        print(total_keys)
        print(escape_keys)

        dir_name_format = (title + "{:02d}").format
        for i in range(100):
            dir_name = dir_name_format(i)
            if os.path.isdir(dir_name):
                pass
            else:
                break

    except NameError:
        print("不適切なクリップボードです")
