import numpy as np
import itertools

class MyCircuit:

    def __init__(self, status_num=0):
        # シフトレジスタ
        self.sr = [[0], [0, 0]]
        self.v = sum(len(i) for i in self.sr)
        # 生成系列
        self.g = [
            [[1, 1], [0, 0, 0]],
            [[0, 1], [0, 1, 1]],
            [[1, 0], [1, 0, 1]]
        ]
        self._set_sr(status_num)
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
        """
        レジスタの中身から状態番号計算
        """
        return int("".join([str(i) for i in itertools.chain.from_iterable(self.sr)]), 2)
    
    def _set_sr(self, status_num):
        """
        シフトレジスタの中身を指定した状態に対応させる
        """
        idx = 0
        st_bin_str = format(status_num, f"0{self.v}b")
        for i in range(len(self.sr)):
            for j in range(len(self.sr[i])):
                self.sr[i][j] = int(st_bin_str[idx])
                idx += 1
    
    def __str__(self):
        moji = f"S_{self.status_num}\n"
        for i, j in enumerate(self.sr):
            moji += f"sr{i}: {j}\n"
        return moji

def create_state_transition_dict():
    """
    状態遷移の辞書を作成
    """
    c = MyCircuit(1)
    print(c)
    st_tr_dic = {i : {} for i in range(1 << c.v)}
    print(st_tr_dic)

if __name__ == "__main__":
    create_state_transition_dict()