import code
import re
import numpy as np
from math import log2, ceil

def fixed_value(v: str) -> str:
    """
    固定値を返す際にただ出力するだけ
    """
    print("固定値: %s" % v)
    return v

def calc_entropy(p_arr):
    """
    エントロピーを計算
    """
    if abs(sum(p_arr) - 1) > 1e-10:
        print(sum(p_arr))
        return
    e = 0
    for i in p_arr:
        if i < 1e-10:
            continue
        e -= i * log2(i)
    return e

def del_zero(ans):
    if ans[-1] == "0":
        ans = ans[:-1]
    return ans

# ハフマン符号関連
def get_min_syms(d_inv, n):
    """
    下からn番目までの記号を取り出す?
    """
    min_prob = min(d_inv)
    min_prob_syms = d_inv.pop(min_prob)
    
    rem_len = n - len(min_prob_syms)
    # オーバー
    if rem_len < 0:
        # 接点番号が小さいもの優先
        min_prob_syms.sort(reverse=False)
        return min_prob_syms[:n]
    elif rem_len == 0:
        return min_prob_syms
    else:
        # 足りない場合は再帰
        return min_prob_syms + get_min_syms(d_inv, rem_len)

def create_connection_dict(prob_d):
    prob_d_cp = prob_d.copy()
    cnct_d = {}
    next_key = max(prob_d_cp) + 1

    while len(prob_d_cp) > 1:
        prob_d_inv = {}
        # 逆引き辞書作成
        for k, v in prob_d_cp.items():
            if v in prob_d_inv:
                prob_d_inv[v].append(k)
            else:
                prob_d_inv[v] = [k]

        print(prob_d_inv)

        min_syms = get_min_syms(prob_d_inv, 2)

        prob_d_cp[next_key] = round(sum(v for k, v in prob_d_cp.items() if k in min_syms), 2)
        cnct_d[next_key] = sorted(min_syms)
        
        for i in min_syms:
            prob_d_cp.pop(i)
    
        print(prob_d_cp)
        print(cnct_d)
        next_key += 1

    return cnct_d

def generate_code(cnct_d, code_d):
    """
    枝の繋がりから符号を作成
    """
    max_key = max(cnct_d)
    children = cnct_d.pop(max_key)
    
    print(cnct_d)
    
    for i, j in enumerate(children):
        if max_key in code_d:
            code_d[j] = code_d[max_key] + str(i)
        else:
            code_d[j] = str(i)
    
    if max_key in code_d:
        code_d.pop(max_key)
    print(code_d)
    
    if any(cnct_d):
        generate_code(cnct_d, code_d)

# 1
# 多分ここだけ順番がランダムで出題される
def solve_q1_1_1(m):
    return fixed_value("2")

def solve_q1_1_2(m):
    return fixed_value("2 3")

def solve_q1_1_3(m):
    return fixed_value("1 4")

def solve_q1_1_4(m):
    ans = str(int(m.groups()[0]) * 2)
    print("最高周波数の倍 %s サンプル必要" % ans)
    return ans

def solve_q1_1_5(m):
    mg = m.groups()
    ans = str(int(mg[0]) // int(log2(int(mg[1]))))
    print("通信速度をレベルのビット数で割った %s MHz" % ans)
    return ans

def solve_q1_1_6(m):
    ans = str(1 << int(m.groups()[0]))
    print("レベルは2のビット数乗 %s" % ans)
    return ans

def solve_q1_1_7(m):
    return fixed_value("3")

# 2
def solve_q2_1_1(m):
    return fixed_value("25/36")
    
def solve_q2_1_2(m):
    return fixed_value("25/36")

def solve_q2_1_3(m):
    return fixed_value("5/324")

def solve_q2_1_4(m):
    return fixed_value("5/9")

def solve_q2_1_5(m):
    return fixed_value("1/6")

def solve_q2_1_6(m):
    return fixed_value("1/3")

def solve_q2_1_7(m):
    return fixed_value("35/18")

def solve_q2_1_8(m):
    return fixed_value("0.206")

def solve_q2_1_9(m):
    return fixed_value("0.045")

def solve_q2_1_10(m):
    return fixed_value("0.794")

# 3-1
def solve_q3_1_1(m):
    part = m.groups()[0]
    ans = str(len(part.split(" ")))
    print("%s の記号の数 %s" % (part, ans))
    return ans

def solve_q3_1_2(m):
    return fixed_value("3 4 7 8")

def solve_q3_1_3(m):
    return fixed_value("0.0504 0.0380")

def solve_q3_1_4(m):
    return fixed_value("0.128")

def solve_q3_1_5(m):
    prob_str = m.groups()[0]
    if prob_str == "0":
        print("log2(0)は定義できません")
        return "0"
    prob = float(prob_str)
    ans = "{:.3f}".format(-log2(prob))
    if ans[-1] == "0":
        ans = ans[:-1]
    print("情報量は -log2(%s) = %s ビット" % (prob, ans))
    return ans

def solve_q3_1_6(m):
    return fixed_value("")

def solve_q3_1_7(m):
    return fixed_value("1 2")

def solve_q3_1_8(m):
    return fixed_value("1")

# 3-2
def solve_q3_2_1(m):
    p_arr = [float(i) for i in m.groups()[0].split(" ")]
    print(p_arr)
    ans = "{:.2f}".format(calc_entropy(p_arr))
    ans = del_zero(ans)
    print("エントロピー %s" % ans)
    return ans

def solve_q3_2_2(m):
    """
    3-2-1と同様だが形だけ定義
    """
    return solve_q3_2_1(m)

def solve_q3_2_3(m):
    return fixed_value("2.75")

def solve_q3_2_4(m):
    p_arr = [float(i) for i in m.groups()[0].split(" ")]
    print(p_arr)
    ans = ceil(10000 * calc_entropy(p_arr))
    print("最低 %s ビット必要" % ans)
    return ans

# 4-1
def solve_q4_1_1(m):
    p_arr = [float(i) for i in m.groups()[0].split(" ")]
    print(p_arr)
    print(sum(p_arr))
    prob_dict = {k: v for k, v in enumerate(p_arr)}

    connect_dict = create_connection_dict(prob_dict)

    print("#" * 100)

    code_dict = {}
    generate_code(connect_dict, code_dict)

    sorted_keys = sorted(code_dict.keys())
    ans = ""
    for i in sorted_keys:
        ans += code_dict[i] + " "
    ans = ans[:-1]
    print(ans)
    return ans

def solve_q4_1_3(m):
    """
    正規表現でハフマン符号を復号
    """
    mg = m.groups()
    patterns = mg[:-1]
    # print(patterns)
    rem = mg[-1]
    ans = []
    while rem:
        for i, p in enumerate(patterns):
            m2 = re.match(p, rem)
            if m2:
                # print(p, rem)
                ans.append("a%d" % i)
                rem = rem[len(p):]
                break
        # 必ず何かしらの記号にマッチするはず
        else:
            break
    ans = " ".join(ans)
    print(ans)
    return ans

QUESTIONS = {
    "1": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[2]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'アナログ信号をディジタル化'), "solver": solve_q1_1_1},
            {"pattern": re.compile(r'次の情報のうち「ディジタル」'), "solver": solve_q1_1_2},
            {"pattern": re.compile(r'次の情報のうちディジタルがアナログより'), "solver": solve_q1_1_3},
            {"pattern": re.compile(r'最高周波数が (\d+) Hz'), "solver": solve_q1_1_4},
            {"pattern": re.compile(r'(\d+) Mb/s である。アナログ信号を表すために <br>\n(\d+)レベル'), "solver": solve_q1_1_5},
            {"pattern": re.compile(r'ディジタル化するとき, (\d+) ビット/サンプル'), "solver": solve_q1_1_6},
            {"pattern": re.compile(r'次の文章.*用語はなにか'), "solver": solve_q1_1_7}
        ]
    },
    "2": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[3]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'さいころを 2 回振る。このとき \d の目が 1 回も出ない'), "solver": solve_q2_1_1},
            {"pattern": re.compile(r'2 個のさいころを同時に振る。このとき \d の目が出ない'), "solver": solve_q2_1_2},
            {"pattern": re.compile(r'\d の目がちょうど 3 回'), "solver": solve_q2_1_3},
            {"pattern": re.compile(r'このとき 1 の目か 2 の目または 1 と 2 の両方'), "solver": solve_q2_1_4},
            {"pattern": re.compile(r'\d の目が出た、このとき 2 回目に \d の目'), "solver": solve_q2_1_5},
            {"pattern": re.compile(r'奇数であるとき 1 の目が 1 回'), "solver": solve_q2_1_6},
            {"pattern": re.compile(r'大きい方から小さい方を引く'), "solver": solve_q2_1_7},
            {"pattern": re.compile(r'2 元対称通信路を用いて P\(X=0\|Y=1\)'), "solver": solve_q2_1_8},
            {"pattern": re.compile(r'2 元対称通信路を用いて P\(X=1\|Y=0\)'), "solver": solve_q2_1_9},
            {"pattern": re.compile(r'2 元対称通信路を用いて P\(X=1\|Y=1\)'), "solver": solve_q2_1_10}
        ]
    },
    "3-1": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[4]/td[3]/a[1]",
        "questions": [
            {"pattern": re.compile(r'記号が｛([A-Z ]+)｝の場合'), "solver": solve_q3_1_1},
            {"pattern": re.compile(r'５元情報源において、有効'), "solver": solve_q3_1_2},
            {"pattern": re.compile(r'ある定常２元情報源から出る'), "solver": solve_q3_1_3},
            {"pattern": re.compile(r'前の問題の情報源は記憶あり'), "solver": solve_q3_1_4},
            {"pattern": re.compile(r'ある記号の発生確率が｛([0-9\.]+)｝の場合'), "solver": solve_q3_1_5},
            {"pattern": re.compile(r'</th></tr> <tr> <td>A</td><td>0.05</td><td>00 <br>'), "solver": solve_q3_1_6},
            {"pattern": re.compile(r'</th></tr> <tr> <td>A</td><td>0.1 </td><td>000 <br>'), "solver": solve_q3_1_7},
            {"pattern": re.compile(r'</th></tr> <tr> <td>A</td><td>0.5 </td><td>1 <br>'), "solver": solve_q3_1_8}
        ]
    },
    "3-2": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[4]/td[3]/a[2]",
        "questions": [
            {"pattern": re.compile(r'４元情報源の記号発生確率が｛ ([0-9\. ]+) ｝'), "solver": solve_q3_2_1},
            {"pattern": re.compile(r'５元情報源の記号発生確率が｛([0-9\. ]+)｝'), "solver": solve_q3_2_2},
            {"pattern": re.compile(r'下記符号の平均符号長'), "solver": solve_q3_2_3},
            {"pattern": re.compile(r'３元情報源の記号発生確率が｛ ([0-9\. ]+) ｝'), "solver": solve_q3_2_4}
        ]
    },
    "4-1": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[5]/td[3]/a[1]",
        "questions": [
            {"pattern": re.compile(r'確率はそれぞれ \{([0-9\. ]+)\}'), "solver": solve_q4_1_1},
            {"pattern": re.compile(r'\{a0-&gt;([01]+),a1-&gt;([01]+),a2-&gt;([01]+),a3-&gt;([01]+),a4-&gt;([01]+)\} .*\n.*\{([01]+)\}'), "solver": solve_q4_1_3},
        ]
    },
    "4-2": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[5]/td[3]/a[2]",
        "questions": [

        ]
    },
    "4-2": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[5]/td[3]/a[3]",
        "questions": [

        ]
    }
}

if __name__ == "__main__":
    print(QUESTIONS)
