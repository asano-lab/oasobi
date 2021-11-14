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

# 宣言
COMPLETE_NUM = 0

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

# デバッグ用サンプル状態
# SAMPLE01 = [
#     [3, 3, 2, 2, 4, 1, 0, 3],
#     [0, 4, 2, 5, 3, 4, 0, 0],
#     [5, 5, 1, 5, 2, 4, 2, 0],
#     [5, 4, 5, 5, 1, 1, 0, 0],
#     [4, 3, 2, 4, 1, 3, 0, 5],
#     [1, 2, 3, 1, 1, 2, 3, 4]
# ]

SAMPLE01 = [
    [5, 2, 0, 2, 5, 0, 5, 2],
    [4, 4, 3, 2, 0, 4, 3, 5],
    [0, 1, 4, 3, 0, 2, 1, 1],
    [1, 0, 1, 4, 5, 2, 4, 0],
    [4, 1, 3, 3, 5, 2, 1, 3],
    [5, 2, 3, 0, 4, 1, 3, 5]
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

JPN_COLOR = ["白", "赤", "黄", "橙", "緑", "青", "黒", "ー"]

DIC_0TO1 = {0: 1, 1: 5, 5: 3, 3: 0, 2: 2, 4: 4, 7: 7}

DIC_1TO2 = {1: 2, 2: 3, 3: 4, 4: 1, 0: 0, 5: 5, 7: 7}

DIC_ROT_R = {0: 2, 2: 7, 7: 5, 5: 0, 1: 4, 4: 6, 6: 3, 3: 1}

ACT_STR = ["lp", "lm", "rp", "rm", "bp", "bm", "fp", "fm", "up", "um", "dp", "dm"]

CORNERS = [0, 2, 5, 7]

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

# 色が一致している数を計算
# 与えるのはキューブの数値
# don't care を含むキューブは第二引数に与える
def calcDist(crnt, dest):
    diff = crnt ^ dest
    dist = 0
    for _ in range(48):
        # don't careでなく, 一致しない場合は加算
        if dest & 0b111 != 0b111 and diff & 0b111:
            dist += 1
        diff >>= 3
        dest >>= 3
    return dist

class Rubik:

    def __init__(self, cube=COMPLETE):
        # 値渡し
        self.cube = self._cubeCopy(cube)
        # インスタンス作成と同時に数値変換も行う
        self.num = self._cube2num(self.cube)
    
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
    # 格納した添え字を各操作の番号とする
    def allActions(self):
        return [
            self.leftRollPlus(), self.leftRollMinus(),
            self.rightRollPlus(), self.rightRollMinus(),
            self.backPitchPlus(), self.backPitchMinus(),
            self.frontPitchPlus(), self.frontPitchMinus(),
            self.upYawPlus(), self.upYawMinus(),
            self.downYawPlus(), self.downYawMinus()
        ]

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

class Search:
    
    # 目的とする状態はリストとして与える (複数あること前提)
    def __init__(self, cube_num, goal=[COMPLETE_NUM]):
        self.goal = goal
        self.explored = []
        # 初期値の距離を計算 (不要だがデバッグのため)
        crnt_dist = self.calcMinDist(cube_num)
        self.unexplored = {crnt_dist: {cube_num: tuple()}}
        self.num_dic = {0: {cube_num: tuple()}}
        # 一手の重み
        self.act_weight = 12
        print(self.unexplored)
        # 現状, 目的に最も近い (と思われる) 距離
        self.min_dist = crnt_dist
        self.depth = 0
    
    # 距離を使って優先順位を決める
    def useDist(self, loop):
        pass
    
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
    
    # 目的とするいくつかの状態から, 最も近い距離を返す
    def calcMinDist(self, cube_num):
        min_dist = 50
        for g in self.goal:
            dist = calcDist(cube_num, g)
            if dist < min_dist:
                min_dist = dist
        return min_dist

# 白基準のキューブから全ての色の等価なキューブのリストを作成
# ついでにマスクも
def makeAllColorCubeList(white_cube):
    r_list = [Rubik(white_cube)]
    r_list.append(r_list[0].switch0to1())
    for i in range(3):
        r_list.append(r_list[i + 1].switch1to2())
    r_list.append(r_list[1].switch0to1())
    return [r.num for r in r_list], [r.getMask() for r in r_list]

def init():
    global COMPLETE_NUM, COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS
    global CROSS_ONE_SIDE_NUMS, CROSS_ONE_SIDE_NUM_MASKS
    # 完成したキューブの数値
    COMPLETE_NUM = Rubik().num
    COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS = makeAllColorCubeList(COMP_0)
    CROSS_ONE_SIDE_NUMS, CROSS_ONE_SIDE_NUM_MASKS = makeAllColorCubeList(CROSS_0)

init()

def main():
    r0 = Rubik(SAMPLE01)
    if not r0.checkSum():
        return
    s = Search(r0.num, CROSS_ONE_SIDE_NUMS)

if __name__ == "__main__":
    main()

