# はげたかのえじきを定式化してみたい

import random as rd

# はげたかの得点
POINTS = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Game:

    def __init__(self, p_list):
        self.flag_hagetaka = [True] * 15
        self.hagetaka = [i for i in range(15)]
        self.num_hagetaka = 15
        self.p_list = p_list
        self.population = len(self.p_list)
        self.place_card = []
    
    def step(self):
        ind = rd.randint(0, self.num_hagetaka - 1)
        selected = self.hagetaka.pop(ind)
        self.flag_hagetaka[selected] = False
        self.num_hagetaka -= 1
        reward = POINTS[selected]

        if reward == 0:
            return

        # 各プレイヤーがカードを出す
        self.place_card = []

        for i in range(self.population):
            if reward > 0:
                self.place_card.append(self.p_list[i].selectCard())
            else:
                self.place_card.append(-self.p_list[i].selectCard())
            
        print(reward)
        print(self.place_card)
        

    def __str__(self):
        moji = "remain: "
        for i, j in enumerate(self.hagetaka):
            moji += "{:2d}".format(POINTS[j])
            if i != self.num_hagetaka - 1:
                moji += ", "
        moji += "\n"
        for i in self.p_list:
            moji += i.__str__()
        return moji

class Player:

    def __init__(self, name):
        self.name = name
        self.flag_cards = [True] * 15
        self.cards = [i for i in range(1, 16)]
        self.num_cards = 15
        self.hagetaka = [False] * 15
        self.point = 0
    
    def selectCard(self):
        ind = rd.randint(0, self.num_cards - 1)
        selected = self.cards.pop(ind)
        self.flag_cards[selected - 1] = False
        self.num_cards -= 1
        return selected
    
    def __str__(self):
        moji = self.name + "\ncards: "
        moji += str(self.cards)

        moji += "\nhagetaka:"

        for i, j in enumerate(self.hagetaka):
            if j:
                moji += "{:2d}".format(POINTS[i])
                if i != 14:
                    moji += ", "
        moji += "\npoint: {:3d}\n".format(self.point)
        return moji

def main():
    p = []
    for i in range(2):
        p.append(Player("p{:1d}".format(i)))
    g = Game(p)
    print(g)
    g.step()
    print(g)

if __name__ == "__main__":
    main()