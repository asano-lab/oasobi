# はげたかのえじきを定式化してみたい

class Game:

    def __init__(self, p_list):
        self.hagetaka = [True] * 15
        print(self.hagetaka)
        print(p_list)

class Player:

    def __init__(self):
        self.cards = [True] * 15
        print(self.cards)

def main():
    p1 = Player()
    p2 = Player()
    g = Game([p1, p2])

if __name__ == "__main__":
    main()