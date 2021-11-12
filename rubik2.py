
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
        sub1 = 0
        sub2 = 0
        moji = ""
        for i in range(3):
            if i == 1:
                sub1 = 3
            elif i == 2:
                sub1 = 5
            for j in range(6):
                sub2 = sub1
                for k in range(3):
                    if i == 1 and k == 1:
                        moji += JPN_COLOR[j]
                    else:
                        moji += JPN_COLOR[self.cube[j][sub2]]
                        sub2 += 1
                    print(sub1, sub2)
                moji += " "
            moji += "\n"
        return moji

if __name__ == "__main__":
    r = Rubik()
    print(r)