import numpy as np

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
    
    def transition(self, u_list):
        w_list = []
        for g_list in self.g:
            for i, u in enumerate(u_list):
                print(u, self.sr[i], g_list[i])
        pass

if __name__ == "__main__":
    c = MyCircuit()
    c.transition([1, 1])