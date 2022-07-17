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
                sr_vec = np.array([u] + self.sr[i])
                g_vec = np.array(g_list[i])
                print(sr_vec, g_vec, np.dot(sr_vec, g_vec))
        pass

if __name__ == "__main__":
    c = MyCircuit()
    c.transition([1, 1])