
# 完成した盤面
# 日本配色で白, 赤, 黄, 橙, 緑, 青の順
# 中央の情報は含まない
COMPLETE = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5, 5]
]

JPN_COLOR = ["白", "赤", "黄", "橙", "緑", "青"]

class Rubik:

    def __init__(self, cube=COMPLETE):
        self.cube = cube
    
    def __str__(self):
        sub = 0
        moji = ""
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    moji += "白"
                else:
                    moji += JPN_COLOR[self.cube[0][sub]]
                    sub += 1
            moji += "\n"
        return moji

if __name__ == "__main__":
    r = Rubik()
    print(r)