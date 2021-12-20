import os
import pickle
import os
import random
import time
import numpy as np
import rubik_win
from rubik_win import SMP_DIR_PATH, SMP_PATH_FORMAT, writeAndBackup

SUBSET_PATH_FORMAT = rubik_win.SMP_DIR_PATH + "subset_act{:03d}.pickle"
BIN_SUBSET_NP_PATH_FORMAT = rubik_win.NP_DIR_PATH + "bin_subset_act{:03d}.npy"
SUBSET_NP_PATH_FORMAT = rubik_win.NP_DIR_PATH + "subset_act{:03d}.npy"
TT_NPZ_PATH_FORMAT = rubik_win.NP_DIR_PATH + "train_test_act{:03d}.npz"
ONEHOT_TT_NPZ_PATH_FORMAT = rubik_win.NP_DIR_PATH + "onehot_train_test_act{:03d}.npz"
MERGED_SMP_PATH = SMP_DIR_PATH + "merged_sample016.pickle"

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

def sampleActLT10(act_num, ratio):
    """
    0 ~ 9手状態のデータ数からランダム抽出.
    """
    t0 = time.time()
    st_subset = []
    for i in range(rubik_win.LOOP_MAX):
        fnamer = rubik_win.SN_PATH_FORMAT.format(act_num, i)
        sts = readPickleFile(fnamer)
        if sts is None:
            break
        print(fnamer + "からロード")
        smp_num = int(len(sts) * ratio)
        print("使うデータ数：%d" % smp_num)
        st_subset += random.sample(list(sts), smp_num)
    fnamew = SUBSET_PATH_FORMAT.format(act_num)
    print("部分集合のサイズ：%d" % len(st_subset))
    # シャッフルを追加 (なんとなく)
    random.shuffle(st_subset)
    # 集合にして保存
    rubik_win.writeAndBackup(fnamew, set(st_subset))
    print("%02d:%02d:%02d" % rubik_win.s2hms(time.time() - t0))

def sampleAct10():
    """
    10手状態のサンプルファイルを作成したい.
    9手状態から1手で到達できる状態を計算し, 既知の状態を除外する.
    8, 9手状態だけ除外すれば問題ない??
    """
    t0 = time.time()
    act10_subset = []
    for i in range(rubik_win.LOOP_MAX):
        fnamer = rubik_win.SN_PATH_FORMAT.format(9, i)
        sts = readPickleFile(fnamer)
        if sts is None:
            break
        print(fnamer + "からロード")
        smp_num = len(sts) // 10000
        print("次の状態を計算するデータ数：%d" % smp_num)
        sts = random.sample(list(sts), smp_num)
        # 10手状態の候補を計算
        for st_num in sts:
            act10_subset += rubik_win.applyAllMovesNormal(st_num)
    print("重複排除前状態数：%d" % len(act10_subset))
    # 重複排除
    act10_subset = set(act10_subset)
    for i in range(10):
        for j in range(rubik_win.LOOP_MAX):
            fnamer = rubik_win.SN_PATH_FORMAT.format(i, j)
            sts = readPickleFile(fnamer)
            if sts is None:
                break
            print(fnamer + "との重複排除")
            act10_subset -= sts
            print("暫定状態数：%d" % len(act10_subset))
    print("10手サンプル数：%d" % len(act10_subset))
    fnamew = SUBSET_PATH_FORMAT.format(10)
    rubik_win.writeAndBackup(fnamew, act10_subset)
    print("%02d:%02d:%02d" % rubik_win.s2hms(time.time() - t0))

def createSampleNpFile(act_num, binary=False):
    """
    サンプル集合からnp配列に変換.
    """
    t0 = time.time()
    fnamer = SUBSET_PATH_FORMAT.format(act_num)
    print(fnamer + "からnp配列を作成")
    sts = readPickleFile(fnamer)
    if sts is None:
        return
    if binary:
        arr = set2nparrayBin(sts)
        fnamew = BIN_SUBSET_NP_PATH_FORMAT.format(act_num)
    else:
        arr = rubik_win.set2nparray(sts)
        fnamew = SUBSET_NP_PATH_FORMAT.format(act_num)
    print(fnamew + "に書き込み")
    print(arr.shape)
    print(arr)
    np.save(fnamew, arr)
    print("%02d:%02d:%02d" % rubik_win.s2hms(time.time() - t0))

def checkSetSize(depth=7):
    """
    集合サイズ確認.
    """
    for i in range(depth + 1):
        set_siz = 0
        for j in range(rubik_win.LOOP_MAX):
            fnamer = rubik_win.SN_PATH_FORMAT.format(i, j)
            sts = readPickleFile(fnamer)
            if sts is None:
                break
            set_siz += len(sts)
            # print(fnamer)
        print(f"{i}手状態数：{set_siz}")

def createNpz(binary=False):
    """
    npzファイルを作成.
    7手以降は用意されている部分集合から作成.
    それぞれ最大10万とする.
    """
    for i in range(11):
        t1 = time.time()
        if i < 7:
            fnamer = rubik_win.SN_PATH_FORMAT.format(i, 0)
        else:
            fnamer = SUBSET_PATH_FORMAT.format(i)
        sts = readPickleFile(fnamer)
        if sts is None:
            break
        print(fnamer)
        if len(sts) > 100000:
            sts = random.sample(list(sts), 100000)
        else:
            sts = list(sts)
            random.shuffle(sts)
        len_all = len(sts)
        len_test = len_all // 7
        print(f"訓練用データ数：{len_all - len_test}, テスト用データ数：{len_test}")
        test_sts = set(sts[:len_test])
        train_sts = set(sts) - test_sts
        # ワンホット
        if binary:
            test_arr = set2nparrayBin(test_sts)
            train_arr = set2nparrayBin(train_sts)
            fnamew = ONEHOT_TT_NPZ_PATH_FORMAT.format(i)
        else:
            test_arr = rubik_win.set2nparray(test_sts)
            train_arr = rubik_win.set2nparray(train_sts)
            fnamew = TT_NPZ_PATH_FORMAT.format(i)
        print(f"{fnamew}を作成.")
        np.savez_compressed(fnamew, train=train_arr, test=test_arr)
        print("%02d:%02d:%02d" % rubik_win.s2hms(time.time() - t1))
    
def mergeSampleFiles16(fnamer1: str):
    """
    各PCで作ったサンプルファイルの統合.
    最大16手判定を前提.
    """
    keys = [i for i in range(10, 17)] + ["gt16"]
    fnamer1 = SMP_DIR_PATH + fnamer1
    smp_dic1 = readPickleFile(fnamer1)
    if smp_dic1 is None:
        print(f"{fnamer1}が存在しません.")
        return
    fnamer2 = MERGED_SMP_PATH
    smp_dic2 = readPickleFile(fnamer2)
    if smp_dic2 is None:
        print("None")
        with open(MERGED_SMP_PATH, "wb") as f:
            pickle.dump(None, f)
        fnamer2 = SMP_PATH_FORMAT.format(16)
        smp_dic2 = readPickleFile(fnamer2)
    smp_dic3 = {}
    print(f"結合するファイル：\n{fnamer1}\n{fnamer2}")
    fnamew = MERGED_SMP_PATH
    print(f"書き込み先：\n{fnamew}")
    for i in keys:
        smp1 = smp_dic1[i]
        smp2 = smp_dic2[i]
        smp3 = smp1 | smp2
        print(i, len(smp1), len(smp2), len(smp3))
        smp_dic3[i] = smp3
    writeAndBackup(fnamew, smp_dic3)

if __name__ == "__main__":
    # mergeSampleFiles16("sample016_sonoda_desktop.pickle")
    mergeSampleFiles16("sample016_asahi_server.pickle")
    pass
