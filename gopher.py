#!/usr/bin/env python3

class Status():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


class Action():
    def __init__(self, direction: str):
        """
        u, d, r, l
        """
        self.direction = direction

    def __str__(self):
        return self.direction


if __name__ == "__main__":
    s0 = Status(0, 1)
    a0 = Action("r")
    print(s0, a0)
