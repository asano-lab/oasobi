# はげたかのえじきを定式化してみたい

class Game:

    def __init__(self):
        self.hagetaka = [True] * 15
        self.hagetaka[5] = False
        print(self.hagetaka)
        print("hello world")

def main():
    g = Game()

if __name__ == "__main__":
    main()