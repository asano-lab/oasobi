import matplotlib.pyplot as plt
import pyperclip
import re
import os
import hashlib
import json
import datetime

# JSTとUTCの差分
DIFF_JST_FROM_UTC = 9

KPS_MAX = 0x7fffffff

def generate_commons_hash(commons_dic: dict) -> str:
    """
    データを識別するハッシュを生成
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

def generate_result_hash(result_dic: dict) -> str:
    """
    結果を識別するハッシュを生成
    """
    m = hashlib.sha256()
    # m.update(result_dic["coppied_time"].encode())
    m.update(str(result_dic["score"]).encode())
    m.update(result_dic["miss"].to_bytes(4, "big"))
    m.update(str(result_dic["acc"]).encode())
    m.update(result_dic["combo_max"].to_bytes(4, "big"))
    m.update(result_dic["esc_keys"].to_bytes(4, "big"))
    m.update(result_dic["ranking"].to_bytes(4, "big"))
    m.update(str(result_dic["kps"]).encode())
    m.update(result_dic["clear_lines"].to_bytes(4, "big"))
    m.update(result_dic["failed_lines"].to_bytes(4, "big"))
    m.update(str(result_dic["miss_penalty"]).encode())
    m.update(str(result_dic["esc_penalty"]).encode())
    m.update(str(result_dic["kps_exc_late"]).encode())

    for i in result_dic["lines"]:
        m.update(i["keys"].encode())
        # m.update(str(i["latency"]).encode())
        m.update(str(i["kps"]).encode())
        m.update(str(i["kps_exc_late"]).encode())
        m.update(i["miss"].to_bytes(4, "big"))
        m.update(str(i["score"]).encode())
        m.update(str(i["clear"]).encode())
        m.update(str(i["comp"]).encode())

    return m.hexdigest()

def main():
    records_dir = "records/"

    if not os.path.isdir(records_dir):
        os.mkdir(records_dir)
        print(f"{records_dir}を作成")
        with open(records_dir + ".gitignore", "w") as f:
            f.write("*\n")
    
    status_line = 0
    lines_flag = 0
    moji = pyperclip.paste()
    result_dic = {"lines": []}
    commons_dic = {"lines": []}
    clear_count = 0

    for i, j in enumerate(moji.split("\r\n")):
        # print(j)
        if j == "":
            continue
        if status_line == 0:
            m = re.match(r'(\d{2}) (\d{2}) (\d{2})', j)
            if m:
                result_dic["copied_time"] = "%s%s%s" % m.groups()
            elif j == "https://policies.google.com/privacy":
                prev_title_flag = 1
        elif prev_title_flag == 1:
            prev_title_flag = 2
            commons_dic["title"] = j.replace("/", "_")
        elif prev_title_flag == 2:
            prev_title_flag = 3
            editor = j
        elif status_line == 3:
            # print(j)
            m = re.match(r' (\d+)打 (\d)+ライン\d+:\d+ 中央値.*打/秒 \| 最高.*打/秒', j)
            if m is not None:
                print(j)
                status_line = 16
                commons_dic["total_keys"] = int(m.groups()[0])
        elif status_line == 16:
            if j == "ranking":
                status_line = 4
        elif status_line == 4:
            status_line = 5
            result_dic["score"] = float(j)
        elif status_line == 5:
            status_line = 15
            m = re.match(r'(\d+)位$', j)
            if m is None:
                break
            result_dic["ranking"] = int(m.groups()[0])
        elif status_line == 15:
            status_line = 6
            m = re.match(r'(\d+)miss$', j)
            if m is None:
                break
            result_dic["miss"] = int(m.groups()[0])
        elif status_line == 6:
            status_line = 7
            m = re.match(r'正確率:(.+)%$', j)
            if m is None:
                break
            result_dic["acc"] = float(m.groups()[0])
        elif status_line == 7:
            status_line = 8
            m = re.match(r'(\d+)combo$', j)
            if m is None:
                break
            result_dic["combo_max"] = int(m.groups()[0])
        elif status_line == 8:
            status_line = 9
            m = re.match(r'(\d+)打 / (\d+)逃し$', j)
            if m is None:
                break
            mg = m.groups()
            # どうやら想定している意味と異なるので省略
            # commons_dic["total_keys"] = int(mg[0]) + int(mg[1])
            one_esc_penalty = 100 / commons_dic["total_keys"]
            one_miss_penalty = one_esc_penalty / 4
            # print(one_esc_penalty, one_miss_penalty)
            result_dic["esc_keys"] = int(mg[1])
        elif status_line == 9:
            status_line = 10
            m = re.match(r'(.+)打/秒$', j)
            if m is None:
                break
            mg = m.groups()
            result_dic["kps"] = float(mg[0])
        elif status_line == 10 and j != "Typing Result":
            status_line = 11
            m = re.match(r'(\d+) clear / (\d+) failed$', j)
            if m is None:
                break
            mg = m.groups()
            result_dic["clear_lines"] = int(mg[0])
            result_dic["failed_lines"] = int(mg[1])
        elif status_line == 11 and j != "Score Penalty":
            status_line = 12
            m = re.match(r'Miss: (.+)', j)
            if m is None:
                break
            result_dic["miss_penalty"] = float(m.groups()[0])
        elif status_line == 12:
            status_line = 13
            m = re.match(r'Esc: (.+)', j)
            if m is None:
                break
            result_dic["esc_penalty"] = float(m.groups()[0])
        elif status_line == 13:
            status_line = 14
            # print(j)
            m = re.match(r'初速抜き: (.+)打/秒$', j)
            if m is None:
                break
            result_dic["kps_exc_late"] = float(m.groups()[0])
        elif status_line == 14:
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
                m = re.match(r'打/秒: (.+),　初速抜き: (.+),　miss: (\d+),　score: (.+) / (.+)', j)
                if m is None:
                    break
                lines_flag = 0
                mg = m.groups()
                tmp_dic2["kps"] = float(mg[0])
                if mg[1] == "Infinity":
                    tmp_dic2["kps_exc_late"] = KPS_MAX
                else:
                    tmp_dic2["kps_exc_late"] = float(mg[1])
                tmp_dic2["miss"] = int(mg[2])
                tmp_dic2["score"] = float(mg[3])
                tmp_dic1["score_max"] = float(mg[4])
                miss_only_score = tmp_dic1["score_max"] - tmp_dic2["miss"] * one_miss_penalty
                score_diff = abs(tmp_dic2["score"] - miss_only_score)
                if score_diff < one_esc_penalty * 0.48:
                    tmp_dic2["clear"] = True
                    # print(tmp_dic2["keys"])
                    # print("score: %.5f, %.5f" % (tmp_dic2["score"], miss_only_score))
                    clear_count += 1
                else:
                    tmp_dic2["clear"] = False
                tmp_dic2["clear"] = miss_only_score == tmp_dic2["score"]
                tmp_dic2["comp"] = tmp_dic2["clear"] and tmp_dic2["miss"] == 0
                commons_dic["lines"].append(tmp_dic1)
                result_dic["lines"].append(tmp_dic2)
    # print(status_line)
    if status_line != 14:
        print("不適切なクリップボードです")
        return
    if lines_flag != 0:
        print("不適切なクリップボードです")
        return
    if result_dic["clear_lines"] + result_dic["failed_lines"] != len(result_dic["lines"]):
        print("行数が一致しません")
        return
    if result_dic["clear_lines"] != clear_count:
        print(result_dic["clear_lines"], clear_count)
        print("クリア数が一致しません")
        return
    print(result_dic["copied_time"])
    print(commons_dic["title"])
    print(editor)
    print(f'スコア: {result_dic["score"]}')
    print(f'ミス: {result_dic["miss"]}')
    print(f'正確率: {result_dic["acc"]}')
    print(f'最大コンボ: {result_dic["combo_max"]}')
    print(f'キー総数: {commons_dic["total_keys"]}')
    print(f'逃したキー数: {result_dic["esc_keys"]}')
    print(f'順位: {result_dic["ranking"]}')
    print(f'クリア行数: {result_dic["clear_lines"]}')
    print(f'失敗行数: {result_dic["failed_lines"]}')
    print(f'miss penalty: {result_dic["miss_penalty"]}')
    print(f'esc penalty: {result_dic["esc_penalty"]}')
    print(f'速さ: {result_dic["kps"]}打/秒')
    print(f'初速抜き速さ: {result_dic["kps_exc_late"]}打/秒')

    commons_dic["hash"] = generate_commons_hash(commons_dic)
    result_dic["hash"] = generate_result_hash(result_dic)

    dir_name_format = (records_dir + commons_dic["title"] + "_{:02d}/").format

    for i in range(100):
        dir_name = dir_name_format(i)
        commons_path = dir_name + "commons.json"
        print(dir_name)
        if os.path.isdir(dir_name):
            with open(commons_path, "r") as f:
                past_commons_dic = json.load(f)
            if past_commons_dic["hash"] == commons_dic["hash"]:
                print("同じデータ")
                break
            else:
                print("同一タイトルだがデータが異なる")
        else:
            os.mkdir(dir_name)
            with open(commons_path, "w") as f:
                json.dump(commons_dic, f, indent=2)
            print("データ追加")
            break
    
    result_fnames = sorted([i for i in os.listdir(dir_name) if re.match(r'result\d{14}.json$', i)])
    print(result_fnames)

    if len(result_fnames) > 0:
        with open(dir_name + result_fnames[-1], "r") as f:
            past_result_dic = json.load(f)
        if past_result_dic["hash"] == result_dic["hash"]:
            if input("直前の結果とハッシュが同じです. データを追加しますか? (y\\n):") != "y":
                return
    
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
    new_result_path = now.strftime(dir_name + "result%Y%m%d%H%M%S.json")
    with open(new_result_path, "w") as f:
        json.dump(result_dic, f, indent=2)
    
    result_fnames = sorted([i for i in os.listdir(dir_name) if re.match(r'result\d{14}.json$', i)])
    x = [i for i in range(len(result_fnames))]
    y = []
    for fnamer in result_fnames:
        with open(dir_name + fnamer, "r") as f:
            past_result_dic = json.load(f)
        y.append(past_result_dic["score"])
    
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()
    pass
