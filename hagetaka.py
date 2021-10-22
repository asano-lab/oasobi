# はげたかのえじきを定式化してみたい

import random as rd

# はげたかの得点
POINTS = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Game:

    def __init__(self, p_list):
        self.hagetaka = [True] * 15
        self.p_list = p_list
        self.population = len(p_list)
        self.place_card = []

        for i in p_list:
            print(i)
    
    def step(self):
        self.place_card = []
        for i in range(self.population):
            self.place_card.append(0)
            print(self.p_list[i].selectCard())

    def __str__(self):
        moji = "remain: "
        for i, j in enumerate(self.hagetaka):
            if j:
                moji += "{:2d}".format(POINTS[i])
                if i != 14:
                    moji += ", "
        return moji

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = [True] * 15
        self.num_cards = 15
        self.hagetaka = [False] * 15
        self.point = 0
    
    def selectCard(self):
        ind = rd.randint(0, self.num_cards - 1)
        return ind
    
    def __str__(self):
        moji = self.name + "\ncards: "
        for i, j in enumerate(self.cards):
            if j:
                moji += "{:2d}".format(i + 1)
                if i != 14:
                    moji += ", "

        moji += "\nhagetaka:"

        for i, j in enumerate(self.hagetaka):
            if j:
                moji += "{:2d}".format(POINTS[i])
                if i != 14:
                    moji += ", "
        moji += "\npoint: {:3d}".format(self.point)
        return moji

def main():
    p = []
    for i in range(2):
        p.append(Player("p{:1d}".format(i)))
    g = Game(p)
    print(g)
    g.step()

if __name__ == "__main__":
    main()