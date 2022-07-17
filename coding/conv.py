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
        return w_list
    
    def _calc_status_num(self):
        return int("".join([str(i) for i in itertools.chain.from_iterable(self.sr)]), 2)
    
    def __str__(self):
        moji = f"S_{self.status_num}\n"
        for i, j in enumerate(self.sr):
            moji += f"sr{i}: {j}\n"
        return moji

def create_state_transition_dict():
    """
    状態遷移の辞書を作成
    """
    c = MyCircuit()
    # 状態のビット数
    v = sum(len(i) for i in c.sr)
    st_tr_dic = {i : {} for i in range(1 << v)}
    print(st_tr_dic)

if __name__ == "__main__":
    c = MyCircuit()
    create_state_transition_dict()