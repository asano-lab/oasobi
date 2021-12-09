import os
import pickle
import os
import random
import time
import numpy as np
import rubik_win

SUBSET_PATH_FORMAT = rubik_win.SMP_DIR_PATH + "subset_act{:03d}.pickle"

BIN_SUBSET_NP_PATH_FORMAT = rubik_win.NP_DIR_PATH + "bin_subset_act{:03d}.npy"

def set2nparrayBin(num_set):
    """
    数値の集合をnumpy配列に変換する.
    ただしワンホットでバイナリ化.
    """
    ll = []
    for num in num_set:
        st = rubik_win.num2state(num)
        ll.append(st.toBinaryList())
    return np.array(ll, dtype="uint8")

def readPickleFile(fnamer: str):
    """
    pickleファイルを読み込む用.
    ファイルが存在しなければNoneを返す.
    Noneを書き込んだファイルは知らん.
    """
    if not os.path.exists(fnamer):
        return None
    f = open(fnamer, "rb")
    obj = pickle.load(f)
    f.close()
    return obj

def sampleAct9():
    """
    9手状態のデータ数が多すぎるのでランダム抽出したい.
    3億6千万くらいあるので, 1000分の1取り出したい.
    """
    t0 = time.time()
    st_subset = []
    for i in range(rubik_win.LOOP_MAX):
        fnamer = rubik_win.SN_PATH_FORMAT.format(9, i)
        sts = readPickleFile(fnamer)
        if sts is None:
            break
        print(fnamer + "からロード")
        smp_num = len(sts) // 1000
        print("使うデータ数：%d" % smp_num)
        st_subset += random.sample(list(sts), smp_num)
    fnamew = SUBSET_PATH_FORMAT.format(9)
    print("部分集合のサイズ：%d" % len(st_subset))
    # 集合にして保存
    rubik_win.writeAndBackup(fnamew, set(st_subset))
    print("%02d:%02d:%02d" % rubik_win.s2hms(time.time() - t0))

if __name__ == "__main__":
    # sampleAct9()
    # fnamer = SUBSET_PATH_FORMAT.format(9)
    # sts = readPickleFile(fnamer)
    # arr = set2nparrayBin(sts)
    # print(arr)
    # print(arr.shape)
    fnamew = BIN_SUBSET_NP_PATH_FORMAT.format(9)
    # np.save(fnamew, arr)
    arr = np.load(fnamew)
    print(arr.shape)
    for i in range(10):
        print(sum(arr[i]))
