import numpy as np
from scipy.sparse.csgraph import shortest_path
import itertools

class MyCircuit:

    def __init__(self, status_num=0):
        # シフトレジスタ
        self.sr = [[0], [0, 0]]
        # メモリ数
        self.v = sum(len(i) for i in self.sr)
        # 同時入力数??
        self.u_len = len(self.sr)
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
    # 全状態
    st_tr_dic = {i : {} for i in range(1 << c.v)}
    # 全入力パターン
    act_list = [[int(j) for j in format(i, f"0{c.u_len}b")] for i in range(1 << c.u_len)]
    for st in st_tr_dic.keys():
        for u_list in act_list:
            c = MyCircuit(st)
            w_list = c.transition(u_list)
            st_tr_dic[st][c.status_num] = [u_list, w_list]
    return st_tr_dic

def to_adjacency_matrix(st_tr_dic: dict):
    """
    状態遷移の辞書から隣接行列作成
    重み付き有効グラフとする
    重みは出力のハミング重み
    """
    m = np.zeros([len(st_tr_dic)] * 2)
    for src, child_dic in st_tr_dic.items():
        for dst, uw in child_dic.items():
            weight = sum(uw[1])
            if weight == 0:
                weight = 1e-5
            m[src][dst] = weight
    return m

def get_path(src, dst, p):
    sp = []
    p_row = p[src]
    i = dst
    while i != src and i >= 0:
        sp.append(i)
        i = p_row[i]
    if i < 0:
        sp = []
    else:
        sp.append(i)
    return sp[::-1]
    

if __name__ == "__main__":
    d = create_state_transition_dict()
    m = to_adjacency_matrix(d)
    # print(m)
    saitan_w, saitan_p = shortest_path(m, method="D", return_predecessors=True)
    saitan_w = saitan_w.astype("u1")
    print(saitan_w)
    print(saitan_p)
    print(get_path(2, 6, saitan_p))