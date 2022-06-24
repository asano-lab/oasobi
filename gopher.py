#!/usr/bin/env python3

import random as rd

# 移動の成功率
# 失敗した場合その場にとどまる
SUCCESS_RATE = 0.99


class Action():
    """
    動作
    """

    def __init__(self, direction: str):
        """
        u, d, r, l
        """
        self.direction = "u"
        if direction in ("u", "d", "r", "l"):
            self.direction = direction

    def __str__(self):
        return self.direction


class Status():
    """
    状態
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def apply_action(self, a: Action):
        """
        動作適用
        """
        if rd.random() < SUCCESS_RATE:
            if a.direction == "u":
                self.y += 1
            elif a.direction == "d":
                self.y -= 1
            elif a.direction == "r":
                self.x += 1
            else:
                self.x -= 1
            self.x = max(0, min(2, self.x))
            self.y = max(0, min(2, self.y))

    def copy(self):
        return Status(self.x, self.y)

    def __eq__(self, s):
        """
        等号演算子の処理
        """
        return self.x == s.x and self.y == s.y

    def __str__(self):
        return f"({self.x},{self.y})"


def reward(s_t: Status, a_t: Action, s_tp1: Status) -> float:
    """
    報酬
    """
    r = 1.0
    if (s_tp1.x == 2 and s_tp1.y == 2):
        r = 100.0
    return r


if __name__ == "__main__":
    a0 = Action("l")
    c = 0
    for i in range(10000):
        s0 = Status(2, 0)
        s1 = s0.copy()
        s1.apply_action(a0)
        if s0 == s1:
            c += 1
    print(c)
