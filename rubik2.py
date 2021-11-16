import time

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

# 白の十字
CROSS_0 = [
    [7, 0, 7, 0, 0, 7, 0, 7],
    [7, 1, 7, 7, 7, 7, 7, 7],
    [7, 2, 7, 7, 7, 7, 7, 7],
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

SAMPLE01 = [
    [5, 5, 3, 4, 0, 4, 4, 4],
    [3, 3, 5, 2, 5, 3, 4, 0],
    [1, 3, 2, 1, 0, 2, 2, 0],
    [5, 3, 2, 2, 1, 1, 3, 0],
    [1, 0, 0, 0, 5, 3, 4, 5],
    [4, 1, 1, 5, 1, 2, 2, 4]
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

# 操作の変換
# 赤正面 -> 黄色正面
# Z軸回りの動作は等価
ACT_DIC_0TO7 = {0: 7, 7: 3, 3: 4, 4: 0, 1: 6, 6: 2, 2: 5, 5: 1, 8: 8, 9: 9, 10: 10, 11: 11}

ACT_DIC_4TO8 = {4: 8, 8: 7, 7: 11, 11: 4, 5: 9, 9: 6, 6: 10, 10: 5, 0: 0, 1: 1, 2: 2, 3: 3}

# ACT_STR = ["lp", "lm", "rp", "rm", "bp", "bm", "fp", "fm", "up", "um", "dp", "dm"]
ACT_STR = ["L", "L'", "R'", "R", "B", "B'", "F'", "F", "U", "U'", "D'", "D"]

ACT_PATTERN_STR = ["C", "C'", "D", "E"]

CORNERS = [0, 2, 5, 7]

# 真逆の色
INV_COLOR = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

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
    moji = ""
    im = len(acts) - 1
    for i, act in enumerate(acts):
        moji += ACT_STR[act]
        if i < im:
            moji += ", "
    print(moji)

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
    
    def checkSum(self):
        corners_sum = {i: 0 for i in range(6)}
        edges_sum = {i: 0 for i in range(6)}
        # print(corners_sum)
        # print(edges_sum)
        for i in range(6):
            for j in range(8):
                if j in CORNERS:
                    corners_sum[self.cube[i][j]] += 1
                else:
                    edges_sum[self.cube[i][j]] += 1
        for i in corners_sum.values():
            if i != 4:
                return False
        for i in edges_sum.values():
            if i != 4:
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
    def __init__(self, cube_num, goal=[COMPLETE_NUM], act_weight=12, match_num=0):
        self.goal = goal
        self.act_weight = act_weight
        self.explored = []
        self.match_num = match_num
        # 初期値
        self.init_cube = cube_num
        # 初期値の距離を計算 (不要だがデバッグのため)
        crnt_dist = self.calcDistMatchNum(cube_num)
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
            r = Rubik(num2cube(k))
            nrl = r.allActions()
            # 新状態を確認
            for j, nr in enumerate(nrl):
                # 探索済みに含まれていたらやりなおし
                if nr.num in self.explored:
                    continue
                # 未探索に含まれていてもやりなおし
                for known in self.unexplored.values():
                    if nr.num in known:
                        continue
                # 最短距離を計算
                dist = self.calcDistMatchNum(nr.num)
                # 一致したら終了
                if dist == 0:
                    print(nr)
                    printActs(v + (j,))
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
        return (-1, -1)
    
    # 幅優先探索 (全探索)
    def bfs(self):
        nrnd = {}
        for k, v in self.num_dic[self.depth].items():
            r = Rubik(num2cube(k))
            nrl = r.allActions()
            for i, nr in enumerate(nrl):
                # 解けた
                if nr.num == COMPLETE_NUM:
                    print(nr)
                    printActs(v + (i,))
                    return True
                # 一面揃ったかチェック
                for j, one_side in enumerate(COMP_ONE_SIDE_NUMS):
                    if nr.num | COMP_ONE_SIDE_NUM_MASKS[j] == one_side:
                        print(nr)
                        printActs(v + (i,))
                        return True
                # 十字が揃ったかチェック
                for j, cross in enumerate(CROSS_ONE_SIDE_NUMS):
                    if nr.num | CROSS_ONE_SIDE_NUM_MASKS[j] == cross:
                        print(nr)
                        printActs(v + (i,))
                        return True
                nrnd[nr.num] = v + (i,)

        print(len(nrnd))
        nrns = set(nrnd)
        for knownd in self.num_dic.values():
            knowns = set(knownd)
            nrns -= knowns
        print(len(nrns))
        self.depth += 1
        self.num_dic[self.depth] = {k: v for k, v in nrnd.items() if k in nrns}
        return False
    
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
                    if not self.calcDistMatchNum(nr.num):
                        print(nr)
                        print(past_acts + (act_name,))
                        return (nr.num, past_acts + (act_name,))
                    nrnd[nr.num] = past_acts + (act_name,)

        # 重複排除フェーズ
        nrns = set(nrnd)
        for knownd in self.num_dic.values():
            knowns = set(knownd)
            nrns -= knowns
        print("新状態数:", len(nrns))
        self.depth += 1
        self.num_dic[self.depth] = {k: v for k, v in nrnd.items() if k in nrns}
        return (-1, -1)
    
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
    global COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS
    global CROSS_ONE_SIDE_NUMS, CROSS_ONE_SIDE_NUM_MASKS
    global CROSS_MID_ONE_NUMS, BAR_TOP_NUMS, CROSS_TOP_NUMS, COMP_TOP_NUMS
    global TOP_PATTERN_NUMS
    global ACTIONS_C_LIST_LIST, ACTIONS_C_DASH_LIST_LIST
    global ACTIONS_D_LIST_LIST, ACTIONS_E_LIST_LIST
    global REMAIN_TOP_ROT_LIST
    # 十字と完全一面
    COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS = makeAllColorCubeList(COMP_0)
    CROSS_ONE_SIDE_NUMS, CROSS_ONE_SIDE_NUM_MASKS = makeAllColorCubeList(CROSS_0)
    # 4種類の側面の辺
    r_list = [Rubik(CROSS_0_MID_12)]
    for i in range(3):
        r_list.append(r_list[i].switch1to2())
    CROSS_MID_ONE_NUMS = [r.num for r in r_list]
    # 上の棒
    r_list = [Rubik(BAR_TOP)]
    r_list.append(r_list[0].downYawPlus())
    BAR_TOP_NUMS = [r.num for r in r_list]
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

def main():
    global CROSS_MID_ONE_NUMS, CROSS_TOP_NUMS, COMP_TOP_NUMS, TOP_PATTERN_NUMS
    global REMAIN_TOP_ROT_LIST, BAR_TOP_NUMS
    global ACTIONS_C_LIST_LIST, ACTIONS_C_DASH_LIST_LIST
    global ACTIONS_D_LIST_LIST, ACTIONS_E_LIST_LIST
    # r0 = Rubik(num2cube(SAMPLE_WHITE_SIDE_MID))
    # r0 = Rubik(num2cube(SAMPLE_FINAL_01))
    r0 = Rubik(SAMPLE01)
    t0 = time.time()
    if not r0.checkSum():
        print("数が合いません")
        return
    # 初期状態
    print("初期状態")
    print(r0)
    # 十字を揃える
    s = Search(r0.num, CROSS_ONE_SIDE_NUMS, 2)
    t1 = time.time()
    rn, act1 = s.useDist(13000)
    print(time.time() - t1, "秒")
    if rn < 0:
        return
    color = 0
    for j, cross in enumerate(CROSS_ONE_SIDE_NUMS):
        if rn | CROSS_ONE_SIDE_NUM_MASKS[j] == cross:
            color = j
            break
    else:
        return
    # 基準の色を決定
    CROSS_MID_ONE_NUMS = switchColorList(CROSS_MID_ONE_NUMS, color)
    CROSS_TOP_NUMS = switchColorList(CROSS_TOP_NUMS, color)
    COMP_TOP_NUMS = switchColorList(COMP_TOP_NUMS, color)
    TOP_PATTERN_NUMS = switchColorList(TOP_PATTERN_NUMS, color)
    BAR_TOP_NUMS = switchColorList(BAR_TOP_NUMS, color)
    # 色の反転に注意
    REMAIN_TOP_ROT_LIST = switchColorList(REMAIN_TOP_ROT_LIST, INV_COLOR[color])

    # 動作
    ACTIONS_C_LIST_LIST = switchColorAct(ACTIONS_C_LIST_LIST, INV_COLOR[color])
    ACTIONS_C_DASH_LIST_LIST = switchColorAct(ACTIONS_C_DASH_LIST_LIST, INV_COLOR[color])
    ACTIONS_D_LIST_LIST = switchColorAct(ACTIONS_D_LIST_LIST, INV_COLOR[color])
    ACTIONS_E_LIST_LIST = switchColorAct(ACTIONS_E_LIST_LIST, INV_COLOR[color])

    for i in range(4):
        s = Search(rn, CROSS_MID_ONE_NUMS, 1, i)
        t1 = time.time()
        rn, act = s.useDist(20000)
        print(time.time() - t1, "秒")
        if rn < 0:
            return
    # 上の棒
    s = Search(rn, BAR_TOP_NUMS, 1, 0)
    t1 = time.time()
    rn, act = s.useDist(20000)
    print(time.time() - t1, "秒")
    if rn < 0:
        return
    # 上の十字
    s = Search(rn, CROSS_TOP_NUMS, 1, 0)
    t1 = time.time()
    rn, act = s.useDist(20000)
    print(time.time() - t1, "秒")
    if rn < 0:
        return
    # パターンのいずれか
    # s = Search(rn, TOP_PATTERN_NUMS, 1, 0)
    # t1 = time.time()
    # rn, act = s.useDist(20000)
    # print(time.time() - t1, "秒")
    # if rn < 0:
    #     return
    # 残るは上の回転のみ
    s = Search(rn, REMAIN_TOP_ROT_LIST)
    t1 = time.time()
    for i in range(5):
        rn, act = s.bfsFinal()
        if rn >= 0:
            break
    print(time.time() - t1, "秒")
    if rn < 0:
        return
    # # 全面
    # s = Search(rn, [COMPLETE_NUM], 1, 0)
    # t1 = time.time()
    # rn, act = s.useDist(30000)
    # print(time.time() - t1, "秒")
    # if rn < 0:
    #     return
    print(time.time() - t0, "秒")

if __name__ == "__main__":
    main()
