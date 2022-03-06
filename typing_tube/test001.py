import pyperclip
import re
import os
import hashlib
import datetime
import json

def generate_commons_hash(commons_dic: dict) -> str:
    """
    データを識別するハッシュを生成
    キーはプレイごと異なる場合があるので使わない
    """
    m = hashlib.sha256()
    m.update(commons_dic["title"].encode())
    # print(total_keys.to_bytes(4, "big"))
    m.update(commons_dic["total_keys"].to_bytes(4, "big"))

    for i in commons_dic["lines"]:
        m.update(i["keys_count"].to_bytes(4, "big"))
        m.update(str(i["seconds"]).encode())
        m.update(str(i["score_max"]).encode())

    return m.hexdigest()

def main():
    if not os.path.isdir("records"):
        os.mkdir("records")
    prev_title_flag = 0
    lines_flag = 0
    lines_list_commons = []
    moji = pyperclip.paste()
    result_dic = {"lines": []}
    commons_dic = {"lines": []}
    for i, j in enumerate(moji.split("\r\n")):
        if j == "":
            continue
        if prev_title_flag == 0:
            m = re.match(r'(\d{2}) (\d{2}) (\d{2})', j)
            if m:
                result_dic["copied_time"] = "%s%s%s" % m.groups()
            elif j == "https://policies.google.com/privacy":
                prev_title_flag = 1
        elif prev_title_flag == 1:
            prev_title_flag = 2
            commons_dic["title"] = j
        elif prev_title_flag == 2:
            prev_title_flag = 3
            editor = j
        elif j == "ranking":
            prev_title_flag = 4
        elif prev_title_flag == 4:
            prev_title_flag = 5
            result_dic["score"] = float(j)
        elif prev_title_flag == 5:
            prev_title_flag = 6
            m = re.match(r'(\d+)miss$', j)
            if m is None:
                break
            result_dic["miss"] = int(m.groups()[0])
        elif prev_title_flag == 6:
            prev_title_flag = 7
            m = re.match(r'正確率:(.+)%$', j)
            if m is None:
                break
            result_dic["acc"] = float(m.groups()[0])
        elif prev_title_flag == 7:
            prev_title_flag = 8
            m = re.match(r'\d+/(\d+)combo$', j)
            if m is None:
                break
            result_dic["combo_max"] = int(m.groups()[0])
        elif prev_title_flag == 8:
            prev_title_flag = 9
            m = re.match(r'\d+/(\d+)打\[(\d+)\]esc$', j)
            if m is None:
                break
            mg = m.groups()
            commons_dic["total_keys"] = int(mg[0])
            one_miss_penalty = 25 / commons_dic["total_keys"]
            result_dic["escape_keys"] = int(mg[1])
        elif prev_title_flag == 9:
            prev_title_flag = 10
            m = re.match(r'(\d+)位\[(.+)打/秒\]$', j)
            if m is None:
                break
            mg = m.groups()
            result_dic["ranking"] = int(mg[0])
            result_dic["kps"] = float(mg[1])
        elif prev_title_flag == 10 and j != "Typing Result":
            prev_title_flag = 11
            m = re.match(r'(\d+) clear / (\d+) failed$', j)
            if m is None:
                break
            mg = m.groups()
            result_dic["clear_lines"] = int(mg[0])
            result_dic["failed_lines"] = int(mg[1])
        elif prev_title_flag == 11 and j != "Score Penalty":
            prev_title_flag = 12
            m = re.match(r'Miss: (.+)', j)
            if m is None:
                break
            result_dic["miss_penalty"] = float(m.groups()[0])
        elif prev_title_flag == 12:
            prev_title_flag = 13
            m = re.match(r'Esc: (.+)', j)
            if m is None:
                break
            result_dic["esc_penalty"] = float(m.groups()[0])
        elif prev_title_flag == 13:
            prev_title_flag = 14
            m = re.match(r'初速抜き: (.+)打/秒$', j)
            if m is None:
                break
            result_dic["kps_exc_late"] = float(m.groups()[0])
        elif prev_title_flag == 14:
            if lines_flag == 0:
                m = re.match(r'\d+/\d+ \((\d+)打 ÷ (.+)秒 = .+打/秒\)$', j)
                if m:
                    lines_flag = 1
                    mg = m.groups()
                    tmp_dic1 = {"keys_count": int(mg[0]), "seconds": float(mg[1])}
            elif lines_flag == 1:
                lines_flag = 2
                tmp_dic2 = {"keys": j}
            elif lines_flag == 2:
                lines_flag = 0
                m = re.match(r'latency: (.+),　打/秒: (.+),　初速抜き: (.+),　miss: (\d+),　score: (.+) / (.+)', j)
                if m is None:
                    break
                mg = m.groups()
                tmp_dic2["latency"] = float(mg[0])
                tmp_dic2["kps"] = float(mg[1])
                tmp_dic2["kps_exc_late"] = float(mg[2])
                tmp_dic2["miss"] = int(mg[3])
                tmp_dic2["score"] = float(mg[4])
                tmp_dic1["score_max"] = float(mg[5])
                miss_only_score = round(tmp_dic1["score_max"] - tmp_dic2["miss"] * one_miss_penalty, 2)
                tmp_dic2["clear"] = miss_only_score == tmp_dic2["score"]
                tmp_dic2["comp"] = tmp_dic2["clear"] and tmp_dic2["miss"] == 0
                commons_dic["lines"].append(tmp_dic1)
                result_dic["lines"].append(tmp_dic2)
    try:
        print(result_dic["copied_time"])
        print(commons_dic["title"])
        print(editor)
        print(f'スコア: {result_dic["score"]}')
        print(f'ミス: {result_dic["miss"]}')
        print(f'正確率: {result_dic["acc"]}')
        print(f'最大コンボ: {result_dic["combo_max"]}')
        print(f'キー総数: {commons_dic["total_keys"]}')
        print(f'逃したキー数: {result_dic["escape_keys"]}')
        print(f'順位: {result_dic["ranking"]}')
        print(f'クリア行数: {result_dic["clear_lines"]}')
        print(f'失敗行数: {result_dic["failed_lines"]}')
        print(f'miss penalty: {result_dic["miss_penalty"]}')
        print(f'esc penalty: {result_dic["esc_penalty"]}')
        print(f'速さ: {result_dic["kps"]}打/秒')
        print(f'初速抜き速さ: {result_dic["kps_exc_late"]}打/秒')

        commons_dic["hash"] = generate_commons_hash(commons_dic)
        print(commons_dic)

        # print(result_dic)
        with open("test.json", "w") as f:
            json.dump(result_dic, f, indent=2)

        dir_name_format = (commons_dic["title"] + "{:02d}").format
        for i in range(100):
            dir_name = dir_name_format(i)
            print(dir_name)
            if os.path.isdir(dir_name):
                pass
            else:
                # os.mkdir(dir_name)
                break

    except NameError:
        print("不適切なクリップボードです")

if __name__ == "__main__":
    main()
