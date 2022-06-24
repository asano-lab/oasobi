#!/usr/bin/env python3

import random as rd
import numpy as np
import pandas as pd

# 移動の成功率
# 失敗した場合その場にとどまる
SUCCESS_RATE = 0.99

# 時間割引率
TIME_DISCOUNT_RATE = 0.9

# 学習率
LEARNING_RATE = 0.2

# ランダムな行動をする確率
EPSILON = 0.3

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

    def is_goal(self):
        """
        ゴールかどうか
        """
        return self.x == X_MAX and self.y == Y_MAX

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
    r = 0.0
    if s_tp1.is_goal():
        r = 100.0
    return r


class QLearning():
    """
    Q学習
    """

    def __init__(self):
        all_status = [str(Status(i, j)) for i in range(X_MIN, X_MAX + 1)
                      for j in range(Y_MIN, Y_MAX + 1)]
        initial_array = np.zeros((len(all_status), len(ALL_ACTIONS)))
        # initial_array = np.random.random((len(all_status), len(ALL_ACTIONS)))
        self.q_table = pd.DataFrame(initial_array,
                                    columns=ALL_ACTIONS, index=all_status)
        print(self.q_table)

    def _calc_next_action(self, st: Status):
        """
        Qテーブルと現在の状態から次の行動を決定
        """
        # 冒険
        if rd.random() < EPSILON:
            return Action(rd.choice(ALL_ACTIONS))
        st_series = self.q_table.loc[str(st)]
        # 最良の手を選択
        best_actions_idx = [i for i, j in enumerate(
            st_series) if j == st_series.max()]
        # 最良の手が複数あれば抽選
        return Action(ALL_ACTIONS[rd.choice(best_actions_idx)])

    def one_game(self):
        """
        ゲームを1回行う
        """
        # 開始状態
        st_now = Status(1, 0)
        while not st_now.is_goal():
            best_action = self._calc_next_action(st_now)
            # print(best_action)
            st_next = st_now.copy()
            st_next.apply_action(best_action)
            print(st_now, best_action, st_next)
            # print(st_next)
            # 現在の状態でとった行動のQ値
            q_now = self.q_table[str(best_action)][str(st_now)]
            # print(q_now)
            # 即時報酬
            imm_reward = reward(st_now, best_action, st_next)
            # print(imm_reward)
            if st_now.is_goal():
                q_next_max = 0
            else:
                q_next_max = self.q_table.loc[str(st_next)].max()
            # print(q_next_max)
            self.q_table[str(best_action)][str(st_now)] = q_now + LEARNING_RATE * \
                (imm_reward + TIME_DISCOUNT_RATE * q_next_max - q_now)
            print(self.q_table)
            st_now = st_next

    def mainloop(self, loop_num):
        """
        ゲームを繰り返してQテーブル更新
        """
        for i in range(loop_num):
            self.one_game()


if __name__ == "__main__":
    ql = QLearning()
    ql.mainloop(1000)
