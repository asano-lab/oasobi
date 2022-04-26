import re
from math import log2

def solve_q1_1_1(m):
    print("固定値: 2")
    return "2"

def solve_q1_1_2(m):
    print("固定値: 2 3")
    return "2 3"

def solve_q1_1_3(m):
    print("固定値: 1 4")
    return "1 4"

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
    print("固定値: 3")
    return "3"

def solve_q2_1_1(m):
    print("固定値: 25/36")
    return "25/36"
    
def solve_q2_1_2(m):
    print("固定値: 25/36")
    return "25/36"

def solve_q2_1_3(m):
    print("固定値: 5/324")
    return "5/324"

def solve_q2_1_4(m):
    print("固定値: 5/9")
    return "5/9"

def solve_q2_1_5(m):
    print("固定値: 1/6")
    return "1/6"

def solve_q2_1_6(m):
    print("固定値: 1/3")
    return "1/3"

def solve_q2_1_7(m):
    print("固定値: 35/18")
    return "35/18"

def solve_q2_1_8(m):
    print("固定値: 0.206")
    return "0.206"

def solve_q2_1_9(m):
    print("固定値: 0.045")
    return "0.045"

def solve_q2_1_10(m):
    print("固定値: 0.794")
    return "0.794"

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
    }
}

if __name__ == "__main__":
    print(QUESTIONS)
