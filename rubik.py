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

    def __init__(self) -> None:
        print(self.complete)
    
    def bfs(self) -> None:
        pass


def main() -> None:
    r = Rubik()

if __name__ == "__main__":
    main()
