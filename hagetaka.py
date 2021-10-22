# はげたかのえじきを定式化してみたい

class Game:

    def __init__(self, p_list):
        self.hagetaka = [True] * 15
        print(self.hagetaka)
        print(*p_list)

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = [True] * 15
        print(self.cards)
    
    def __str__(self):
        moji = self.name
        for i, j in enumerate(self.cards):
            if i:
                moji += ", " + str(i)
        moji += "\n"
        return moji

def main():
    p = []
    for i in range(2):
        p.append(Player("p{:1d}".format(i)))
    g = Game(p)

if __name__ == "__main__":
    main()