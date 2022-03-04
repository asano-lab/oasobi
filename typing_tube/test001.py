import pyperclip
import re
import os
import hashlib
import datetime

def generate_hash(title: str, total_keys: int, lines_list: list) -> str:
    """
    データを識別するハッシュを生成
    キーはプレイごと異なる場合があるので使わない
    """
    m = hashlib.sha256()
    m.update(title.encode())
    # print(total_keys.to_bytes(4, "big"))
    m.update(total_keys.to_bytes(4, "big"))

    for i in lines_list:
        m.update(i["keys_count"].to_bytes(4, "big"))
        m.update(str(i["seconds"]).encode())
        m.update(str(i["score_max"]).encode())

    return m.hexdigest()

def create_commons_dic(title: str, total_keys: int, lines_list: list):
    """
    プレイごとに変化しない情報
    """
    commons_dic = {}
    commons_dic["hash"] = generate_hash(title, total_keys, lines_list)
    commons_dic["title"] = title
    commons_dic["total_keys"] = total_keys
    commons_dic["lines"] = []
    for i in lines_list:
        tmp_dic = {}
        tmp_dic["keys_count"] = i["keys_count"]
        tmp_dic["seconds"] = i["seconds"]
        tmp_dic["score_max"] = i["score_max"]
        commons_dic["lines"].append(tmp_dic)
    return commons_dic

def main():
    if not os.path.isdir("records"):
        os.mkdir("records")
    prev_title_flag = 0
    lines_flag = 0
    lines_list = []
    moji = pyperclip.paste()
    result_dic = {}
    for i, j in enumerate(moji.split("\r\n")):
        if j == "":
            continue
        if prev_title_flag == 0:
            m = re.match(r'(\d{2}) (\d{2}) (\d{2})', j)
            if m:
                copied_time = [int(i) for i in m.groups()]
            elif j == "https://policies.google.com/privacy":
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
            total_keys = int(mg[0])
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
                    tmp_dic = dict()
                    lines_flag = 1
                    mg = m.groups()
                    tmp_dic["keys_count"] = int(mg[0])
                    tmp_dic["seconds"] = float(mg[1])
            elif lines_flag == 1:
                lines_flag = 2
                tmp_dic["keys"] = j
            elif lines_flag == 2:
                lines_flag = 0
                m = re.match(r'latency: (.+),　打/秒: (.+),　初速抜き: (.+),　miss: (\d+),　score: (.+) / (.+)', j)
                if m is None:
                    break
                mg = m.groups()
                tmp_dic["latency"] = float(mg[0])
                tmp_dic["kps"] = float(mg[1])
                tmp_dic["kps_exc_late"] = float(mg[2])
                tmp_dic["miss"] = int(mg[3])
                tmp_dic["score"] = float(mg[4])
                tmp_dic["score_max"] = float(mg[5])
                lines_list.append(tmp_dic)
    try:
        print(copied_time)
        print(title)
        print(editor)
        print(f'スコア: {result_dic["score"]}')
        print(f'ミス: {result_dic["miss"]}')
        print(f'正確率: {result_dic["acc"]}')
        print(f'最大コンボ: {result_dic["combo_max"]}')
        print(f'キー総数: {total_keys}')
        print(f'逃したキー数: {result_dic["escape_keys"]}')
        print(f'順位: {result_dic["ranking"]}')
        print(f'クリア行数: {result_dic["clear_lines"]}')
        print(f'失敗行数: {result_dic["failed_lines"]}')
        print(f'miss penalty: {result_dic["miss_penalty"]}')
        print(f'esc penalty: {result_dic["esc_penalty"]}')
        print(f'速さ: {result_dic["kps"]}打/秒')
        print(f'初速抜き速さ: {result_dic["kps_exc_late"]}打/秒')

        commons_dic = create_commons_dic(title, total_keys, lines_list)
        # print(commons_dic)

        print(result_dic)

        dir_name_format = (title + "{:02d}").format
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
