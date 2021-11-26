from ctypes import CDLL, c_uint64, Structure

class cState(Structure):
    # コーナーの情報40bitとエッジの情報60bitに分けたい
    _fields_ = [("c_info", c_uint64), ("e_info", c_uint64)]

    def __init__(self, num: int):
        self._fields_[0] = ("c_info", c_uint64(num >> 60))
        self._fields_[1] = ("e_info", c_uint64(num & 0xfffffffffffffff))
    
    def getNum(self):
        c_info = self._fields_[0][1].value
        e_info = self._fields_[1][1].value
        print(hex(c_info))
        print(hex(e_info))
        return c_info << 60 | e_info

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
        return moji

class State2():

    def __init__(self, num: int):
        self.num = num
        self.cst = cState(self.num)
    
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
        ncst = applyMove(self.cst, arg.cst)
        print(hex(ncst.getNum()))
        return State2(ncst.getNum())
    
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

applyMove = clib.applyMove
applyMove.restype = cState
applyMove.argtypes = (cState, cState)

faces = list(moves.keys())
for face_name in faces:
    moves[face_name + "2"] = moves[face_name] * 2
    moves[face_name + "'"] = moves[face_name] * 3

scramble = "L D2 R U2 L F2 U2 L F2 R2 B2 R U' R' U2 F2 R' D B' F2"
scramble = scramble.split()

scrambled_state = solved
for move_name in scramble:
    scrambled_state += moves[move_name]
print(moves["F2"].toState2())
yeah = moves["F"].toState2()
print(yeah)
yeah3 = yeah + yeah
print(yeah3)
# print(scrambled_state)

