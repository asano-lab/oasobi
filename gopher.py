#!/usr/bin/env python3

class Status():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


if __name__ == "__main__":
    st0 = Status(2, 3)
    print(st0)
