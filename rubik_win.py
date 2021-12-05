from ctypes import CDLL, c_int32, c_ulonglong
import time

clib = CDLL("./rubik_win.so")

cull2 = c_ulonglong * 2

# 全動作適用後状態格納用配列
cull36 = c_ulonglong * 36

# 初期化関数を実行 (必須)
clib.init()

_applyMove = clib.applyMove
_applyMove.restype = c_int32
_applyMove.argtypes = (cull2, cull2, cull2)

_applyAllMoves = clib.applyAllMoves
_applyAllMoves.restype = c_int32
_applyAllMoves.argtypes = (cull2, cull36)

# 正規化関数
_normalState = clib.normalState
_normalState.restype = c_int32
_normalState.argtypes = (cull2,)

# 正規化した次の状態を返す
_applyAllMovesNormal = clib.applyAllMovesNormal
_applyAllMovesNormal.restype = c_int32
_applyAllMovesNormal.argtypes = (cull2, cull36)

# 日本仕様の色
JPN_COLOR = {"U": "白", "D": "青", "L": "橙", "R": "赤", "F": "緑", "B": "黄"}

# 角のブロックの色, 各3色
# U, Dの色を基準にして反時計回りに並べる
CORNER_COLOR = {
    0: "UBL", 1: "URB", 2: "UFR", 3: "ULF",
    4: "DLB", 5: "DBR", 6: "DRF", 7: "DFL"
}

CORNER_COLOR_INV = {
    "UBL": 0, "URB": 1, "UFR": 2, "ULF": 3,
    "DLB": 4, "DBR": 5, "DRF": 6, "DFL": 7
}

# 辺のブロックの色, 各2色
# 基準面の色が先頭
EDGE_COLOR = {
    0: "BL", 1: "BR", 2: "FR", 3: "FL",
    4: "UB", 5: "UR", 6: "UF", 7: "UL",
    8: "DB", 9: "DR", 10: "DF", 11: "DL"
}

EDGE_COLOR_INV = {
    "BL": 0, "BR": 1, "FR": 2, "FL": 3,
    "UB": 4, "UR": 5, "UF": 6, "UL": 7,
    "DB": 8, "DR": 9, "DF": 10, "DL": 11
}

# 色配列への変換法則 (コーナーパーツ)
CORNER_PO2COLOR = {
    0: ((0, 0), (0, 11), (0, 12)), 1: ((0, 2), (0, 8), (0, 9)),
    2: ((2, 2), (0, 5), (0, 6)), 3: ((2, 0), (0, 14), (0, 3)),
    4: ((2, 15), (2, 12), (2, 11)), 5: ((2, 17), (2, 9), (2, 8)),
    6: ((0, 17), (2, 6), (2, 5)), 7: ((0, 15), (2, 3), (2, 14))
}

# 色配列への変換法則 (エッジパーツ)
EDGE_PO2COLOR = {
    0: ((1, 11), (1, 12)), 1: ((1, 9), (1, 8)), 2: ((1, 5), (1, 6)), 3: ((1, 3), (1, 14)),
    4: ((0, 1), (0, 10)), 5: ((1, 2), (0, 7)), 6: ((2, 1), (0, 4)), 7: ((1, 0), (0, 13)),
    8: ((2, 16), (2, 10)), 9: ((1, 17), (2, 7)), 10: ((0, 16), (2, 4)), 11: ((1, 15), (2, 13))
}

# 中央パーツと色配列の添え字の対応
CENTER_INDICES = {
    "U": (1, 1), "F": (1, 4), "R": (1, 7),
    "B": (1, 10), "L": (1, 13), "D": (1, 16)
}

# 向きを含めずに位置だけ
MIRROR_POS = {
    "UD": [
        [4, 5, 6, 7, 0, 1, 2, 3],
        [0, 1, 2, 3, 8, 9, 10, 11, 4, 5, 6, 7]
    ],
    "LR": [
        [1, 0, 3, 2, 5, 4, 7, 6],
        [1, 0, 3, 2, 4, 7, 6, 5, 8, 11, 10, 9]
    ],
    "FB": [
        [3, 2, 1, 0, 7, 6, 5, 4],
        [3, 2, 1, 0, 6, 5, 4, 7, 10, 9, 8, 11]
    ]
}

# 資料通りのクラス
class State():

    def __init__(self, cp, co, ep, eo):
        self.cp = cp
        self.co = co
        self.ep = ep
        self.eo = eo
    
    def copy(self):
        return State(self.cp.copy(), self.co.copy(), self.ep.copy(), self.eo.copy())
    
    # 数値変換
    def toNum(self):
        s_num = 0
        for i in range(8):
            s_num = (s_num << 3) | self.cp[i]
            s_num = (s_num << 2) | self.co[i]
        for i in range(12):
            s_num = (s_num << 4) | self.ep[i]
            s_num = (s_num << 1) | self.eo[i]
        return s_num

    # 数値で扱うクラスに変換
    def toState2(self):
        return State2(self.toNum())
    
    # 色配列の作成 (描画用)
    def makeColorArray(self):
        color_array = [[" "] * 18 for _ in range(3)]
        for k, v in CENTER_INDICES.items():
            color_array[v[0]][v[1]] = k
        for k, v in CORNER_PO2COLOR.items():
            cpk = self.cp[k]
            cok = self.co[k]
            for i, jt in enumerate(v):
                color_array[jt[0]][jt[1]] = CORNER_COLOR[cpk][(cok + i) % 3]
        for k, v in EDGE_PO2COLOR.items():
            epk = self.ep[k]
            eok = self.eo[k]
            for i, jt in enumerate(v):
                color_array[jt[0]][jt[1]] = EDGE_COLOR[epk][eok ^ i]
        return color_array
    
    def changeColor(self, color_pattern):
        tmpst = self + change_color[color_pattern]
        rp = replace_parts[color_pattern]
        ncp = []
        nco = []
        nep = []
        neo = []
        for i, j in enumerate(tmpst.cp):
            ncp.append(rp[0][j])
            nco.append((tmpst.co[i] + rp[1][j]) % 3)
        for i, j in enumerate(tmpst.ep):
            nep.append(rp[2][j])
            neo.append(tmpst.eo[i] ^ rp[3][j])
        return State(ncp, nco, nep, neo)
    
    # 上下鏡写しの等価盤面を作りたい
    def mirror(self, mirror_pattern):
        mp = MIRROR_POS[mirror_pattern]
        tmpst = State(
            [self.cp[i] for i in mp[0]],
            [-self.co[i] % 3 for i in mp[0]],
            [self.ep[i] for i in mp[1]],
            [self.eo[i] for i in mp[1]]
        )
        nst = tmpst.copy()
        nst.cp = [mp[0][i] for i in tmpst.cp]
        nst.ep = [mp[1][i] for i in tmpst.ep]
        return nst
    
    # 動作の適用
    # + 演算子を用いる
    def __add__(self, arg):
        ncp = []
        nco = []
        nep = []
        neo = []
        for i, j in enumerate(arg.cp):
            ncp.append(self.cp[j])
            nco.append((self.co[j] + arg.co[i]) % 3)
        for i, j in enumerate(arg.ep):
            nep.append(self.ep[j])
            neo.append(self.eo[j] ^ arg.eo[i])
        return State(ncp, nco, nep, neo)
    
    def __mul__(self, arg: int):
        if arg <= 0:
            return solved
        s_add = self.copy()
        ns = s_add
        for _ in range(arg - 1):
            ns += s_add
        return ns
    
    def __str__(self):
        moji = str(self.cp) + "\n"
        moji += str(self.co) + "\n"
        moji += str(self.ep) + "\n"
        moji += str(self.eo) + "\n"
        color_array = self.makeColorArray()
        for ca in color_array:
            for i, c in enumerate(ca):
                moji += JPN_COLOR[c]
                if i % 3 == 2:
                    moji += " "
            moji += "\n"
        return moji

class State2():

    def __init__(self, num: int):
        self.num = num
        self.c_arr = cull2(num >> 60, num & 0xfffffffffffffff)
    
    def toState(self):
        cp = []
        co = []
        ep = []
        eo = []
        for i in range(0, 40, 5):
            cp.append(self.num >> (97 - i) & 0b111)
            co.append(self.num >> (95 - i) & 0b11)
        for i in range(0, 60, 5):
            ep.append(self.num >> (56 - i) & 0b1111)
            eo.append(self.num >> (55 - i) & 0b1)
        return State(cp, co, ep, eo)
    
    def allNextStates(self):
        nc_arr = cull36()
        _applyAllMoves(self.c_arr, nc_arr)
        n_list = list(nc_arr)
        return [State2(n_list[i] << 60 | n_list[i + 1]) for i in range(0, 36, 2)]
    
    def __add__(self, arg):
        nc_arr = cull2()
        _applyMove(self.c_arr, arg.c_arr, nc_arr)
        n_list = list(nc_arr)
        return State2(n_list[0] << 60 | n_list[1])
    
    def __str__(self):
        c_info = self.num >> 60
        e_info = self.num & 0xfffffffffffffff
        return "0x%010x, 0x%015x" % (c_info, e_info)

# 完成形
solved = State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
)

# 基本動作
moves = {
    "U": State(
        [3, 0, 1, 2, 4, 5, 6, 7],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    "D": State(
        [0, 1, 2, 3, 5, 6, 7, 4],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    "L": State(
        [4, 1, 2, 0, 7, 5, 6, 3],
        [2, 0, 0, 1, 1, 0, 0, 2],
        [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    "R": State(
        [0, 2, 6, 3, 4, 1, 5, 7],
        [0, 1, 2, 0, 0, 2, 1, 0],
        [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    "F": State(
        [0, 1, 3, 7, 4, 5, 2, 6],
        [0, 0, 1, 2, 0, 0, 2, 1],
        [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    ),
    "B": State(
        [1, 5, 2, 3, 0, 4, 6, 7],
        [1, 2, 0, 0, 2, 1, 0, 0],
        [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    )
}

# 残りの基本操作を追加
faces = list(moves.keys())
for face_name in faces:
    moves[face_name + "2"] = moves[face_name] * 2
    moves[face_name + "'"] = moves[face_name] * 3

faces = [
    "U", "D", "L", "R", "F", "B", "U2", "U'", "D2", "D'", "L2", "L'",
    "R2", "R'", "F2", "F'", "B2", "B'"
]

# 色変換のための操作 (位置と回転のみ)
# 全23種
# キーは上面と正面の順
change_color = {
    # UDBFLR
    "UL": State(
        [3, 0, 1, 2, 7, 4, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 1, 2, 7, 4, 5, 6, 11, 8, 9, 10],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    # FBLRDU
    "FD": State(
        [4, 5, 1, 0, 7, 6, 2, 3],
        [2, 1, 2, 1, 1, 2, 1, 2],
        [11, 9, 5, 7, 8, 1, 4, 0, 10, 2, 6, 3],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    ),
    # RLUDFB
    "RF": State(
        [4, 0, 3, 7, 5, 1, 2, 6],
        [1, 2, 1, 2, 2, 1, 2, 1],
        [8, 4, 6, 10, 0, 7, 3, 11, 1, 5, 2, 9],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    )
}

# 残りの色変換は最初の3種から作成
change_color["UB"] = change_color["UL"] * 2
change_color["UR"] = change_color["UL"] * 3
change_color["DB"] = change_color["FD"] * 2
change_color["BU"] = change_color["FD"] * 3
change_color["DF"] = change_color["RF"] * 2
change_color["LF"] = change_color["RF"] * 3
change_color["LD"] = change_color["FD"] + change_color["UL"]
change_color["BD"] = change_color["LD"] + change_color["UL"]
change_color["RD"] = change_color["BD"] + change_color["UL"]
change_color["FL"] = change_color["UL"] + change_color["FD"]
change_color["DL"] = change_color["FL"] + change_color["FD"]
change_color["BL"] = change_color["DL"] + change_color["FD"]
change_color["DR"] = change_color["DB"] + change_color["UL"]
change_color["LB"] = change_color["LD"] + change_color["FD"]
change_color["LU"] = change_color["LB"] + change_color["FD"]
change_color["RB"] = change_color["RD"] + change_color["FD"]
change_color["RU"] = change_color["RB"] + change_color["FD"]
change_color["FU"] = change_color["FL"] + change_color["RF"]
change_color["FR"] = change_color["FU"] + change_color["RF"]
change_color["BR"] = change_color["BU"] + change_color["RF"]

def cleateReplaceParts(chclr: State):
    ll = [[-1] * 8, chclr.co.copy(), [-1] * 12, chclr.eo.copy()]
    for i, j in enumerate(chclr.cp):
        ll[0][j] = i
        ll[1][j] = -chclr.co[i] % 3
    for i, j in enumerate(chclr.ep):
        ll[2][j] = i
        ll[3][j] = chclr.eo[i]
    return ll

def num2state(num: int) -> State:
    """
    数値からStateに変換
    """
    cp = []
    co = []
    ep = []
    eo = []
    for i in range(0, 40, 5):
        cp.append(num >> (97 - i) & 0b111)
        co.append(num >> (95 - i) & 0b11)
    for i in range(0, 60, 5):
        ep.append(num >> (56 - i) & 0b1111)
        eo.append(num >> (55 - i) & 0b1)
    if len(set(cp)) != 8 or len(set(ep)) != 12:
        return None
    return State(cp, co, ep, eo)

def applyAllMovesNormal(num: int) -> list:
    """
    一手後の正規化した状態のリストを返す
    """
    c_arr = cull2(num >> 60, num & 0xfffffffffffffff)
    nc_arr = cull36()
    _applyAllMovesNormal(c_arr, nc_arr)
    return [nc_arr[i] << 60 | nc_arr[i + 1] for i in range(0, 36, 2)]

class Search:

    def __init__(self):
        # 完成状態付近
        self.solved_neighbors = {0: set([solved.toNum()])}

    def searchSolvedNeighbors(self):
        t0 = time.time()
        depth = max(self.solved_neighbors)
        print("深さ%dの探索" % (depth + 1))
        nsts = []
        for st_num in self.solved_neighbors[depth]:
            nsts += applyAllMovesNormal(st_num)
        print("新状態数（重複あり）: %d" % len(nsts))
        nsts = set(nsts)
        for past_sts in self.solved_neighbors.values():
            nsts -= past_sts
        print("新状態数（重複なし）：%d" % len(nsts))
        self.solved_neighbors[depth + 1] = nsts
        print("所要時間：%6.2f秒" % (time.time() - t0))

def circularRShiftStr(moji: str, n: int) -> str:
    """
    n文字右シフト
    """
    l = len(moji)
    n = l - n % l
    return moji[n:] + moji[:n]

# 色配列を順列・方向の配列に変換
def colorArray2State(color_array: list) -> State:
    cp = [-1] * 8
    co = [-1] * 8
    ep = [-1] * 12
    eo = [-1] * 12
    # コーナー情報
    for k, v in CORNER_PO2COLOR.items():
        p_colors = ""
        for sub1, sub2 in v:
            p_colors += color_array[sub1][sub2]
        for i in range(3):
            spc = circularRShiftStr(p_colors, i)
            if spc in CORNER_COLOR_INV:
                cp[k] = CORNER_COLOR_INV[spc]
                co[k] = i
                break
        else:
            return None
    # エッジ情報
    for k, v in EDGE_PO2COLOR.items():
        p_colors = ""
        for sub1, sub2 in v:
            p_colors += color_array[sub1][sub2]
        for i in range(2):
            spc = circularRShiftStr(p_colors, i)
            if spc in EDGE_COLOR_INV:
                ep[k] = EDGE_COLOR_INV[spc]
                eo[k] = i
                break
        else:
            return None
    # パーツの重複チェック
    if len(set(cp)) != 8 or len(set(ep)) != 12:
        return None
    return State(cp, co, ep, eo)

# 標準入力
def inputState():
    # どうしても数値で入力したい人用
    mens = "UDLRFB"
    # 入力する面の順番
    input_order = "UFRBLD"
    # 色を標準入力から取得する際の置き方
    input_uf = {
        "U": "F", "F": "D", "R": "D",
        "B": "D", "L": "D", "D": "B"
    }
    # 日本配色と面の対応
    jpc2men = {
        "w": "U", "b": "D", "o": "L",
        "r": "R", "g": "F", "y": "B"
    }
    print("ルービックキューブの状態を入力.")
    print("入力する順番は\n1 2 3\n4 5 6\n7 8 9\nです.")
    print("色の頭文字, 面または面の番号で入力してください.")
    print("白: (0, w, U), 青: (1, b, D), 橙: (2, o, L), 赤: (3, r, R), 緑: (4, g, F), 黄: (5, y, B)")
    print("最初からやり直したい場合は \"!\" を入力してください.")
    color_array = [[-1] * 18 for _ in range(3)]
    st = None
    while st is None:
        i = 0
        while i < 6:
            men = input_order[i]
            try:
                moji = input("中央が「{:s}」の面を上にし、「{:s}」を正面に持って上の色を入力してください：".format(JPN_COLOR[men], JPN_COLOR[input_uf[men]]))
            except KeyboardInterrupt:
                return None
            if not moji:
                continue
            if moji[0] == "!":
                break
            if moji[:2] == "0x":
                try:
                    r_num = int(moji, 0)
                except ValueError:
                    print("数値変換できません.")
                    break
                st = num2state(r_num)
                break
            if (len(moji) < 9):
                print("文字数が不足しています.")
                break
            for j, c in enumerate(moji):
                if j >= 9:
                    continue
                sub1 = j // 3
                sub2 = i * 3 + j % 3
                # 数値でもいい
                if c.isdecimal():
                    cn = int(c, 0)
                    if 0 <= cn and cn < 6:
                        color_array[sub1][sub2] = mens[cn]
                    else:
                        print("無効な入力です.")
                        break
                # 色頭文字
                elif c in jpc2men:
                    color_array[sub1][sub2] = jpc2men[c]
                # 面
                elif c in mens:
                    color_array[sub1][sub2] = c
                else:
                    print("無効な入力です.")
                    break
            else:
                i += 1
        if i >= 6:
            st = colorArray2State(color_array)
    return st

# パーツの入れ替え辞書を作成
replace_parts = {}
for k, v in change_color.items():
    replace_parts[k] = cleateReplaceParts(v)

scramble = "L D2 R U2 L F2 U2 L F2 R2 B2 R U' R' U2 F2 R' D B' F2"
scramble = scramble.split()

scramble_udm = "L' U2 R' D2 L' F2 D2 L' F2 R2 B2 R' D R D2 F2 R U' B F2"
scramble_udm = scramble_udm.split()

scrambled_state = solved.toState2()
for move_name in scramble:
    scrambled_state += moves[move_name].toState2()

scrambled_state = scrambled_state.toState()
# print(scrambled_state)

# Cで格納するための順番
cl_list = [
    "UL", "UR", "UB", "DF", "DL", "DR", "DB",
    "LU", "LD", "LF", "LB", "RU", "RD", "RF", "RB",
    "FU", "FD", "FL", "FR", "BU", "BD", "BL", "BR"
]

srch = Search()
for i in range(5):
    srch.searchSolvedNeighbors()
