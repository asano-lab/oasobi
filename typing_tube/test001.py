import pyperclip
import re
import os

if __name__ == "__main__":
    if not os.path.isdir("records"):
        os.mkdir("records")
    prev_title_flag = 0
    moji = pyperclip.paste()
    for i, j in enumerate(moji.split("\r\n")):
        if j == "":
            continue
        m = re.match(r'\d+/\d+', j)
        if m is not None:
            pass
        if j == "https://policies.google.com/privacy":
            prev_title_flag = 1
        elif prev_title_flag == 1:
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
            m = re.match(r'正確率:(.+)%', j)
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
            mg = m.groups()
            total_keys = int(mg[0])
            escape_keys = int(mg[1])
        elif prev_title_flag == 9:
            prev_title_flag = 10
            m = re.match(r'(\d+)位\[(.+)打/秒\]', j)
            if m is None:
                break
            mg = m.groups()
            ranking = int(mg[0])
            kps = float(mg[1])
        elif prev_title_flag == 10 and j != "Typing Result":
            prev_title_flag = 11
            m = re.match(r'(\d+) clear / (\d+) failed', j)
            if m is None:
                break
            mg = m.groups()
            clear_lines = int(mg[0])
            failed_lines = int(mg[1])
        elif prev_title_flag == 11 and j != "Score Penalty":
            prev_title_flag = 12
            m = re.match(r'Miss: (.+)', j)
            if m is None:
                break
            miss_penalty = float(m.groups()[0])
        elif prev_title_flag == 12:
            prev_title_flag = 13
            m = re.match(r'Esc: (.+)', j)
            if m is None:
                break
            escape_penalty = float(m.groups()[0])
    try:
        print(f"title = {title}")
        print(editor)
        print(score)
        print(miss)
        print(accuracy)
        print(combo_max)
        print(total_keys)
        print(escape_keys)
        print(f"ranking = {ranking}")
        print(f"kps = {kps}")
        print(f"clear = {clear_lines}")
        print(f"failed = {failed_lines}")
        print(f"miss_penalty = {miss_penalty}")
        print(f"escape_penalty = {escape_penalty}")

        dir_name_format = (title + "{:02d}").format
        for i in range(100):
            dir_name = dir_name_format(i)
            if os.path.isdir(dir_name):
                pass
            else:
                break

    except NameError:
        print("不適切なクリップボードです")
