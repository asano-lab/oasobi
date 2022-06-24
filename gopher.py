#!/usr/bin/env python3

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
    s0 = Status(0, 1)
    a0 = Action("r")
    s0.apply_action(a0)
    s0.apply_action(Action("u"))
    s0.apply_action(Action("d"))
    s0.apply_action(Action("d"))
    s1 = Status(2, 1)
    print(s0, a0, s1)
    r = reward(s0, a0, s1)
    print(r)
