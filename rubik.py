#!/usr/bin/python3
from ctypes import CDLL, c_int32, c_ulonglong
import time
import os
import pickle
import json
import random
import numpy as np
import shutil
import re

clib = CDLL("./rubik.so")

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

ST_LEN_MAX = 1000000

# 9にしてみる
SOLVED_NEIGHBOR_DEPTH_MAX = 9

LOOP_MAX = 2000

DIR_PATH = "./dat2/"
NP_DIR_PATH = "./np_dat/"
SMP_DIR_PATH = "./samples/"

SN_PATH_FORMAT = DIR_PATH + "act{:03d}_{:03d}.pickle"
NP_SN_PATH_FORMAT = NP_DIR_PATH + "act{:03d}_{:03d}.npy"

# サンプルファイルフォーマット
# 数値は判定できる最大手数
SMP_PATH_FORMAT = SMP_DIR_PATH + "sample{:03d}.pickle"

LOG_PATH = None
# LOG_PATH = "./log/collect_sample_log.txt"

# 秒を時間分秒のタプルで返す
def s2hms(s):
    s = int(s)
    return s // 3600, s % 3600 // 60, s % 60

# ログファイルに書き出し
def printLog(moji="", end="\n"):
    if LOG_PATH is None:
        print(moji, end=end)
    else:
        with open(LOG_PATH, "a") as f:
            print(moji, file=f, end=end)

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
    def toNum(self) -> int:
        s_num = 0
        for i in range(8):
            s_num = (s_num << 3) | self.cp[i]
            s_num = (s_num << 2) | self.co[i]
        for i in range(12):
            s_num = (s_num << 4) | self.ep[i]
            s_num = (s_num << 1) | self.eo[i]
        return s_num
    
    # 数値変換と正規化
    def toNumNormal(self):
        return normalState(self.toNum())

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
    
    # 全動作適用後の状態を辞書で返す
    def applyAllMoves(self):
        return {k: self + v for k, v in moves.items()}
    
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
        moji += hex(self.toNum()) + "\n"
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

moves_list = [
    "U", "D", "L", "R", "F", "B", "U2", "U'", "D2", "D'",
    "L2", "L'", "R2", "R'", "F2", "F'", "B2", "B'"
]

# 残りの基本操作を追加
faces = list(moves.keys())
for face_name in faces:
    moves[face_name + "2"] = moves[face_name] * 2
    moves[face_name + "'"] = moves[face_name] * 3

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

# パーツの入れ替え辞書を作成
replace_parts = {}
for k, v in change_color.items():
    replace_parts[k] = cleateReplaceParts(v)

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

def normalState(num: int) -> int:
    """
    正規化関数
    """
    c_arr = cull2(num >> 60, num & 0xfffffffffffffff)
    _normalState(c_arr)
    return c_arr[0] << 60 | c_arr[1]

def applyAllMovesNormal(num: int) -> list:
    """
    一手後の正規化した状態のリストを返す
    """
    c_arr = cull2(num >> 60, num & 0xfffffffffffffff)
    nc_arr = cull36()
    _applyAllMovesNormal(c_arr, nc_arr)
    return [nc_arr[i] << 60 | nc_arr[i + 1] for i in range(0, 36, 2)]

def randomScramble(n: int) -> State:
    """
    指定した回数だけ完成状態からランダムに動かす.
    最短路は必ず引数以下になる.
    """
    st = solved.copy()
    for _ in range(n):
        move_name = random.choice(moves_list)
        printLog(move_name, end=" ")
        st += moves[move_name]
    printLog()
    return st

def randomScrambleDependent(n: int) -> State:
    """
    依存関係にある動作のみでランダムに動かす.
    R, R2やR, L, Rなど明らかに冗長なものを排除.
    """
    ind_faces = {"U": "D", "D": "U", "R": "L", "L": "R", "F": "B", "B": "F"}
    st = solved.copy()
    prev_faces = []
    count = 0
    while count < n:
        move_name = random.choice(moves_list)
        face = move_name[0]
        if face in prev_faces:
            continue
        if len(prev_faces) == 1 and ind_faces[face] == prev_faces[0]:
            prev_faces.append(face)
        else:
            prev_faces = [face]
        st += moves[move_name]
        printLog(move_name, end=" ")
        count += 1
    printLog()
    return st

class Search:
    SUBSET_MAX = 1000000

    def __init__(self, target: State, snd_max=8):
        self.target = target.copy()
        self.snd_max = snd_max
        self.target_num = normalState(target.toNum())
        # 完成状態付近
        self.solved_neighbors = {0: set([solved.toNum()])}
        # ターゲット付近
        self.target_neighbors = {0: set([self.target_num])}
        self.solved_neighbors_depth = 0
        self.target_neighbors_depth = 0
        self.common_states = set()
        self.common_sub = -1
        self.route = []
        self.dist = -1

    def calcSolvedNeighbors(self, depth):
        """
        完成状態の近所を探索する
        """
        for _ in range(depth):
            self._calcNeighbors(self.solved_neighbors)
        self.solved_neighbors_depth = max(self.solved_neighbors)

    def searchTargetInSolvedNeighbors(self):
        """
        完成状態の近所にターゲットが含まれているか確認
        一方向探索
        """
        for k, v in self.solved_neighbors.items():
            if self.target in v:
                self.dist = k
                return k
        return -1
    
    def searchTargetBid(self, depth):
        """
        双方向探索
        引数にはターゲット側からの探索深さを指定する
        """
        dist = self.searchTargetInSolvedNeighbors()
        if dist >= 0:
            return dist
        for _ in range(depth):
            self._calcNeighbors(self.target_neighbors)
            self.target_neighbors_depth = max(self.target_neighbors)
            # 共通部分を計算
            cmns = self.solved_neighbors[self.solved_neighbors_depth] & self.target_neighbors[self.target_neighbors_depth]
            if cmns:
                self.common_states = cmns
                self.dist = self.solved_neighbors_depth + self.target_neighbors_depth
                return self.dist
        return -1

    def searchWithDat(self, tnd: int):
        """
        完成状態近傍はファイルに保存されているものとして探索
        引数は逆探索の深さ
        """
        snd_max_sub = -1
        printLog("%d手以内を探索" % self.snd_max)
        # 片方向探索から
        for i in range(self.snd_max + 1):
            for j in range(LOOP_MAX):
                fnamer = SN_PATH_FORMAT.format(i, j)
                if not os.path.exists(fnamer):
                    break
                snd_max_sub = j
                # printLog(fnamer)
                with open(fnamer, "rb") as f:
                    known_states = pickle.load(f)
                # 見つかったら終了
                if self.target_num in known_states:
                    self.dist = i
                    printLog("発見")
                    return self.dist
        printLog("双方向探索開始")
        # ターゲット付近
        self.target_neighbors = {0: set([self.target_num])}
        for _ in range(tnd):
            self._calcNeighbors(self.target_neighbors)
            self.target_neighbors_depth = max(self.target_neighbors)
            for j in range(snd_max_sub + 1):
                fnamer = SN_PATH_FORMAT.format(self.snd_max, j)
                # printLog(fnamer)
                with open(fnamer, "rb") as f:
                    known_states = pickle.load(f)
                # 共通部分を計算
                cmns = known_states & self.target_neighbors[self.target_neighbors_depth]
                if cmns:
                    self.common_states = cmns
                    self.common_sub = j
                    self.dist = self.snd_max + self.target_neighbors_depth
                    # printLog(cmns)
                    # printLog(self.dist)
                    return self.dist
        return -1
        
    def searchWithDat2(self, tnd: int):
        """
        完成状態近傍はファイルに保存されているものとして探索.
        引数は逆探索の深さ.
        ファイルを読み込む回数をできるだけ減らしたい.
        最後の深さを探索する場合, 部分集合でチェックしていく.
        手数が少ない状態の探索にはかえって効率が悪い.
        """
        t0 = time.time()
        printLog("%d手未満を探索" % self.snd_max)
        # まずは完成状態近傍の最深ファイル以外をチェック
        for i in range(self.snd_max):
            for j in range(LOOP_MAX):
                fnamer = SN_PATH_FORMAT.format(i, j)
                if not os.path.exists(fnamer):
                    break
                with open(fnamer, "rb") as f:
                    known_states = pickle.load(f)
                # 見つかったら終了
                if self.target_num in known_states:
                    self.dist = i
                    self.target_neighbors_depth = 0
                    printLog("発見")
                    return self.dist
        printLog("経過時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
        # ターゲット近傍の探索開始
        printLog("逆方向探索")
        while max(self.target_neighbors) < tnd - 1:
            self._calcNeighbors(self.target_neighbors)
        printLog("経過時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
        # 完成状態近傍最深ファイルをチェック
        printLog("%d手以上%d手未満を探索" % (self.snd_max, self.snd_max + tnd))
        cmns_dic = {k: [] for k in self.target_neighbors}
        snd_max_sub = -1
        min_dist = tnd
        for i in range(LOOP_MAX):
            fnamer = SN_PATH_FORMAT.format(self.snd_max, i)
            if not os.path.exists(fnamer):
                break
            snd_max_sub = i
            # printLog(fnamer)
            with open(fnamer, "rb") as f:
                known_states = pickle.load(f)
            # 各集合との共通部分を計算 (和はリストが速い(?))
            for k, v in self.target_neighbors.items():
                cmns = list(known_states & v)
                if cmns and k < min_dist:
                    min_dist = k
                    printLog("%d手以下確定" % (k + self.snd_max))
                cmns_dic[k] += cmns
        # 全共通部分を取得後, 浅い要素から確認
        for i in range(tnd):
            cmns = cmns_dic[i]
            if cmns:
                self.common_states = set(cmns)
                self.dist = self.snd_max + i
                self.target_neighbors_depth = i
                printLog(cmns)
                printLog(self.dist)
                return self.dist
        del cmns_dic
        printLog("経過時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
        # ターゲット最深探索
        printLog("%d手を探索" % (self.snd_max + tnd))
        count = 0
        nsts = []
        count_max = len(self.target_neighbors[tnd - 1])
        for st_num in self.target_neighbors[tnd - 1]:
            nsts += applyAllMovesNormal(st_num)
            count += 1
            if (count % self.SUBSET_MAX) == 0 or count == count_max:
                # 集合変換
                nsts = set(nsts)
                # 全最深ファイルを確認
                for i in range(snd_max_sub + 1):
                    fnamer = SN_PATH_FORMAT.format(self.snd_max, i)
                    with open(fnamer, "rb") as f:
                        known_states = pickle.load(f)
                    cmns = known_states & nsts
                    if cmns:
                        self.common_states = cmns
                        self.common_sub = i
                        self.dist = self.snd_max + tnd
                        self.target_neighbors_depth = tnd
                        printLog(cmns)
                        printLog(self.dist)
                        return self.dist
                printLog("%d / %d 探索済み" % (count, count_max))
                printLog("経過時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
                # 初期化
                nsts = []
        printLog(nsts)
        return -1
    
    def calcTargetNeighbors(self, depth: int):
        """
        解きたい状態の近所を探索する.
        """
        for _ in range(depth):
            self._calcNeighbors(self.target_neighbors)

    def _calcNeighbors(self, neighbor_dic: dict):
        """
        メインの探索
        """
        depth = max(neighbor_dic)
        printLog("深さ%dの探索" % (depth + 1))
        nsts = []
        for st_num in neighbor_dic[depth]:
            nsts += applyAllMovesNormal(st_num)
        # printLog("新状態数（重複あり）: %d" % len(nsts))
        nsts = set(nsts)
        for past_sts in neighbor_dic.values():
            nsts -= past_sts
        printLog("新状態数（重複なし）：%d" % len(nsts))
        neighbor_dic[depth + 1] = nsts
    
    def getRoute(self):
        """
        完成までの状態遷移を返す.
        """
        return self.route
    
    def getSolveMoves(self):
        """
        手数が分かっている前提で, 解く手順を返す.
        双方向探索前提.
        """
        cmnst = list(self.common_states)
        # まずは辿る状態を求める
        solved_route = [cmnst[0]]
        target_route = [cmnst[0]]
        for i in range(self.solved_neighbors_depth):
            nsts = set(applyAllMovesNormal(solved_route[i]))
            nsts &= self.solved_neighbors[self.solved_neighbors_depth - (i + 1)]
            solved_route.append(list(nsts)[0])
        for i in range(self.target_neighbors_depth):
            nsts = set(applyAllMovesNormal(target_route[i]))
            nsts &= self.target_neighbors[self.target_neighbors_depth - (i + 1)]
            target_route.append(list(nsts)[0])
        total_route = [target_route[-(i + 1)] for i in range(len(target_route) - 1)] + solved_route
        tmpst = self.target.copy()
        solve_moves = []
        for i, j in enumerate(total_route):
            if i == 0:
                continue
            nstd = tmpst.applyAllMoves()
            for k, v in nstd.items():
                if v.toNumNormal() == j:
                    solve_moves.append(k)
                    tmpst = v.copy()
                    break
            else:
                printLog("なんかおかしい")
                return []
        return solve_moves
    
    def getSolveMovesWithDatOne(self):
        """
        片方向探索で見つかった場合の手順を求める関数.
        """
        solved_route = [self.target_num]
        for i in range(self.dist):
            nsts = set(applyAllMovesNormal(solved_route[i]))
            for j in range(LOOP_MAX):
                fnamer = SN_PATH_FORMAT.format(self.dist - (i + 1), j)
                if not os.path.exists(fnamer):
                    break
                with open(fnamer, "rb") as f:
                    nsts_cmn = nsts & pickle.load(f)
                if nsts_cmn:
                    break
            solved_route.append(list(nsts_cmn)[0])
        self.route = solved_route
        return self.route2moves(solved_route)
    
    def getSolveMovesWithDat(self):
        """
        手数が分かっている前提で, 解く手順を返す.
        ファイルを用いる.
        """
        # 片方向で見つかった場合
        if self.dist <= self.snd_max:
            return self.getSolveMovesWithDatOne()
        cmnst = list(self.common_states)
        # まずは辿る状態を求める
        solved_route = [cmnst[0]]
        target_route = [cmnst[0]]
        for i in range(self.snd_max):
            nsts = set(applyAllMovesNormal(solved_route[i]))
            for j in range(LOOP_MAX):
                fnamer = SN_PATH_FORMAT.format(self.snd_max - (i + 1), j)
                if not os.path.exists(fnamer):
                    break
                # printLog(fnamer)
                with open(fnamer, "rb") as f:
                    nsts_cmn = nsts & pickle.load(f)
                if nsts_cmn:
                    break
            solved_route.append(list(nsts_cmn)[0])
        for i in range(self.target_neighbors_depth):
            nsts = set(applyAllMovesNormal(target_route[i]))
            nsts &= self.target_neighbors[self.target_neighbors_depth - (i + 1)]
            target_route.append(list(nsts)[0])
        total_route = [target_route[-(i + 1)] for i in range(len(target_route) - 1)] + solved_route
        self.route = total_route
        return self.route2moves(total_route)
    
    def route2moves(self, route: list):
        """
        状態のリストから動作のリストを計算
        """
        tmpst = self.target.copy()
        solve_moves = []
        for i, j in enumerate(route):
            if i == 0:
                continue
            nstd = tmpst.applyAllMoves()
            for k, v in nstd.items():
                if v.toNumNormal() == j:
                    solve_moves.append(k)
                    tmpst = v.copy()
                    break
            else:
                printLog("なんかおかしい")
                return []
        return solve_moves

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

def inputState():
    """
    標準入力から状態を受け取る.
    """
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

def createSolvedNeighborsFile():
    """
    完成状態近傍ファイルを作成する関数.
    """
    t0 = time.time()
    searching = DIR_PATH + "searching.json"
    act_num = 0
    sub_num = 0

    if not os.path.isdir(DIR_PATH):
        os.mkdir(DIR_PATH)
        printLog("ディレクトリ%sを作成" % DIR_PATH)
    # まだ何も作られていない
    # 最初のファイルを作成し, 深さ1の探索も行う
    if not os.path.exists(searching):
        fnamew = SN_PATH_FORMAT.format(0, 0)
        with open(fnamew, "wb") as f:
            # 多分無意味だが一応正規化
            st_num = solved.toNumNormal()
            # 要素が1つだけの集合をファイルに書き込む
            pickle.dump(set([st_num]), f)
        fnamer = fnamew
    # ファイルが存在する
    else:
        # 探索済みファイルを読み出し
        with open(searching, "r") as f:
            act_num, sub_num = json.load(f)

        # 副番号をインクリメントしてファイルの存在を確認
        sub_num += 1
        fnamer = SN_PATH_FORMAT.format(act_num, sub_num)
        # 存在しない (この深さの盤面はすべて探索済み)
        if not os.path.exists(fnamer):
            # 次の深さの最初のファイルを指定
            act_num += 1
            # 探索8手までで終了させる
            if act_num > 8:
                printLog("全9手状態を発見")
                return True
            # 副番号はリセット
            sub_num = 0
            fnamer = SN_PATH_FORMAT.format(act_num, sub_num)

    printLog(fnamer, "から次の状態を計算")
    # ロード
    with open(fnamer, "rb") as f:
        prev_st_nums = pickle.load(f)
    printLog("探索状態数：{:d}".format(len(prev_st_nums)))

    # 次の状態を計算
    next_st_nums = []
    while prev_st_nums:
        st_num = prev_st_nums.pop()
        next_st_nums += applyAllMovesNormal(st_num)

    # 探索情報を更新
    with open(searching, "w") as f:
        json.dump([act_num, sub_num], f)

    printLog("新状態数 (重複排除前)：{:d}".format(len(next_st_nums)))

    # 集合に変換
    next_st_nums = set(next_st_nums)
    # なんとなく初期化
    known_st_nums = set()
    latest_act_num = 0
    latest_sub_num = 0

    # 探索済み状態との重複を削除
    for i in range(act_num + 2):
        j = 0
        past_fname = SN_PATH_FORMAT.format(i, j)
        while os.path.exists(past_fname):
            with open(past_fname, "rb") as f:
                # ループ終了時, 最新ファイルの状態が格納される
                known_st_nums = pickle.load(f)
            next_st_nums -= known_st_nums
            # 最新ファイル名更新
            latest_fname = past_fname
            latest_act_num = i
            latest_sub_num = j
            j += 1
            past_fname = SN_PATH_FORMAT.format(i, j)
    
    # リストに変換
    next_st_nums = list(next_st_nums)
    printLog("新状態数 (重複排除後)：{:d}".format(len(next_st_nums)))

    # 全探索終了 (ルービックキューブでは無理)
    if not next_st_nums:
        return True

    # 深さ更新
    if latest_act_num == act_num:
        latest_act_num += 1
        latest_sub_num = 0
        latest_fname = SN_PATH_FORMAT.format(latest_act_num, latest_sub_num)
    # 更新しない場合, 最新ファイルの状態と足す
    else:
        next_st_nums = list(known_st_nums) + next_st_nums

    # 分割してファイルに保存
    while len(next_st_nums) > ST_LEN_MAX:
        with open(latest_fname, "wb") as f:
            pickle.dump(set(next_st_nums[:ST_LEN_MAX]), f)
        # 分割した残り
        next_st_nums = next_st_nums[ST_LEN_MAX:]
        # 最新番号の更新
        latest_sub_num += 1
        latest_fname = SN_PATH_FORMAT.format(latest_act_num, latest_sub_num)
    if next_st_nums:
        with open(latest_fname, "wb") as f:
            pickle.dump(set(next_st_nums), f)
    printLog("%02d:%02d:%02d" % s2hms(time.time() - t0))
    return False

def set2nparray(num_set):
    """
    数値の集合をnumpy配列に変換する
    """
    ll = []
    for num in num_set:
        st = num2state(num)
        ll.append(st.cp + st.co + st.ep + st.eo)
    return np.array(ll, dtype="uint8")

# バックアップして書き込み
# .pickle のみ対応
def writeAndBackup(fnamew, obj):
    # バックアップ
    if os.path.exists(fnamew):
        m = re.match(r"(.*)(\.pickle)", fnamew)
        fnamew_bu = m.groups()[0] + "_backup.pickle"
        shutil.copyfile(fnamew, fnamew_bu)
    
    # 書き込み
    with open(fnamew, "wb") as f:
        pickle.dump(obj, f)

def collectSamples(loop, tnd, mode=0, shuffle_num=20):
    """
    サンプル収集用関数.
    """
    t0 = time.time()
    dist_max = SOLVED_NEIGHBOR_DEPTH_MAX + tnd
    fnamew = SMP_PATH_FORMAT.format(dist_max)
    gt_key = "gt%d" % dist_max
    # パスが存在しない場合は初期化
    if not os.path.exists(fnamew):
        if not os.path.isdir(SMP_DIR_PATH):
            os.mkdir(SMP_DIR_PATH)
            printLog("ディレクトリ%sを作成" % SMP_DIR_PATH)
        smp_dic = {dist_max - i: set() for i in range(tnd)}
        smp_dic[gt_key] = set()
        printLog(fnamew + "を作成")
        writeAndBackup(fnamew, smp_dic)
    with open(fnamew, "rb") as f:
        smp_dic = pickle.load(f)
    # 最初のサンプル数も保存
    len_dic = {}
    printLog("過去のサンプル数")
    for k, v in smp_dic.items():
        len_dic[k] = len(v)
        if type(k) is int:
            printLog("%2d手サンプル数：%d" % (k, len_dic[k]))
        else:
            printLog("%2d手以上サンプル数：%d" % (dist_max + 1, len_dic[k]))
    try:
        for i in range(loop):
            printLog(f"{i + 1}ループ目")
            if mode == 0:
                printLog("通常スクランブル%d手：" % shuffle_num, end="")
                sst = randomScramble(shuffle_num)
            elif mode == 1:
                printLog("冗長排除スクランブル%d手：" % shuffle_num, end="")
                sst = randomScrambleDependent(shuffle_num)
            else:
                printLog("手入力")
                sst = inputState()
                if sst is None:
                    break
            printLog(sst)
            srch = Search(sst, SOLVED_NEIGHBOR_DEPTH_MAX)
            # dist = srch.searchWithDat(tnd)
            dist = srch.searchWithDat2(tnd)
            if dist >= 0:
                printLog("最短%2d手：" % dist, end="")
                mvs = srch.getSolveMovesWithDat()
                for mv in mvs:
                    printLog(mv, end=" ")
                printLog()
                route = srch.getRoute()
                for j in range(dist - SOLVED_NEIGHBOR_DEPTH_MAX):
                    smp_dic[dist - j].add(route[j])
            else:
                printLog("%2d手以上" % (dist_max + 1))
                smp_dic[gt_key].add(sst.toNumNormal())
            for k, v in smp_dic.items():
                smp_len = len(v)
                smp_inc = smp_len - len_dic[k]
                if type(k) is int:
                    printLog("%2d手サンプル数：%d (+%d)" % (k, smp_len, smp_inc))
                else:
                    printLog("%2d手以上サンプル数：%d (+%d)" % (dist_max + 1, smp_len, smp_inc))
            writeAndBackup(fnamew, smp_dic)
            printLog("経過時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
    except KeyboardInterrupt:
        printLog("強制終了")
    printLog("総計算時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
    

# scramble = "L D2 R U2 L F2 U2 L F2 R2 B2 R U' R' U2 F2 R' D B' F2"
# scramble = scramble.split()

# scramble_udm = "L' U2 R' D2 L' F2 D2 L' F2 R2 B2 R' D R D2 F2 R U' B F2"
# scramble_udm = scramble_udm.split()

# Cで格納するための順番
# cl_list = [
#     "UL", "UR", "UB", "DF", "DL", "DR", "DB",
#     "LU", "LD", "LF", "LB", "RU", "RD", "RF", "RB",
#     "FU", "FD", "FL", "FR", "BU", "BD", "BL", "BR"
# ]

def createSampleNpFiles(dist_max):
    """
    サンプル辞書からnp配列ファイルを作る.
    キーの数だけ作る.
    """
    smp_np_path_format = "./np_dat/sample{:03d}_{:03d}.npy".format
    fnamer = SMP_PATH_FORMAT.format(dist_max)
    if not os.path.exists(fnamer):
        return
    with open(fnamer, "rb") as f:
        smp_dic = pickle.load(f)
    for k, v in smp_dic.items():
        arr = set2nparray(v)
        if type(k) is int:
            fnamew = smp_np_path_format(dist_max, k)
        else:
            fnamew = "./np_dat/sample{:03d}_{:03d}ijou.npy".format(dist_max, dist_max + 1)
        printLog(k, arr.shape)
        np.save(fnamew, arr)

def main():
    if LOG_PATH is not None:
        if not os.path.exists(LOG_PATH):
            try:
                with open(LOG_PATH, "w") as f:
                    print(f"「{LOG_PATH}」を作成.")
            except FileNotFoundError:
                print(f"「{LOG_PATH}」の作成失敗.")
                return
    collectSamples(1000, 7, 0, 100)

if __name__ == "__main__":
    main()
    pass

