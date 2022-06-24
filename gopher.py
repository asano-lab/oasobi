#!/usr/bin/env python3

import random as rd
import numpy as np
import pandas as pd

# 移動の成功率
# 失敗した場合その場にとどまる
SUCCESS_RATE = 0.99

X_MIN = 0
X_MAX = 2
Y_MIN = 0
Y_MAX = 2

ALL_ACTIONS = ("u", "d", "r", "l")


class Action():
    """
    動作
    """

    def __init__(self, direction: str):
        """
        u, d, r, l
        """
        self.direction = "u"
        if direction in ALL_ACTIONS:
            self.direction = direction

    def __str__(self):
        return self.direction


class Status():
    """
    状態
    """

    def __init__(self, x: int, y: int):
        self.x = max(X_MIN, min(X_MAX, x))
        self.y = max(Y_MIN, min(Y_MAX, y))

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
            self.x = max(X_MIN, min(X_MAX, self.x))
            self.y = max(Y_MIN, min(Y_MAX, self.y))

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


class QLearning():
    def __init__(self):
        all_status = [str(Status(i, j)) for i in range(X_MIN, X_MAX + 1)
                      for j in range(Y_MIN, Y_MAX + 1)]
        self.q_table = pd.DataFrame(np.zeros((len(all_status), len(ALL_ACTIONS))),
                                    columns=ALL_ACTIONS, index=all_status)
        print(self.q_table)


if __name__ == "__main__":
    a0 = Action("l")
    ql = QLearning()
