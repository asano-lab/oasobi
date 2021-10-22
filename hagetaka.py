# はげたかのえじきを定式化してみたい

class Game:

    def __init__(self, p_list):
        self.hagetaka = [True] * 15
        print(self.hagetaka)
        for i in p_list:
            print(i)

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = [True] * 15
        # print(self.cards)
    
    def __str__(self):
        moji = self.name + "\ncards: "
        for i, j in enumerate(self.cards):
            if j:
                moji += "{:2d}".format(i + 1)
            if i != 14:
                moji += ", "
        # moji += "\n"
        return moji

def main():
    p = []
    for i in range(2):
        p.append(Player("p{:1d}".format(i)))
    g = Game(p)

if __name__ == "__main__":
    main()