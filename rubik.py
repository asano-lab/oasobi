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
    immovable = [9, 11, 13, 15, 24, 25, 26]

    # 動かないマスの添え字
    immovable_ind = [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)]

    def __init__(self) -> None:
        print(self.complete)
        n = self.lll2num(self.complete)
        print(bin(n))
        lll = self.num2lll(n)
        print(lll)
    
    # 3次元リストを数値に変換 (100bit)
    def lll2num(self, lll: list) -> int:
        n = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    p = lll[i][j][k]
                    if p not in self.immovable:
                        n = (n << 5) | p
        return n
    
    def num2lll(self, n: int) -> list:
        lll = [[[0 for i in range(3)] for j in range(3)] for k in range(3)]
        for i in range(2, -1, -1):
            for j in range(2, -1, -1):
                for k in range(2, -1, -1):
                    if (i, j, k) not in self.immovable_ind:
                        lll[i][j][k] = n & 0b11111
                        n >>= 5
        return lll
    
    def bfs(self) -> None:
        pass


def main() -> None:
    r = Rubik()

if __name__ == "__main__":
    main()
