# はげたかのえじきを定式化してみたい

class Game:

    def __init__(self):
        self.hagetaka = [True] * 15
        print(self.hagetaka)

class Player:

    def __init__(self):
        self.cards = [True] * 15
        print(self.cards)

def main():
    g = Game()
    p1 = Player()

if __name__ == "__main__":
    main()