

class MyCircuit:

    def __init__(self):
        # シフトレジスタ
        self.sr = [[0], [0, 0]]
        # 生成系列
        self.g = [
            [[1, 1], [0, 0, 0]],
            [[0, 1], [0, 1, 1]],
            [[1, 0], [1, 0, 1]]
        ]
    
    def transition(self, u):
        w = []
        for g_list in self.g:
            print(g_list)
        pass

if __name__ == "__main__":
    c = MyCircuit()
    c.transition([1, 1])