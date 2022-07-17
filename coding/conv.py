import numpy as np
import itertools

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
        self.status_num = self._calc_status_num()
    
    def transition(self, u_list):
        """
        状態遷移
        """
        w_list = []
        for g_list in self.g:
            w = 0
            for i, u in enumerate(u_list):
                sr_vec = np.array([u] + self.sr[i])
                g_vec = np.array(g_list[i])
                w += np.dot(sr_vec, g_vec)
            w_list.append(w % 2)
        for i in range(len(self.sr)):
            self.sr[i] = [u_list[i]] + self.sr[i][:-1]
        self.status_num = self._calc_status_num()
    
    def _calc_status_num(self):
        return int("".join([str(i) for i in itertools.chain.from_iterable(self.sr)]), 2)

if __name__ == "__main__":
    c = MyCircuit()
    print(c.status_num)
    c.transition([1, 1])
    print(c.status_num)