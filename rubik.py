from ctypes import CDLL, c_int32, c_ulonglong

# 日本仕様の色
JPN_COLOR = {"U": "白", "D": "青", "L": "橙", "R": "赤", "F": "緑", "B": "黄"}

# 角のブロックの色, 各3色
# U, Dの色を基準にして反時計回りに並べる
CORNER_COLOR = {
    0: "UBL", 1: "URB", 2: "UFR", 3: "ULF",
    4: "DLB", 5: "DBR", 6: "DRF", 7: "DFL"
}

# 辺のブロックの色, 各2色
# 基準面の色が先頭
EDGE_COLOR = {
    0: "BL", 1: "BR", 2: "FR", 3: "FL",
    4: "UB", 5: "UR", 6: "UF", 7: "UL",
    8: "DB", 9: "DR", 10: "DF", 11: "DL"
}

CORNER_PO2COLOR = {
    0: ((0, 0), (0, 11), (0, 12)), 1: ((0, 2), (0, 8), (0, 9)),
    2: ((2, 2), (0, 5), (0, 6)), 3: ((2, 0), (0, 14), (0, 3)),
    4: ((2, 15), (2, 12), (2, 11)), 5: ((2, 17), (2, 9), (2, 8)),
    6: ((0, 17), (2, 6), (2, 5)), 7: ((0, 15), (2, 3), (2, 14))
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
    
    # 数値で扱うクラスに変換
    def toState2(self):
        s_num = 0
        for i in range(8):
            s_num = (s_num << 3) | self.cp[i]
            s_num = (s_num << 2) | self.co[i]
        for i in range(12):
            s_num = (s_num << 4) | self.ep[i]
            s_num = (s_num << 1) | self.eo[i]
        return State2(s_num)
    
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
        color_array = [[-1] * 18 for _ in range(3)]
        for k, v in CORNER_PO2COLOR.items():
            for i, jt in enumerate(v):
                color_array[jt[0]][jt[1]] = CORNER_COLOR[self.cp[k]][(self.co[k] + i) % 3]
        color_array[0][1] = EDGE_COLOR[self.ep[4]][self.eo[4]]
        color_array[0][4] = EDGE_COLOR[self.ep[6]][self.eo[6] ^ 1]
        color_array[0][7] = EDGE_COLOR[self.ep[5]][self.eo[5] ^ 1]
        color_array[0][10] = EDGE_COLOR[self.ep[4]][self.eo[4] ^ 1]
        color_array[0][13] = EDGE_COLOR[self.ep[7]][self.eo[7] ^ 1]
        color_array[0][16] = EDGE_COLOR[self.ep[10]][self.eo[10]]
        print(color_array)
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
    
    def __add__(self, arg):
        nc_arr = cull2()
        applyMove(self.c_arr, arg.c_arr, nc_arr)
        n_list = list(nc_arr)
        return State2(n_list[0] << 60 | n_list[1])
    
    def __str__(self):
        return hex(self.num)

# 完成形
solved = State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
)

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

clib = CDLL("./rubik.so")

cull2 = c_ulonglong * 2

applyMove = clib.applyMove
applyMove.restype = c_int32
applyMove.argtypes = (cull2, cull2, cull2)

faces = list(moves.keys())
for face_name in faces:
    moves[face_name + "2"] = moves[face_name] * 2
    moves[face_name + "'"] = moves[face_name] * 3

scramble = "L D2 R U2 L F2 U2 L F2 R2 B2 R U' R' U2 F2 R' D B' F2"
scramble = scramble.split()

scrambled_state = solved
for move_name in scramble:
    scrambled_state += moves[move_name]

# print(scrambled_state)

scrambled_state = solved.toState2()
for move_name in scramble:
    scrambled_state += moves[move_name].toState2()

# print(scrambled_state.toState())

print(moves["L"])
# print(moves["R"])
# print(moves["R'"])
# print(moves["B"])
print(moves["F'"])
