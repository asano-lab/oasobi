import code
import re
import numpy as np
import unicodedata
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

def del_zero(ans: str) -> str:
    """
    無駄な0を削除
    小数部がなくなったら.も削除
    整数部は0でも残す
    """
    while ans[-1] in "0." and len(ans) > 1:
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

def run_length_each_prob(Pb, N):
    """
    各長さの確率
    """
    return np.array([(1 - Pb) ** i * Pb for i in range(N)] + [(1 - Pb) ** N])

def calc_source_len_mean(Pb, N):
    """
    情報源の長さの平均値
    """
    return (1 - (1 - Pb) ** N) / Pb

# 1
# 順不同出題
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
    ans = del_zero(ans)
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
    """
    2問目も兼ねている
    """
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

# 4-2
def solve_q4_2_1(m):
    """
    ランレングス符号化 (ただ区切るだけ)
    """
    mg = m.groups()
    symbol_series = mg[0]
    r_max = int(mg[1])
    print(r_max)
    print(symbol_series)
    r = 1
    r_list = []
    for s in symbol_series:
        if s == "B":
            r_list.append(r - 1)
            r = 1
        elif r < r_max:
            r += 1
        else:
            r_list.append(r)
            r = 1
    if r > 1:
        r_list.append(r)

    ans = " ".join([str(i) for i in r_list])
    print(ans)
    return ans

def solve_q4_2_3(m):
    """
    ランレングス・ハフマン符号
    """
    Pb = float(m.groups()[0])
    N = 4

    prob_arr = run_length_each_prob(Pb, N)
    print(prob_arr, prob_arr.sum())

    prob_dict = {k: v for k, v in enumerate(prob_arr)}

    connect_dict = create_connection_dict(prob_dict)

    print("#" * 100)

    code_dict = {}
    generate_code(connect_dict, code_dict)

    len_arr = np.array([len(code_dict[k]) for k in sorted(code_dict.keys())])

    codeword_len_mean = np.dot(prob_arr, len_arr)
    print("L = %f" % codeword_len_mean)
    source_len_mean = calc_source_len_mean(Pb, N)
    print("n_N = %f" % source_len_mean)

    ans = "{:.3f}".format(codeword_len_mean / source_len_mean)
    print("l_N = %s" % ans)
    return ans

# 4-3
def solve_q4_3_1(m):
    """
    ZL符号
    """
    symbol_series = m.groups()[0]
    codes = []
    known_patterns = {}

    i = 0
    rem = ""
    while i < len(symbol_series):
        for j in range(i):
            for l in range(1, i - j + 1):
                pattern = symbol_series[j:j+l]
                if pattern not in known_patterns:
                    known_patterns[pattern] = (j, l)
        for j in range(i, 0, -1):
            pattern = symbol_series[i:i + j]
            # print(i, j, pattern)
            if pattern in known_patterns:
                if i + j >= len(symbol_series):
                    print(i, j, pattern)
                    rem = pattern
                    print("末尾余り: %s" % rem)
                    i = float("inf")
                else:
                    print(i, j, pattern)
                    codes.append(known_patterns[pattern] + (symbol_series[i+j],))
                    i += j + 1
                break
        else:
            print(0, 0, symbol_series[i])
            codes.append((0, 0, symbol_series[i]))
            i += 1
        print("#" * 50)
        
    # print(known_patterns)
    print(codes)

    ans = ""
    for i in codes:
        ans += "%d " % (i[1] + 1)
    if len(rem) > 0:
        ans += "%d" % len(rem)
    else:
        ans = ans[:-1]
    print(ans)
    return ans

def solve_q4_3_2(m):
    """
    実用的なZL符号化
    """
    symbol_series = m.groups()[0]

    offset_bit = 3
    length_bit = 2

    offset = 1 << offset_bit
    length = 1 << length_bit

    buffer = "A" * offset + symbol_series[:length]

    symbol_remain = symbol_series[length:]

    codes = []
    while len(buffer) > offset:
        print(buffer[:offset] + "|" + buffer[offset:])
        print(symbol_remain)
        
        known_patterns = {}
        for i in range(offset):
            for j in range(i + 1, offset + 1):
                pattern = buffer[i:j]
                if pattern not in known_patterns:
                    known_patterns[pattern] = (i, j - i)
    #     print(known_patterns)
        for l in range(len(buffer) - offset - 1, 0, -1):
            pattern = buffer[offset:offset+l]
            print(i, j, pattern)
            if pattern in known_patterns:
                codes.append(known_patterns[pattern] + (buffer[offset + l],))
                buffer = buffer[l+1:] + symbol_remain[:l+1]
                symbol_remain = symbol_remain[l+1:]
                break
        else:
            codes.append((0, 0, buffer[offset]))
            buffer = buffer[1:] + symbol_remain[:1]
            symbol_remain = symbol_remain[1:]
        print("#" * 50)
    print(codes)

    ans = ""
    for i in codes:
        ans += format(i[0], "0%db" % offset_bit) + format(i[1], "0%db" % length_bit) + str((i[2] == "B") * 1) + " "
    ans = ans[:-1]
    print(ans)
    return ans

def solve_q4_3_3(m):
    """
    実用的なZL符号の復号
    """
    offset_bit = 4
    length_bit = 3

    codes = m.groups()[0].split(" ")
    codes = [(int(i[:offset_bit], 2), int(i[offset_bit:offset_bit+length_bit], 2), chr(ord("A") + int(i[-1]))) for i in codes]
    print(codes)

    offset = 1 << offset_bit

    buffer = "A" * offset
    ans = ""

    print(buffer[:offset] + "|" + buffer[offset:])
    for i in codes:
        print(i)
        pattern = buffer[i[0]:i[0]+i[1]] + i[2]
        ans += pattern
        buffer = (buffer + pattern)[i[1]+1:]
        print(buffer[:offset] + "|" + buffer[offset:])

    # print(buffer[:offset] + "|" + buffer[offset:] + "\n")
    print(ans)
    return ans

# 5
def solve_q5_1_1(m):
    ball_count = [int(i) for i in m.groups()]
    joint_prob_arr = []

    for color, count1 in enumerate(ball_count):
        px_color = count1 / sum(ball_count)
        ball_count_second = ball_count.copy()
        ball_count_second[color] -= 1
        for count2 in ball_count_second:
            py_color = count2 / sum(ball_count_second)
            joint_prob_arr.append(px_color * py_color)
    
    print("同時確率分布", joint_prob_arr)
    ans = "{:.2f}".format(calc_entropy(joint_prob_arr))
    ans = del_zero(ans)
    print("結合エントロピー: %s" % ans)
    return ans

def solve_q5_1_2(m):
    ball_count = [int(i) for i in m.groups()]
    e = 0

    for color, count1 in enumerate(ball_count):
        px_color = count1 / sum(ball_count)
        ball_count_second = ball_count.copy()
        ball_count_second[color] -= 1
        for count2 in ball_count_second:
            if count2 == 0:
                continue
            py_color = count2 / sum(ball_count_second)
            e -= px_color * py_color * log2(py_color)
    
    ans = del_zero("{:.2f}".format(e))
    print("条件付きエントロピー H(Y|X) = %s" % ans)
    return ans

def solve_q5_1_3(m):
    return fixed_value("3 6 8")

def solve_q5_1_4(m):
    """
    2元対称通信路の相互情報量
    """
    pe, px0 = tuple(float(i) for i in m.groups())

    pxl = [px0, 1 - px0]

    py0 = px0 * (1 - pe) + (1 - px0) * pe
    pyl = [py0, 1 - py0]

    # 例外処理
    # Xの値が固定ならもともと情報を持たない
    if px0 < 1e-10 or (1 - px0) < 1e-10:
        Iyx = 0.0

    # 誤り率が0ならどちらかを知れば全てわかる
    elif pe < 1e-10 or (1 - pe) < 1e-10:
        Iyx = calc_entropy(pxl)

    else:
        Iyx = calc_entropy(pyl)
        
        for i, pxi in enumerate(pxl):
            for j in range(len(pyl)):
                if i == j:
                    Iyx += pxi * (1 - pe) * log2(1 - pe)
                else:
                    Iyx += pxi * pe * log2(pe)

    ans = del_zero("{:.2f}".format(Iyx))
    print("相互情報量: %s" % ans)
    return ans

def solve_q5_1_5(m):
    return fixed_value("0")

# 6
def solve_q6_1_1(m):
    """
    2元対称通信路における通信路容量
    相互情報量の最大値
    """
    pe = float(m.groups()[0])

    if pe < 1e-10 or (1 - pe) < 1e-10:
        C = 1
    else:
        C = 1 + pe * log2(pe) + (1 - pe) * log2(1 - pe)
    
    ans = del_zero("{:.3f}".format(C))
    print("通信路容量: %s" % ans)
    return ans

def solve_q6_1_2(m):
    pa, pb, pc = [float(i) for i in m.groups()]
    ans = del_zero("{:.3f}".format(1.0 * pb * pc))
    print("確率: %s" % ans)
    return ans

def solve_q6_1_3(m):
    pa, pb, pc = [float(i) for i in m.groups()]
    p0e = 0
    p1e = 3 * pb * (1 - pb) ** 2 + (1 - pb) ** 3
    p2e = 3 * pc * (1 - pc) ** 2 + (1 - pc) ** 3
    ans = del_zero("{:.3f}".format((p0e + p1e + p2e) / 3))
    print("平均誤り率: %s" % ans)
    return ans

def solve_q6_1_4(m):
    pe = float(m.groups()[0])
    ans = del_zero("{:.2f}".format(1 - pe))
    print("情報速度 %s 未満なら可能" % ans)
    return ans

# 7-1
def solve_q7_1_1(m):
    hamming_weights = [sum(j == "1" for j in i) for i in m.groups()]
    ans = " ".join([str(i) for i in hamming_weights])
    print("ハミング重み: %s" % ans)
    return ans

def solve_q7_1_2(m):
    codewords = [int(i.replace(" ", ""), 2) for i in m.groups()]
    hamming_distances = []
    for i in range(0, len(codewords), 2):
        hamming_distances.append(sum(j == "1" for j in format(codewords[i] ^ codewords[i + 1], "b")))
    ans = " ".join([str(i) for i in hamming_distances])
    print("ハミング距離: %s" % ans)
    return ans

def solve_q7_1_3(m):
    ans = " ".join([str(int(i) - 1) for i in m.groups()])
    print("検出可能ビット数: %s" % ans)
    return ans

def solve_q7_1_4(m):
    ans = " ".join([str((int(i) - 1) // 2) for i in m.groups()])
    print("訂正可能ビット数: %s" % ans)
    return ans

def solve_q7_1_5(m):
    return fixed_value("1 2")

# 7-2
def solve_q7_2_1(m):
    mg = m.groups()
    G = np.matrix([[int(j) for j in i.split("　")] for i in mg[:3]])
    info_series = np.matrix([[int(j) for j in i] for i in mg[3].split(" ")])
    print(info_series)
    print(G)
    return ""

QUESTIONS = {
    "1": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[2]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'アナログ信号をディジタル化'), "solver": solve_q1_1_1},
            {"pattern": re.compile(r'次の情報のうち「ディジタル」'), "solver": solve_q1_1_2},
            {"pattern": re.compile(r'次の情報のうちディジタルがアナログより'), "solver": solve_q1_1_3},
            {"pattern": re.compile(r'最高周波数が (\d+) Hz'), "solver": solve_q1_1_4},
            {"pattern": re.compile(r'送信できるのは、(\d+) Mb/s である.*\n(\d+)レベル'), "solver": solve_q1_1_5},
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
            {"pattern": re.compile(r'発生された記号は \{([WB]+)\}.*\n.*Ｎ＝([０-９])を使用'), "solver": solve_q4_2_1},
            {"pattern": re.compile(r'Ｐ（Ｂ）＝ ([0-9\.]+)'), "solver": solve_q4_2_3}
        ]
    },
    "4-3": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[5]/td[3]/a[3]",
        "questions": [
            {"pattern": re.compile(r'記号系列は \{([AB]+)\}.*\n.*区切りなさい'), "solver": solve_q4_3_1},
            {"pattern": re.compile(r'記号系列は \{([AB]+)\}.*\n.*実用的'), "solver": solve_q4_3_2},
            {"pattern": re.compile(r'([01 ]+) <br>\n復号しなさい'), "solver": solve_q4_3_3}
        ]
    },
    "5": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[6]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'白、赤、青のボールがそれぞれ \{(\d) (\d) (\d)\}.*\n.*\n.*\n.*結合'), "solver": solve_q5_1_1},
            {"pattern": re.compile(r'白、赤、青のボールがそれぞれ \{(\d) (\d) (\d)\}.*\n.*\n.*\n.*条件'), "solver": solve_q5_1_2},
            {"pattern": re.compile(r'ＸとＹに対する各種情報量'), "solver": solve_q5_1_3},
            {"pattern": re.compile(r'誤る確率と入力Ｘ＝０を使う確率はそれぞれ \{([0-9\.]+) ([0-9\.]+)\}'), "solver": solve_q5_1_4},
            {"pattern": re.compile(r'普通のさいころを２回振る'), "solver": solve_q5_1_5}
        ]
    },
    "6": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[7]/td[3]/a",
        "questions": [
            {"pattern": re.compile(r'pが ([0-9\.]+) の場合、通信路容量'), "solver": solve_q6_1_1},
            {"pattern": re.compile(r'それぞれ \{([0-9\.]+) ([0-9\.]+) ([0-9\.]+)\} の場合'), "solver": solve_q6_1_2},
            {"pattern": re.compile(r'それぞれ \{([0-9\.]+) ([0-9\.]+) ([0-9\.]+)\} である'), "solver": solve_q6_1_3},
            {"pattern": re.compile(r'誤る確率pが ([0-9\.]+) の場合'), "solver": solve_q6_1_4}
        ]
    },
    "7-1": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[8]/td[3]/a[1]",
        "questions": [
            {"pattern": re.compile(r'<li> ([01 ]+) <br>\n.*<li> ([01 ]+) <br>\n.*<li> ([01 ]+) <br>'), "solver": solve_q7_1_1},
            {"pattern": re.compile(r'<li> ([01 ]+), ([01 ]+) <br>\n.*<li> ([01 ]+), ([01 ]+) <br>\n.*<li> ([01 ]+), ([01 ]+) <br>'), "solver": solve_q7_1_2},
            {"pattern": re.compile(r'検出.*\n.*<li> (\d+) <br>\n.*<li> (\d+) <br>\n.*<li> (\d+) <br>'), "solver": solve_q7_1_3},
            {"pattern": re.compile(r'訂正.*\n.*<li> (\d+) <br>\n.*<li> (\d+) <br>\n.*<li> (\d+) <br>'), "solver": solve_q7_1_4},
            {"pattern": re.compile(r'どの符号が線形符号？'), "solver": solve_q7_1_5}
        ]
    },
    "7-2": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[8]/td[3]/a[2]",
        "questions": [
            {"pattern": re.compile(r'\|([01　]+)\|.*\n.*\|([01　]+)\|.*\n.*\|([01　]+)\|.*\n.*\n.*\n\{([01 ]+)\}'), "solver": solve_q7_2_1},
        ]
    },
    "7-3": {
        "xpath": "/html/body/div[2]/ol/li[1]/p/table/tbody/tr[8]/td[3]/a[3]",
        "questions": [

        ]
    }
}

if __name__ == "__main__":
    print(QUESTIONS)
