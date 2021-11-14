
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

# デバッグ用サンプル状態
SAMPLE01 = [
    [3, 3, 2, 2, 4, 1, 0, 3],
    [0, 4, 2, 5, 3, 4, 0, 0],
    [5, 5, 1, 5, 2, 4, 2, 0],
    [5, 4, 5, 5, 1, 1, 0, 0],
    [4, 3, 2, 4, 1, 3, 0, 5],
    [1, 2, 3, 1, 1, 2, 3, 4]
]

JPN_COLOR = ["白", "赤", "黄", "橙", "緑", "青", "黒", "ー"]

DIC_0TO1 = {0: 1, 1: 5, 5: 3, 3: 0, 2: 2, 4: 4, 7: 7}

DIC_1TO2 = {1: 2, 2: 3, 3: 4, 4: 1, 0: 0, 5: 5, 7: 7}

DIC_ROT_R = {0: 2, 2: 7, 7: 5, 5: 0, 1: 4, 4: 6, 6: 3, 3: 1}

# 数値を2次元リストに戻す
# メソッドでなく関数として定義
def num2cube(num):
    cube = [[] for i in range(6)]
    for i in range(6):
        for j in range(8):
            cube[i].append(num & 0b111)
            num >>= 3
    return cube

class Rubik:

    def __init__(self, cube=COMPLETE, tekazu=0):
        # 値渡し
        self.cube = self._cubeCopy(cube)
        # インスタンス作成と同時に数値変換も行う
        self.num = self._cube2num(self.cube)
        self.tekazu = tekazu
    
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
    def _aboveYawPlus(self, cube):
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
    def _aboveYawMinus(self, cube):
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
    def _belowYawPlus(self, cube):
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
    def _belowYawMinus(self, cube):
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
    
    def aboveYawPlus(self):
        return self._aboveYawPlus(self.cube)
    
    def aboveYawMinus(self):
        return self._aboveYawMinus(self.cube)
    
    def belowYawPlus(self):
        return self._belowYawPlus(self.cube)
    
    def belowYawMinus(self):
        return self._belowYawMinus(self.cube)
    
    def allActions(self):
        cube_list = []
        cube_list.append(self.rightRollPlus())
        cube_list.append(self.rightRollMinus())
        cube_list.append(self.leftRollPlus())
        cube_list.append(self.leftRollMinus())
        cube_list.append(self.backPitchPlus())
        cube_list.append(self.backPitchMinus())
        cube_list.append(self.frontPitchPlus())
        cube_list.append(self.frontPitchMinus())
        cube_list.append(self.aboveYawPlus())
        cube_list.append(self.aboveYawMinus())
        cube_list.append(self.belowYawPlus())
        cube_list.append(self.belowYawMinus())
        return cube_list
    
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
    
    def __init__(self, cube_num):
        self.num_dic = {0: [cube_num]}
        self.depth = 0
    
    def bfs(self):
        nrnl = []
        for i in self.num_dic[self.depth]:
            r = Rubik(num2cube(i))
            nrl = r.allActions()
            nrnl += [nr.num for nr in nrl]
        print(len(nrnl))
        nrns = set(nrnl)
        print(len(nrns))
        del nrnl
        for knownl in self.num_dic.values():
            knowns = set(knownl)
            nrns -= knowns
        print(len(nrns))
        self.depth += 1
        self.num_dic[self.depth] = list(nrns)
        # for i in nrns:
        #     print(Rubik(num2cube(i)))
    
    # ひとまず一面を揃えたい
    def oneSide(self):
        pass

def init():
    global COMP_ONE_SIDE_NUMS, COMP_ONE_SIDE_NUM_MASKS
    # 白
    r_list = [Rubik(COMP_0)]
    # 赤
    r_list.append(r_list[0].switch0to1())
    # 黄, 橙, 緑
    for i in range(3):
        r_list.append(r_list[1 + i].switch1to2())
    # 青
    r_list.append(r_list[1].switch0to1())
    COMP_ONE_SIDE_NUMS = [r.num for r in r_list]
    COMP_ONE_SIDE_NUM_MASKS = [r.getMask() for r in r_list]

init()

if __name__ == "__main__":
    print(COMP_ONE_SIDE_NUMS)
    for i in COMP_ONE_SIDE_NUM_MASKS:
        r = Rubik(num2cube(i))
        print(r)

