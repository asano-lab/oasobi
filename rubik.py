# ルービックキューブソルバを作りたい

class Rubik():
    complete = [
        [
            [ 0,  1,  2],
            [ 7, 24,  3],
            [ 6,  5,  4]
        ], [
            [ 8,  9, 10],
            [15, 25, 11],
            [14, 13, 12]
        ], [
            [16, 17, 18],
            [23, 26, 19],
            [22, 21, 20]
        ]
    ]

    # 動かないマス
    # キーが添え字のタプルで値が数値
    immovable = {
        (0, 1, 1): 24,
        (1, 0, 1):  9,
        (1, 1, 0): 15,
        (1, 1, 1): 25,
        (1, 1, 2): 11,
        (1, 2, 1): 13,
        (2, 1, 1): 26
    }

    pos_avail = (0, 2)

    def __init__(self) -> None:
        print(self.complete)
        n = self.lll2num(self.complete)
        print(bin(n))
        lll = self.num2lll(n)
        print(lll)
        for i in range(1):
            lll = self.rollPlus(lll, 2)
            lll = self.rollMinus(lll, 2)
            # lll = self.pitchPlus(lll, 2)
            # lll = self.pitchMinus(lll, 0)
            # lll = self.yawMinus(lll, 2)
            # lll = self.yawPlus(lll, 0)
        print(lll)
    
    # 3次元リストを数値に変換 (100bit)
    def lll2num(self, lll: list) -> int:
        n = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    p = lll[i][j][k]
                    if p not in self.immovable.values():
                        n = (n << 5) | p
        return n
    
    def num2lll(self, n: int) -> list:
        lll = [[[0 for i in range(3)] for j in range(3)] for k in range(3)]
        for i in range(2, -1, -1):
            for j in range(2, -1, -1):
                for k in range(2, -1, -1):
                    if (i, j, k) in self.immovable:
                        lll[i][j][k] = self.immovable[(i, j, k)]
                    else:
                        lll[i][j][k] = n & 0b11111
                        n >>= 5
        return lll
    
    # 3次元リストのコピー
    def lllCopy(self, lll: list) -> list:
        lcp = [[] for i in range(3)]
        for i, j in enumerate(lll):
            for k in j:
                lcp[i].append(k.copy())
        return lcp

    # 下方向に90deg回転
    # 第2引数には回転させる位置を与える
    # 0: left, 2: right
    # とりあえず真ん中は1ステップで動かせないものとする
    # 軸に対して右ねじの向きをプラスにした
    def rollPlus(self, cube: list, x: int) -> list:
        if x not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][0][x] = cube[2][0][x]
        n_cube[2][0][x] = cube[2][2][x]
        n_cube[2][2][x] = cube[0][2][x]
        n_cube[0][2][x] = cube[0][0][x]
        n_cube[0][1][x] = cube[1][0][x]
        n_cube[1][0][x] = cube[2][1][x]
        n_cube[2][1][x] = cube[1][2][x]
        n_cube[1][2][x] = cube[0][1][x]
        return n_cube
    
    # 上方向に90deg回転
    # 0: left, 2: right
    def rollMinus(self, cube: list, x: int) -> list:
        if x not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][0][x] = cube[0][2][x]
        n_cube[0][2][x] = cube[2][2][x]
        n_cube[2][2][x] = cube[2][0][x]
        n_cube[2][0][x] = cube[0][0][x]
        n_cube[0][1][x] = cube[1][2][x]
        n_cube[1][2][x] = cube[2][1][x]
        n_cube[2][1][x] = cube[1][0][x]
        n_cube[1][0][x] = cube[0][1][x]
        return n_cube
    
    # y軸周りに回転 (順)
    # 0: back, 2: front
    def pitchPlus(self, cube: list, y: int) -> list:
        if y not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][y][0] = cube[0][y][2]
        n_cube[0][y][2] = cube[2][y][2]
        n_cube[2][y][2] = cube[2][y][0]
        n_cube[2][y][0] = cube[0][y][0]
        n_cube[0][y][1] = cube[1][y][2]
        n_cube[1][y][2] = cube[2][y][1]
        n_cube[2][y][1] = cube[1][y][0]
        n_cube[1][y][0] = cube[0][y][1]
        return n_cube
    
    # y軸周りに回転 (逆)
    # 0: back, 2: front
    def pitchMinus(self, cube: list, y: int) -> list:
        if y not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][y][0] = cube[2][y][0]
        n_cube[2][y][0] = cube[2][y][2]
        n_cube[2][y][2] = cube[0][y][2]
        n_cube[0][y][2] = cube[0][y][0]
        n_cube[0][y][1] = cube[1][y][0]
        n_cube[1][y][0] = cube[2][y][1]
        n_cube[2][y][1] = cube[1][y][2]
        n_cube[1][y][2] = cube[0][y][1]
        return n_cube
    
    # z軸周りに回転 (順)
    # 0: top, 2: bottom
    def yawPlus(self, cube: list, z: int) -> list:
        if z not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[z][0][0] = cube[z][2][0]
        n_cube[z][2][0] = cube[z][2][2]
        n_cube[z][2][2] = cube[z][0][2]
        n_cube[z][0][2] = cube[z][0][0]
        n_cube[z][0][1] = cube[z][1][0]
        n_cube[z][1][0] = cube[z][2][1]
        n_cube[z][2][1] = cube[z][1][2]
        n_cube[z][1][2] = cube[z][0][1]
        return n_cube

    # z軸周りに回転 (逆)
    # 0: top, 2: bottom
    def yawMinus(self, cube: list, z: int) -> list:
        if z not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[z][0][0] = cube[z][0][2]
        n_cube[z][0][2] = cube[z][2][2]
        n_cube[z][2][2] = cube[z][2][0]
        n_cube[z][2][0] = cube[z][0][0]
        n_cube[z][0][1] = cube[z][1][2]
        n_cube[z][1][2] = cube[z][2][1]
        n_cube[z][2][1] = cube[z][1][0]
        n_cube[z][1][0] = cube[z][0][1]
        return n_cube
        
    def bfs(self) -> None:
        pass


def main() -> None:
    r = Rubik()

if __name__ == "__main__":
    main()
