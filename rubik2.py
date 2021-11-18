import time
import datetime
import random

# 完成した盤面
# 日本配色で白, 赤, 黄, 橙, 緑, 青の順
# 中央の情報は含まない
# 白 -> 0, 赤 -> 1, 黄 -> 2, 橙 -> 3, 緑 -> 4, 青 -> 5
COMPLETE = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5, 5]
]

# 白の完全一面
COMP_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 7, 7, 7, 7, 7],
    [2, 2, 2, 7, 7, 7, 7, 7],
    [3, 3, 3, 7, 7, 7, 7, 7],
    [4, 4, 4, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7]
]

# 白の完全一面と中間層全て
COMP_0_MID = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 7],
    [2, 2, 2, 2, 2, 7, 7, 7],
    [3, 3, 3, 3, 3, 7, 7, 7],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7]
]

# 白の十字
CROSS_0 = [
    [7, 0, 7, 0, 0, 7, 0, 7],
    [7, 1, 7, 7, 7, 7, 7, 7],
    [7, 2, 7, 7, 7, 7, 7, 7],
    [7, 3, 7, 7, 7, 7, 7, 7],
    [7, 4, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7]
]

# 白の十字と一つのコーナー
CROSS_0_CORNER = [
    [7, 0, 7, 0, 0, 7, 0, 0],
    [7, 1, 1, 7, 7, 7, 7, 7],
    [2, 2, 7, 7, 7, 7, 7, 7],
    [7, 3, 7, 7, 7, 7, 7, 7],
    [7, 4, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7]
]

# 白の十字と, 赤黄の上・中層が揃う
CROSS_0_MID_12 = [
    [7, 0, 7, 0, 0, 7, 0, 0],
    [7, 1, 1, 7, 1, 7, 7, 7],
    [2, 2, 7, 2, 7, 7, 7, 7],
    [7, 3, 7, 7, 7, 7, 7, 7],
    [7, 4, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7]
]

# 上の棒
# 青の棒が揃っている
BAR_TOP = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 7],
    [2, 2, 2, 2, 2, 7, 7, 7],
    [3, 3, 3, 3, 3, 7, 7, 7],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [7, 5, 7, 7, 7, 7, 5, 7]
]

# 白を基準に中間層が揃っている
# かつ, 青の十字が揃っている
CROSS_TOP = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 7],
    [2, 2, 2, 2, 2, 7, 7, 7],
    [3, 3, 3, 3, 3, 7, 7, 7],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [7, 5, 7, 5, 5, 7, 5, 7]
]

# パターンC
PATTERN_C_12 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 5],
    [2, 2, 2, 2, 2, 7, 7, 7],
    [3, 3, 3, 3, 3, 7, 7, 5],
    [4, 4, 4, 4, 4, 7, 7, 5],
    [7, 5, 7, 5, 5, 7, 5, 5]
]

# パターンC'
PATTERN_C_DASH_12 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 5, 7, 7],
    [2, 2, 2, 2, 2, 5, 7, 7],
    [3, 3, 3, 3, 3, 5, 7, 7],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [7, 5, 7, 5, 5, 5, 5, 7]
]

# パターンD
PATTREN_D_12 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 5],
    [2, 2, 2, 2, 2, 7, 7, 7],
    [3, 3, 3, 3, 3, 5, 7, 7],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [5, 5, 7, 5, 5, 5, 5, 7]
]

# パターンE
PATTERN_E_12 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 7],
    [2, 2, 2, 2, 2, 5, 7, 7],
    [3, 3, 3, 3, 3, 7, 7, 5],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [5, 5, 7, 5, 5, 7, 5, 5]
]

# 白を基準に中間層が揃っている
# かつ, 青の一面が揃っている
# 現状使う機会はなさそう
COMP_TOP = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 7, 7, 7],
    [2, 2, 2, 2, 2, 7, 7, 7],
    [3, 3, 3, 3, 3, 7, 7, 7],
    [4, 4, 4, 4, 4, 7, 7, 7],
    [5, 5, 5, 5, 5, 5, 5, 5]
]

ACTIONS_C_LIST = [1, 9, 0, 9, 1, 9, 9, 0]

ACTIONS_C_DASH_LIST = [3, 8, 2, 8, 3, 8, 8, 2]

ACTIONS_D_LIST = [1, 9, 0, 8, 3, 9, 1, 8, 0, 2]

ACTIONS_E_LIST = [1, 3, 8, 2, 9, 0, 8, 3, 9, 2]

# デバッグ用サンプル状態

# SAMPLE01 = [
#     [5, 4, 3, 1, 4, 4, 4, 3],
#     [1, 1, 5, 5, 5, 0, 0, 2],
#     [4, 3, 2, 4, 1, 1, 5, 0],
#     [5, 0, 2, 2, 5, 1, 2, 0],
#     [1, 0, 5, 2, 1, 3, 0, 3],
#     [4, 2, 0, 3, 3, 2, 3, 4]
# ]

# SAMPLE01 = [
#     [2, 4, 0, 2, 0, 4, 0, 5],
#     [5, 3, 1, 1, 3, 3, 5, 4],
#     [4, 1, 1, 2, 4, 0, 2, 2],
#     [2, 0, 5, 5, 1, 5, 5, 2],
#     [3, 0, 3, 4, 5, 0, 3, 4],
#     [0, 2, 1, 4, 1, 3, 3, 1]
# ]

# SAMPLE01 = [
#     [5, 5, 3, 4, 0, 4, 4, 4],
#     [3, 3, 5, 2, 5, 3, 4, 0],
#     [1, 3, 2, 1, 0, 2, 2, 0],
#     [5, 3, 2, 2, 1, 1, 3, 0],
#     [1, 0, 0, 0, 5, 3, 4, 5],
#     [4, 1, 1, 5, 1, 2, 2, 4]
# ]

SAMPLE01 = [
    [4, 1, 0, 0, 4, 4, 5, 2],
    [1, 4, 3, 0, 5, 1, 1, 0],
    [0, 1, 3, 3, 1, 2, 0, 3],
    [4, 2, 1, 5, 2, 4, 2, 2],
    [0, 4, 5, 5, 3, 3, 3, 5],
    [2, 0, 1, 4, 2, 5, 3, 5]
]

# 黄色の完全一面から6手動かした盤面
SAMPLE02 = [
    [3, 5, 5, 3, 2, 1, 5, 1],
    [5, 1, 2, 4, 2, 4, 1, 0],
    [0, 3, 2, 0, 3, 4, 1, 3],
    [1, 2, 0, 4, 5, 5, 0, 4],
    [2, 5, 4, 4, 0, 0, 1, 3],
    [5, 0, 3, 4, 2, 1, 3, 2]
]

# 赤の十字
SAMPLE_RED_CROSS = 0x22c5282245607230e8ac34ab66134a40ba52

# 白の一面と中間層
SAMPLE_WHITE_SIDE_MID = 0x4ed36a76492474b6dbb0a4928a9249000000

# ほぼ最終局面
SAMPLE_FINAL_01 = 0x74daad8ec92446b6db8aa492709249000000

JPN_COLOR = ["白", "赤", "黄", "橙", "緑", "青", "黒", "ー"]

DIC_0TO1 = {0: 1, 1: 5, 5: 3, 3: 0, 2: 2, 4: 4, 7: 7}

DIC_1TO2 = {1: 2, 2: 3, 3: 4, 4: 1, 0: 0, 5: 5, 7: 7}

DIC_ROT_R = {0: 2, 2: 7, 7: 5, 5: 0, 1: 4, 4: 6, 6: 3, 3: 1}

# ある色を上にして正面になる色
DIC_FRONT_COLOR = {0: 1, 1: 5, 2: 5, 3: 5, 4: 5, 5: 3}

# 操作の変換
# 赤正面 -> 黄色正面
# Z軸回りの動作は等価
ACT_DIC_0TO7 = {0: 7, 7: 3, 3: 4, 4: 0, 1: 6, 6: 2, 2: 5, 5: 1, 8: 8, 9: 9, 10: 10, 11: 11}

ACT_DIC_4TO8 = {4: 8, 8: 7, 7: 11, 11: 4, 5: 9, 9: 6, 6: 10, 10: 5, 0: 0, 1: 1, 2: 2, 3: 3}

# ACT_STR = ["lp", "lm", "rp", "rm", "bp", "bm", "fp", "fm", "up", "um", "dp", "dm"]
# ACT_STR = ["L", "L'", "R'", "R", "B", "B'", "F'", "F", "U", "U'", "D'", "D"]
ACT_STR = ["L", "-L", "-R", "R", "B", "-B", "-F", "F", "U", "-U", "-D", "D"]

ACT_PATTERN_STR = ["C", "C'", "D", "E"]

CORNERS = [0, 2, 5, 7]

# 真逆の色
INV_COLOR = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

# 色番号と頭文字
COLOR_INITIAL = {"w": 0, "r": 1, "y": 2, "o": 3, "g": 4, "b": 5}

# 数値を2次元リストに戻す
# メソッドでなく関数として定義
def num2cube(num):
    cube = [[] for _ in range(6)]
    for i in range(6):
        for j in range(8):
            cube[i].append(num & 0b111)
            num >>= 3
    return cube

# 手順を出力
def printActs(acts):
    moji = "\n"
    im = len(acts) - 1
    for i, act in enumerate(acts):
        moji += ACT_STR[act]
        if i < im:
            moji += ", "
    print(moji)

# C, C', D, Eなどを動作のリストに変換
# 動作は数値のまま
def procedure2actions(p: str):
    sub = int(p[-1])
    act = []
    if p[0] == "C":
        if p[1] == "'":
            act = ACTIONS_C_DASH_LIST_LIST[sub]
        else:
            act = ACTIONS_C_LIST_LIST[sub]
    elif p[0] == "D":
        act = ACTIONS_D_LIST_LIST[sub]
    elif p[0] == "E":
        act = ACTIONS_E_LIST_LIST[sub]
    return tuple(act)

# 赤 -> 黄 -> 橙 -> 緑 -> 赤
def switch0to7Acts(a_list):
    return [ACT_DIC_0TO7[a] for a in a_list]

# 白 -> 赤 -> 青 -> 橙 -> 白
def swith4to8Acts(a_list):
    return [ACT_DIC_4TO8[a] for a in a_list]

class Rubik:

    def __init__(self, cube=COMPLETE):
        # 値渡し
        self.cube = self._cubeCopy(cube)
        # インスタンス作成と同時に数値変換も行う
        self.num = self._cube2num(self.cube)
        # 動作のリストを作成
        # 格納した添え字を各操作の番号とする
        self.acts_list = [
            self.leftRollPlus, self.leftRollMinus,
            self.rightRollPlus, self.rightRollMinus,
            self.backPitchPlus, self.backPitchMinus,
            self.frontPitchPlus, self.frontPitchMinus,
            self.upYawPlus, self.upYawMinus,
            self.downYawPlus, self.downYawMinus
        ]
    
    # インスタンスのコピー
    # 恒等写像 (何も操作しない) とみなせるかも
    def copy(self):
        return Rubik(self.cube)
    
    # キューブのコピー
    def _cubeCopy(self, cube):
        return [i.copy() for i in cube]
    
    # 右ロール回転 (正)
    def _rightRollPlus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][2] = cube[3][5]
        n_cube[3][5] = cube[5][2]
        n_cube[5][2] = cube[1][2]
        n_cube[1][2] = cube[0][2]
        n_cube[0][4] = cube[3][3]
        n_cube[3][3] = cube[5][4]
        n_cube[5][4] = cube[1][4]
        n_cube[1][4] = cube[0][4]
        n_cube[0][7] = cube[3][0]
        n_cube[3][0] = cube[5][7]
        n_cube[5][7] = cube[1][7]
        n_cube[1][7] = cube[0][7]
        n_cube[2][0] = cube[2][2]
        n_cube[2][2] = cube[2][7]
        n_cube[2][7] = cube[2][5]
        n_cube[2][5] = cube[2][0]
        n_cube[2][1] = cube[2][4]
        n_cube[2][4] = cube[2][6]
        n_cube[2][6] = cube[2][3]
        n_cube[2][3] = cube[2][1]
        return Rubik(n_cube)
    
    # 右ロール回転 (負)
    def _rightRollMinus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][2] = cube[1][2]
        n_cube[1][2] = cube[5][2]
        n_cube[5][2] = cube[3][5]
        n_cube[3][5] = cube[0][2]
        n_cube[0][4] = cube[1][4]
        n_cube[1][4] = cube[5][4]
        n_cube[5][4] = cube[3][3]
        n_cube[3][3] = cube[0][4]
        n_cube[0][7] = cube[1][7]
        n_cube[1][7] = cube[5][7]
        n_cube[5][7] = cube[3][0]
        n_cube[3][0] = cube[0][7]
        n_cube[2][0] = cube[2][5]
        n_cube[2][5] = cube[2][7]
        n_cube[2][7] = cube[2][2]
        n_cube[2][2] = cube[2][0]
        n_cube[2][1] = cube[2][3]
        n_cube[2][3] = cube[2][6]
        n_cube[2][6] = cube[2][4]
        n_cube[2][4] = cube[2][1]
        return Rubik(n_cube)
    
    # 左ロール回転 (正)
    def _leftRollPlus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][0] = cube[3][7]
        n_cube[3][7] = cube[5][0]
        n_cube[5][0] = cube[1][0]
        n_cube[1][0] = cube[0][0]
        n_cube[0][3] = cube[3][4]
        n_cube[3][4] = cube[5][3]
        n_cube[5][3] = cube[1][3]
        n_cube[1][3] = cube[0][3]
        n_cube[0][5] = cube[3][2]
        n_cube[3][2] = cube[5][5]
        n_cube[5][5] = cube[1][5]
        n_cube[1][5] = cube[0][5]
        n_cube[4][0] = cube[4][5]
        n_cube[4][5] = cube[4][7]
        n_cube[4][7] = cube[4][2]
        n_cube[4][2] = cube[4][0]
        n_cube[4][1] = cube[4][3]
        n_cube[4][3] = cube[4][6]
        n_cube[4][6] = cube[4][4]
        n_cube[4][4] = cube[4][1]
        return Rubik(n_cube)
    
    # 左ロール回転 (負)
    def _leftRollMinus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][0] = cube[1][0]
        n_cube[1][0] = cube[5][0]
        n_cube[5][0] = cube[3][7]
        n_cube[3][7] = cube[0][0]
        n_cube[0][3] = cube[1][3]
        n_cube[1][3] = cube[5][3]
        n_cube[5][3] = cube[3][4]
        n_cube[3][4] = cube[0][3]
        n_cube[0][5] = cube[1][5]
        n_cube[1][5] = cube[5][5]
        n_cube[5][5] = cube[3][2]
        n_cube[3][2] = cube[0][5]
        n_cube[4][0] = cube[4][2]
        n_cube[4][2] = cube[4][7]
        n_cube[4][7] = cube[4][5]
        n_cube[4][5] = cube[4][0]
        n_cube[4][1] = cube[4][4]
        n_cube[4][4] = cube[4][6]
        n_cube[4][6] = cube[4][3]
        n_cube[4][3] = cube[4][1]
        return Rubik(n_cube)
    
    # 奥ピッチ回転 (正)
    def _backPitchPlus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][0] = cube[2][2]
        n_cube[2][2] = cube[5][7]
        n_cube[5][7] = cube[4][5]
        n_cube[4][5] = cube[0][0]
        n_cube[0][1] = cube[2][4]
        n_cube[2][4] = cube[5][6]
        n_cube[5][6] = cube[4][3]
        n_cube[4][3] = cube[0][1]
        n_cube[0][2] = cube[2][7]
        n_cube[2][7] = cube[5][5]
        n_cube[5][5] = cube[4][0]
        n_cube[4][0] = cube[0][2]
        n_cube[3][0] = cube[3][5]
        n_cube[3][5] = cube[3][7]
        n_cube[3][7] = cube[3][2]
        n_cube[3][2] = cube[3][0]
        n_cube[3][1] = cube[3][3]
        n_cube[3][3] = cube[3][6]
        n_cube[3][6] = cube[3][4]
        n_cube[3][4] = cube[3][1]
        return Rubik(n_cube)
    
    # 奥ピッチ回転 (負)
    def _backPitchMinus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][0] = cube[4][5]
        n_cube[4][5] = cube[5][7]
        n_cube[5][7] = cube[2][2]
        n_cube[2][2] = cube[0][0]
        n_cube[0][1] = cube[4][3]
        n_cube[4][3] = cube[5][6]
        n_cube[5][6] = cube[2][4]
        n_cube[2][4] = cube[0][1]
        n_cube[0][2] = cube[4][0]
        n_cube[4][0] = cube[5][5]
        n_cube[5][5] = cube[2][7]
        n_cube[2][7] = cube[0][2]
        n_cube[3][0] = cube[3][2]
        n_cube[3][2] = cube[3][7]
        n_cube[3][7] = cube[3][5]
        n_cube[3][5] = cube[3][0]
        n_cube[3][1] = cube[3][4]
        n_cube[3][4] = cube[3][6]
        n_cube[3][6] = cube[3][3]
        n_cube[3][3] = cube[3][1]
        return Rubik(n_cube)
    
    # 手前ピッチ回転 (正)
    def _frontPitchPlus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][5] = cube[2][0]
        n_cube[2][0] = cube[5][2]
        n_cube[5][2] = cube[4][7]
        n_cube[4][7] = cube[0][5]
        n_cube[0][6] = cube[2][3]
        n_cube[2][3] = cube[5][1]
        n_cube[5][1] = cube[4][4]
        n_cube[4][4] = cube[0][6]
        n_cube[0][7] = cube[2][5]
        n_cube[2][5] = cube[5][0]
        n_cube[5][0] = cube[4][2]
        n_cube[4][2] = cube[0][7]
        n_cube[1][0] = cube[1][2]
        n_cube[1][2] = cube[1][7]
        n_cube[1][7] = cube[1][5]
        n_cube[1][5] = cube[1][0]
        n_cube[1][1] = cube[1][4]
        n_cube[1][4] = cube[1][6]
        n_cube[1][6] = cube[1][3]
        n_cube[1][3] = cube[1][1]
        return Rubik(n_cube)
    
    # 手前ピッチ回転 (負)
    def _frontPitchMinus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][5] = cube[4][7]
        n_cube[4][7] = cube[5][2]
        n_cube[5][2] = cube[2][0]
        n_cube[2][0] = cube[0][5]
        n_cube[0][6] = cube[4][4]
        n_cube[4][4] = cube[5][1]
        n_cube[5][1] = cube[2][3]
        n_cube[2][3] = cube[0][6]
        n_cube[0][7] = cube[4][2]
        n_cube[4][2] = cube[5][0]
        n_cube[5][0] = cube[2][5]
        n_cube[2][5] = cube[0][7]
        n_cube[1][0] = cube[1][5]
        n_cube[1][5] = cube[1][7]
        n_cube[1][7] = cube[1][2]
        n_cube[1][2] = cube[1][0]
        n_cube[1][1] = cube[1][3]
        n_cube[1][3] = cube[1][6]
        n_cube[1][6] = cube[1][4]
        n_cube[1][4] = cube[1][1]
        return Rubik(n_cube)
    
    # 上ヨー回転 (正)
    def _upYawPlus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][0] = cube[0][5]
        n_cube[0][5] = cube[0][7]
        n_cube[0][7] = cube[0][2]
        n_cube[0][2] = cube[0][0]
        n_cube[0][1] = cube[0][3]
        n_cube[0][3] = cube[0][6]
        n_cube[0][6] = cube[0][4]
        n_cube[0][4] = cube[0][1]
        n_cube[1][:3] = cube[2][:3]
        n_cube[2][:3] = cube[3][:3]
        n_cube[3][:3] = cube[4][:3]
        n_cube[4][:3] = cube[1][:3]
        return Rubik(n_cube)
    
    # 上ヨー回転 (負)
    def _upYawMinus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[0][0] = cube[0][2]
        n_cube[0][2] = cube[0][7]
        n_cube[0][7] = cube[0][5]
        n_cube[0][5] = cube[0][0]
        n_cube[0][1] = cube[0][4]
        n_cube[0][4] = cube[0][6]
        n_cube[0][6] = cube[0][3]
        n_cube[0][3] = cube[0][1]
        n_cube[1][:3] = cube[4][:3]
        n_cube[4][:3] = cube[3][:3]
        n_cube[3][:3] = cube[2][:3]
        n_cube[2][:3] = cube[1][:3]
        return Rubik(n_cube)
    
    # 下ヨー回転 (正)
    def _downYawPlus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[1][5:] = cube[2][5:]
        n_cube[2][5:] = cube[3][5:]
        n_cube[3][5:] = cube[4][5:]
        n_cube[4][5:] = cube[1][5:]
        n_cube[5][0] = cube[5][2]
        n_cube[5][2] = cube[5][7]
        n_cube[5][7] = cube[5][5]
        n_cube[5][5] = cube[5][0]
        n_cube[5][1] = cube[5][4]
        n_cube[5][4] = cube[5][6]
        n_cube[5][6] = cube[5][3]
        n_cube[5][3] = cube[5][1]
        return Rubik(n_cube)
    
    # 下ヨー回転 (負)
    def _downYawMinus(self, cube):
        n_cube = self._cubeCopy(cube)
        n_cube[1][5:] = cube[4][5:]
        n_cube[4][5:] = cube[3][5:]
        n_cube[3][5:] = cube[2][5:]
        n_cube[2][5:] = cube[1][5:]
        n_cube[5][0] = cube[5][5]
        n_cube[5][5] = cube[5][7]
        n_cube[5][7] = cube[5][2]
        n_cube[5][2] = cube[5][0]
        n_cube[5][1] = cube[5][3]
        n_cube[5][3] = cube[5][6]
        n_cube[5][6] = cube[5][4]
        n_cube[5][4] = cube[5][1]
        return Rubik(n_cube)

    def rightRollPlus(self):
        return self._rightRollPlus(self.cube)
    
    def rightRollMinus(self):
        return self._rightRollMinus(self.cube)
    
    def leftRollPlus(self):
        return self._leftRollPlus(self.cube)
    
    def leftRollMinus(self):
        return self._leftRollMinus(self.cube)

    def backPitchPlus(self):
        return self._backPitchPlus(self.cube)
    
    def backPitchMinus(self):
        return self._backPitchMinus(self.cube)
    
    def frontPitchPlus(self):
        return self._frontPitchPlus(self.cube)
    
    def frontPitchMinus(self):
        return self._frontPitchMinus(self.cube)
    
    def upYawPlus(self):
        return self._upYawPlus(self.cube)
    
    def upYawMinus(self):
        return self._upYawMinus(self.cube)
    
    def downYawPlus(self):
        return self._downYawPlus(self.cube)
    
    def downYawMinus(self):
        return self._downYawMinus(self.cube)
    
    # 12種類の操作を行ったあとのキューブのリスト
    def allActions(self):
        return [i() for i in self.acts_list]
    
    # 指定した添え字の動作を行う
    def anyAction(self, act_num):
        return self.acts_list[act_num]()

    # 複数の動作を行う
    def actionByList(self, a_list):
        r = self.copy()
        for a in a_list:
            r = r.anyAction(a)
        return r

    # 数値変換
    # 若い添え字の値が下位ビットになるように変換
    # 各3bit
    def _cube2num(self, cube):
        num = 0
        sft = 0
        for i in range(6):
            for j in range(8):
                num |= cube[i][j] << sft
                sft += 3
        return num
    
    # 数値を2次元リストに戻す
    def _num2cube(self, num):
        cube = [[] for i in range(6)]
        for i in range(6):
            for j in range(8):
                cube[i].append(num & 0b111)
                num >>= 3
        return cube
    
    # 0と1の色, 位置を切り替え
    # 白 -> 赤 -> 青 -> 橙 -> 白
    # 白の完全一面を基に赤の完全一面を作る
    # 色を切り替えて等価な盤面を作る場合に使える??
    def _switch0to1(self, cube):
        s_cube = [[6] * 8 for _ in range(6)]
        s_cube[1] = [DIC_0TO1[i] for i in cube[0]]
        s_cube[5] = [DIC_0TO1[i] for i in cube[1]]
        for i in range(8):
            s_cube[3][i] = DIC_0TO1[cube[5][7 - i]]
            s_cube[0][i] = DIC_0TO1[cube[3][7 - i]]
        for k, v in DIC_ROT_R.items():
            s_cube[2][k] = DIC_0TO1[cube[2][v]]
            s_cube[4][v] = DIC_0TO1[cube[4][k]]
        return Rubik(s_cube)

    # 1と2の色, 位置を切り替え
    # 赤 -> 黄 -> 橙 -> 緑 -> 赤
    def _switch1to2(self, cube):
        s_cube = [[6] * 8 for _ in range(6)]
        for i in range(1, 5):
            s_cube[DIC_1TO2[i]] = [DIC_1TO2[j] for j in cube[i]]
        for k, v in DIC_ROT_R.items():
            s_cube[0][k] = DIC_1TO2[cube[0][v]]
            s_cube[5][v] = DIC_1TO2[cube[5][k]]
        return Rubik(s_cube)
    
    def switch0to1(self):
        return self._switch0to1(self.cube)
    
    def switch1to2(self):
        return self._switch1to2(self.cube)
    
    # 比較用のマスクを取得 (通常キューブには使わない)
    # 7はそのまま, それ以外は0
    # 比較対象とorを取ることで, don't careの部分は全て1になる
    def getMask(self):
        cube_mask = 0
        sft = 0
        for i in range(6):
            for j in range(8):
                if self.cube[i][j] == 7:
                    cube_mask |= 7 << sft
                sft += 3
        return cube_mask
    
    # 合計をカウント
    def checkSum(self):
        corners_sum = {i: 0 for i in range(8)}
        edges_sum = {i: 0 for i in range(8)}
        for i in range(6):
            for j in range(8):
                if j in CORNERS:
                    corners_sum[self.cube[i][j]] += 1
                else:
                    edges_sum[self.cube[i][j]] += 1
        for i in range(6):
            if corners_sum[i] != 4:
                return False
            if edges_sum[i] != 4:
                return False
        return True
    
    # 等号演算子の処理を定義
    def __eq__(self, target):
        return self.num == target.num
    
    def __str__(self):
        sub1 = 0
        sub2 = 0
        moji = hex(self.num) + "\n"
        for i in range(3):
            if i != 0:
                if i == 1:
                    sub1 = 3
                else:
                    sub1 = 5
            for j in range(6):
                sub2 = sub1
                for k in range(3):
                    if i == 1 and k == 1:
                        moji += JPN_COLOR[j]
                    else:
                        moji += JPN_COLOR[self.cube[j][sub2]]
                        sub2 += 1
                moji += " "
            moji += "\n"
        return moji

# 完成したキューブの数値
COMPLETE_NUM = Rubik().num

class Search:
    
    # 目的とする状態はリストとして与える (複数あること前提)
    # 一手の重みも与える
    # 与えた候補で一致する数も与える??
    # 角を複数揃えたい場合など
    def __init__(self, cube_num, goal=COMPLETE_NUM, act_weight=12, match_num=0):
        self.goal = goal
        # 第二引数は整数型も許容
        if type(goal) is int:
            self.calc_dist_method = lambda rn: self._calcDist(rn, goal)
        # リストならこれまで通り
        elif type(goal) is list:
            self.calc_dist_method = self.calcDistMatchNum
        self.act_weight = act_weight
        # 探索済み
        self.explored = []
        self.match_num = match_num
        # 初期値
        self.init_cube = cube_num
        # 初期値の距離を計算 (不要だがデバッグのため)
        crnt_dist = self.calc_dist_method(cube_num)
        if crnt_dist == 0:
            print("達成済み")
        self.unexplored = {crnt_dist: {cube_num: tuple()}}
        # 幅優先探索で使用
        self.num_dic = {0: {cube_num: tuple()}}
        # 現状, 目的に最も近い (と思われる) 距離
        self.min_dist = crnt_dist
        self.num_known_states = 1
        self.nearest_dist = crnt_dist
        self.nearest_r = Rubik(num2cube(cube_num))
        self.nearest_acts = tuple()
        self.depth = 0
    
    # 距離を使って優先順位を決める
    # とりあえずループ数だけ繰り返す
    def useDist(self, loop):
        if self.min_dist == 0:
            return (self.init_cube, tuple())
        for i in range(loop):
            while not self.unexplored[self.min_dist]:
                self.unexplored.pop(self.min_dist)
                self.min_dist = min(self.unexplored)
            k, v = self.unexplored[self.min_dist].popitem()
            # 次の状態への動作と数値
            nr_act_l = list(enumerate(Rubik(num2cube(k)).allActions()))
            # シャッフル
            random.shuffle(nr_act_l)
            # 新状態を確認
            for j, nr in nr_act_l:
                # 探索済みに含まれていたらやりなおし
                if nr.num in self.explored:
                    continue
                # 未探索に含まれていてもやりなおし
                for known in self.unexplored.values():
                    if nr.num in known:
                        continue
                # 最短距離を計算
                dist = self.calc_dist_method(nr.num)
                # 一致したら終了
                if dist == 0:
                    printActs(v + (j,))
                    print(nr)
                    return (nr.num, v + (j,))
                # これまでの手数を加える
                total_dist = dist + (len(v) + 1) * self.act_weight
                # キーが存在しない場合は追加
                if total_dist not in self.unexplored:
                    # 最短距離の更新
                    if total_dist < self.min_dist:
                        self.min_dist = total_dist
                        # 最も近づいた(?)状態を保存
                        if total_dist < self.nearest_dist:
                            self.nearest_dist = total_dist
                            self.nearest_r = nr
                            self.nearest_acts = v + (j,)
                    self.unexplored[total_dist] = {nr.num: v + (j,)}
                    self.num_known_states += 1
                # 既存のキーなら追加
                else:
                    self.unexplored[total_dist][nr.num] = v + (j,)
                    self.num_known_states += 1
            # 探索済みは数値だけ格納
            self.explored.append(k)
            if i % 1000 == 999:
                print("ループ数：{:d}, 総状態数：{:d}".format(i + 1, self.num_known_states))
        return (-1, tuple())
    
    # 幅優先探索 (全探索)
    def bfs(self):
        nrnd = {}
        for r_num, past_acts in self.num_dic[self.depth].items():
            r = Rubik(num2cube(r_num))
            # シャッフル
            nr_act_l = list(enumerate(r.allActions()))
            random.shuffle(nr_act_l)
            for a, nr in nr_act_l:
                if not self.calc_dist_method(nr.num):
                    printActs(past_acts + (a,))
                    print(nr)
                    return (nr.num, past_acts + (a,))
                nrnd[nr.num] = past_acts + (a,)

        # 重複排除フェーズ
        nrns = set(nrnd)
        for knownd in self.num_dic.values():
            knowns = set(knownd)
            nrns -= knowns
        self.depth += 1
        print("深さ：{:d}, 状態数：{:d}".format(self.depth, len(nrns)))
        self.num_dic[self.depth] = {k: v for k, v in nrnd.items() if k in nrns}
        return (-1, tuple())
    
    # 最終局面の探索
    # C, C', D, Eで幅優先探索
    def bfsFinal(self):
        nrnd = {}
        for r_num, past_acts in self.num_dic[self.depth].items():
            r = Rubik(num2cube(r_num))
            # 動作 C, C', D, E それぞれ4方向, 計16種類
            nrll = [[r.actionByList(al) for al in ACTIONS_C_LIST_LIST]]
            nrll.append([r.actionByList(al) for al in ACTIONS_C_DASH_LIST_LIST])
            nrll.append([r.actionByList(al) for al in ACTIONS_D_LIST_LIST])
            nrll.append([r.actionByList(al) for al in ACTIONS_E_LIST_LIST])
            for i, nrl in enumerate(nrll):
                for j, nr in enumerate(nrl):
                    act_name = ACT_PATTERN_STR[i] + str(j)
                    if not self.calc_dist_method(nr.num):
                        print(past_acts + (act_name,))
                        print(nr)
                        return (nr.num, past_acts + (act_name,))
                    nrnd[nr.num] = past_acts + (act_name,)

        # 重複排除フェーズ
        nrns = set(nrnd)
        for knownd in self.num_dic.values():
            knowns = set(knownd)
            nrns -= knowns
        self.depth += 1
        print("深さ{:d}, 状態数：{:d}".format(self.depth, len(nrns)))
        self.num_dic[self.depth] = {k: v for k, v in nrnd.items() if k in nrns}
        return (-1, tuple())
    
    # 目的とするいくつかの状態から, 最も近い距離を返す
    def calcMinDist(self, cube_num):
        min_dist = 50
        for g in self.goal:
            dist = self._calcDist(cube_num, g)
            if dist < min_dist:
                min_dist = dist
        return min_dist
    
    # 使用する添え字を指定
    # self.match_num == 0 なら calcMinDist と同じ
    def calcDistMatchNum(self, cube_num):
        dists = [self._calcDist(cube_num, g) for g in self.goal]
        dists.sort()
        return dists[self.match_num]
    
    # 色が一致している数を計算
    # 与えるのはキューブの数値
    # don't care を含むキューブは第二引数に与える
    def _calcDist(self, crnt, dest):
        diff = crnt ^ dest
        dist = 0
        for _ in range(48):
            # don't careでなく, 一致しない場合は加算
            if dest & 0b111 != 0b111 and diff & 0b111:
                dist += 1
            diff >>= 3
            dest >>= 3
        return dist

# 白基準のキューブから全ての色の等価なキューブのリストを作成
# ついでにマスクも
def makeAllColorCubeList(white_cube):
    r_list = [Rubik(white_cube)]
    r_list.append(r_list[0].switch0to1())
    for i in range(3):
        r_list.append(r_list[i + 1].switch1to2())
    r_list.append(r_list[1].switch0to1())
    return [r.num for r in r_list], [r.getMask() for r in r_list]

# リストの数値すべての色を変換
def switchColorList(rn_list, color):
    # 白
    if color == 0:
        return rn_list
    r_list = [Rubik(num2cube(rn)).switch0to1() for rn in rn_list]
    # 青
    if color == 5:
        return [r.switch0to1().num for r in r_list]
    # 赤, 黄, 橙, 緑
    for _ in range(color - 1):
        r_list = [r.switch1to2() for r in r_list]
    return [r.num for r in r_list]

# 動作を色によって変更
def switchColorAct(a_list_list, color):
    # 白
    if color == 0:
        return a_list_list
    a_list_list = [swith4to8Acts(a_list) for a_list in a_list_list]
    # 青
    if color == 5:
        return [swith4to8Acts(a_list) for a_list in a_list_list]
    # 赤, 黄, 橙, 緑
    for _ in range(color - 1):
        a_list_list = [switch0to7Acts(a_list) for a_list in a_list_list]
    return a_list_list

def init():
    global COMP_MID_NUMS, COMP_MID_NUM_MASKS
    global COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS
    global CROSS_ONE_SIDE_NUMS, CROSS_ONE_SIDE_NUM_MASKS
    global CROSS_MID_ONE_NUMS, BAR_TOP_NUMS, CROSS_TOP_NUMS, COMP_TOP_NUMS
    global TOP_PATTERN_NUMS, CROSS_CORNER_NUMS
    global ACTIONS_C_LIST_LIST, ACTIONS_C_DASH_LIST_LIST
    global ACTIONS_D_LIST_LIST, ACTIONS_E_LIST_LIST
    global REMAIN_TOP_ROT_LIST
    # 完全一面と中間層
    COMP_MID_NUMS, COMP_MID_NUM_MASKS = makeAllColorCubeList(COMP_0_MID)
    # 完全一面
    COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS = makeAllColorCubeList(COMP_0)
    # 十字
    CROSS_ONE_SIDE_NUMS, CROSS_ONE_SIDE_NUM_MASKS = makeAllColorCubeList(CROSS_0)
    # 十字と一つの角
    r_list = [Rubik(CROSS_0_CORNER)]
    for _ in range(3):
        r_list.append(r_list[-1].switch1to2())
    CROSS_CORNER_NUMS = [r.num for r in r_list]
    # 4種類の側面の辺
    r_list = [Rubik(CROSS_0_MID_12)]
    for _ in range(3):
        r_list.append(r_list[-1].switch1to2())
    CROSS_MID_ONE_NUMS = [r.num for r in r_list]
    # 上の棒
    r_list = [Rubik(BAR_TOP)]
    r_list.append(r_list[0].downYawPlus())
    BAR_TOP_NUMS = [r.num for r in r_list]
    # 基準色の反対側の十字
    # 複数形だが要素は一つ
    CROSS_TOP_NUMS = [Rubik(CROSS_TOP).num]
    COMP_TOP_NUMS = [Rubik(COMP_TOP).num]
    r_list = [Rubik(PATTERN_C_12)]
    for _ in range(3):
        r_list.append(r_list[-1].switch1to2())
    r_list.append(Rubik(PATTERN_C_DASH_12))
    for _ in range(3):
        r_list.append(r_list[-1].switch1to2())
    r_list.append(Rubik(PATTREN_D_12))
    for _ in range(3):
        r_list.append(r_list[-1].switch1to2())
    r_list.append(Rubik(PATTERN_E_12))
    for _ in range(3):
        r_list.append(r_list[-1].switch1to2())
    TOP_PATTERN_NUMS = [r.num for r in r_list]
    # 残りは最後の面の回転だけ (初期値白基準)
    r_list = [Rubik(COMPLETE)]
    for _ in range(3):
        r_list.append(r_list[-1].upYawMinus())
    REMAIN_TOP_ROT_LIST = [r.num for r in r_list]

    # 動作関係
    # C, C', D, E の各方向4パターン (初期値白基準)
    ACTIONS_C_LIST_LIST = [ACTIONS_C_LIST]
    ACTIONS_C_DASH_LIST_LIST = [ACTIONS_C_DASH_LIST]
    ACTIONS_D_LIST_LIST = [ACTIONS_D_LIST]
    ACTIONS_E_LIST_LIST = [ACTIONS_E_LIST]
    for _ in range(3):
        ACTIONS_C_LIST_LIST.append(switch0to7Acts(ACTIONS_C_LIST_LIST[-1]))
        ACTIONS_C_DASH_LIST_LIST.append(switch0to7Acts(ACTIONS_C_DASH_LIST_LIST[-1]))
        ACTIONS_D_LIST_LIST.append(switch0to7Acts(ACTIONS_D_LIST_LIST[-1]))
        ACTIONS_E_LIST_LIST.append(switch0to7Acts(ACTIONS_E_LIST_LIST[-1]))

init()

# 標準入力
def inputCube():
    print("ルービックキューブの状態を入力")
    print("入力する順番は\n1 2 3\n4 5 6\n7 8 9\nです")
    print("色は英語の頭文字で入力してください（色番号も可）")
    print("白:w (0), 赤:r (1), 黄:y (2), 橙:o (3), 緑:g (4), 青:b (5)")
    print("最初からやり直したい場合は \"!\" を入力してください")
    cube = [[6] * 8 for _ in range(6)]
    cont = True
    while cont:
        i = 0
        while i < 6:
            sub = 0
            moji = input("中央が「{:s}」の面を上にし、「{:s}」を正面に持って上の色を入力してください：".format(JPN_COLOR[i], JPN_COLOR[DIC_FRONT_COLOR[i]]))
            moji = moji.lower()
            if not moji:
                break
            if moji[0] == "!":
                break
            if moji[:2] == "0x":
                r_num = int(moji, 0)
                cube = num2cube(r_num)
                i = 6
                break
            if (len(moji) < 9):
                print("文字数が不足しています")
                break
            for j, c in enumerate(moji):
                if j == 4:
                    continue
                if j >= 9:
                    continue
                # 数値でもいい
                if c.isdecimal():
                    cn = int(c)
                    if cn in COLOR_INITIAL.values():
                        cube[i][sub] = cn
                    else:
                        print("無効な入力です")
                        break
                # 頭文字
                elif c in COLOR_INITIAL:
                    cube[i][sub] = COLOR_INITIAL[c]
                else:
                    print("無効な入力です")
                    break
                sub += 1
            else:
                i += 1
        r = Rubik(cube)
        print(r)
        if r.checkSum():
            cont = False
        else:
            print("色の数が間違っています")   
    return Rubik(cube)

# 十字を見つける
def searchCross(r_num):
    # 動作の重みは2
    s = Search(r_num, CROSS_ONE_SIDE_NUMS, 2)
    t1 = time.time()
    nr_num, acts = s.useDist(30000)
    print(time.time() - t1, "秒")
    return nr_num, acts

# 十字と角と対応する中間層を揃える
def searchCrossCornerMid(r_num):
    # 完全一面を揃えつつ中間層も揃える
    i = 0
    compromise = False
    total_acts = tuple()
    while i < 4:
        r_num_cp = r_num
        s = Search(r_num, CROSS_MID_ONE_NUMS, 2, i)
        t1 = time.time()
        r_num, acts = s.useDist(10000)
        total_acts += acts
        print(time.time() - t1, "秒")
        # 妥協して端から揃える
        if r_num < 0:
            # 妥協しても見つからなかった場合
            if compromise:
                t1 = time.time()
                if i == 3:
                    print("中間層ラスト")
                    # 最後の一個はできるだけ効率化
                    s = Search(r_num_cp, COMP_MID_NUMS[STD_COLOR], 1)
                    r_num, acts = s.useDist(100000)
                    total_acts += acts
                else:
                    s = Search(r_num_cp, CROSS_MID_ONE_NUMS, 1, i)
                    r_num, acts = s.useDist(100000)
                    total_acts += acts
                print(time.time() - t1, "秒")
                if r_num < 0:
                    return r_num, acts
            # 最初の妥協
            else:
                compromise = True
                print("妥協")
                s = Search(r_num_cp, CROSS_CORNER_NUMS, 2, i)
                t1 = time.time()
                r_num, acts = s.useDist(20000)
                total_acts += acts
                print(time.time() - t1, "秒")
                if r_num < 0:
                    return r_num, acts
        else:
            compromise = False
            i += 1
    return r_num, total_acts

# 基準色の反対側の十字を揃える
def searchTopCross(r_num):
    # コピー
    r_num_cp = r_num
    # まずは上の十字を直接探す
    s = Search(r_num, CROSS_TOP_NUMS[0], 2, 0)
    t1 = time.time()
    r_num, acts = s.useDist(20000)
    total_acts = acts
    print(time.time() - t1, "秒")
    # 十字が見つからない場合は棒から探す
    if r_num < 0:
        # 上の棒
        s = Search(r_num_cp, BAR_TOP_NUMS, 2, 0)
        t1 = time.time()
        r_num, acts = s.useDist(20000)
        total_acts += acts
        print(time.time() - t1, "秒")
        if r_num < 0:
            return r_num, acts
        # 上の十字
        s = Search(r_num, CROSS_TOP_NUMS[0], 2, 0)
        t1 = time.time()
        r_num, acts = s.useDist(20000)
        total_acts += acts
        print(time.time() - t1, "秒")
    return r_num, total_acts

# 上の回転4パターンのどれかを探す
def searchOnlyTopRot(r_num):
    s = Search(r_num, REMAIN_TOP_ROT_LIST)
    t1 = time.time()
    total_acts = tuple()
    # 深さは最大6
    for _ in range(6):
        nr_num, procs = s.bfsFinal()
        if nr_num >= 0:
            break
    # 動作手順を動作に変換
    for p in procs:
        acts = procedure2actions(p)
        printActs(acts)
        total_acts += acts
    print(time.time() - t1, "秒")
    return nr_num, total_acts

# 幅優先で完成を目指す
# 深さは適当な値 (時間をかけたくない)
def searchCompBfs(r_num):
    s = Search(r_num)
    t1 = time.time()
    for _ in range(5):
        nr_num, acts = s.bfs()
        if nr_num >= 0:
            break
    print(time.time() - t1, "秒")
    return nr_num, acts

# 基準となる色を決める
def detStdColor(color):
    print("基準となる色は「%s」に決定" % JPN_COLOR[color])
    global CROSS_MID_ONE_NUMS, CROSS_TOP_NUMS
    global REMAIN_TOP_ROT_LIST, BAR_TOP_NUMS, CROSS_CORNER_NUMS
    global ACTIONS_C_LIST_LIST, ACTIONS_C_DASH_LIST_LIST
    global ACTIONS_D_LIST_LIST, ACTIONS_E_LIST_LIST
    global STD_COLOR
    STD_COLOR = color
    # 基準の色を決定
    CROSS_CORNER_NUMS = switchColorList(CROSS_CORNER_NUMS, color)
    CROSS_MID_ONE_NUMS = switchColorList(CROSS_MID_ONE_NUMS, color)
    CROSS_TOP_NUMS = switchColorList(CROSS_TOP_NUMS, color)
    BAR_TOP_NUMS = switchColorList(BAR_TOP_NUMS, color)
    # 色の反転に注意
    REMAIN_TOP_ROT_LIST = switchColorList(REMAIN_TOP_ROT_LIST, INV_COLOR[color])

    # 動作
    ACTIONS_C_LIST_LIST = switchColorAct(ACTIONS_C_LIST_LIST, INV_COLOR[color])
    ACTIONS_C_DASH_LIST_LIST = switchColorAct(ACTIONS_C_DASH_LIST_LIST, INV_COLOR[color])
    ACTIONS_D_LIST_LIST = switchColorAct(ACTIONS_D_LIST_LIST, INV_COLOR[color])
    ACTIONS_E_LIST_LIST = switchColorAct(ACTIONS_E_LIST_LIST, INV_COLOR[color])

def main():
    # r0 = Rubik(SAMPLE01)
    r0 = inputCube()
    all_act = tuple()
    t0 = time.time()
    if not r0.checkSum():
        print("数が合いません")
        return
    # 初期状態
    print("初期状態")
    print(r0)
    # 完成かチェック
    if r0.num == COMPLETE_NUM:
        print("既に完成しています")
        return
    # ログに状態を保持しておく
    with open("rubik_log.txt", "a", encoding="utf-8") as f:
        dt = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
        print(dt.strftime("%Y-%m-%d %H:%M:%S, "), file=f, end="")
        print(hex(r0.num), file=f)

    # とりあえず幅優先探索
    rn, act = searchCompBfs(r0.num)
    all_act += act
    phase = 0
    if rn >= 0:
        phase = 5
    
    if phase < 5:
        # 中間層まで揃っている面があるか
        for i, cmp_mid in enumerate(COMP_MID_NUMS):
            if r0.num | COMP_MID_NUM_MASKS[i] == cmp_mid:
                detStdColor(i)
                # フェーズ3までスキップ
                print("中間層まで既に揃っています")
                phase = 3
                break
        
        rn = r0.num

    # 十字を揃える
    if phase == 0:
        rn, act = searchCross(rn)
        if rn < 0:
            return
        all_act += act
        for i, cross in enumerate(CROSS_ONE_SIDE_NUMS):
            if rn | CROSS_ONE_SIDE_NUM_MASKS[i] == cross:
                detStdColor(i)
                break
        else:
            return
        phase += 1
    
    # 完全一面と中間層
    if phase == 1:
        rn, act = searchCrossCornerMid(rn)
        if rn < 0:
            return
        all_act += act
        phase += 1
    
    # 上の十字
    if phase == 2:
        rn, act = searchTopCross(rn)
        if rn < 0:
            return
        all_act += act
        phase += 1

    # 上の回転のみを残してほぼ全面揃える
    if phase == 3:
        rn, act = searchOnlyTopRot(rn)
        if rn < 0:
            return
        all_act += act
        phase += 1

    # 全面
    if phase == 4:
        rn, act = searchCompBfs(rn)
        if rn < 0:
            return
        all_act += act
        phase += 1

    # 全ての手順
    print("総手順数：{:d}".format(len(all_act)))
    printActs(all_act)
    print(time.time() - t0, "秒")

if __name__ == "__main__":
    main()
