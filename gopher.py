#!/usr/bin/env python3

class Status():
    """
    状態
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Action():
    """
    動作
    """

    def __init__(self, direction: str):
        """
        u, d, r, l
        """
        self.direction = direction

    def __str__(self):
        return self.direction


def reward(s_t: Status, a_t: Action, s_tp1: Status) -> float:
    """
    報酬
    """
    r = 1.0
    if (s_tp1.x == 2 and s_tp1.y == 2):
        r = 100.0
    return r


if __name__ == "__main__":
    s0 = Status(0, 1)
    a0 = Action("r")
    s1 = Status(2, 1)
    print(s0, a0, s1)
    r = reward(s0, a0, s1)
    print(r)
