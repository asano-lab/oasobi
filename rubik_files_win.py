import os
import pickle
import os
import random
import rubik_win

SUBSET_PATH_FORMAT = rubik_win.SMP_DIR_PATH + "subset_act{:03d}.pickle"

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
    for i in range(rubik_win.LOOP_MAX):
        fnamer = rubik_win.SN_PATH_FORMAT.format(9, i)
        sts = readPickleFile(fnamer)
        if sts is None:
            break
        smp_num = len(sts) // 1000
        print("使うデータ数：%d" % smp_num)
    print(rubik_win.SN_PATH_FORMAT.format(9, 1))
    # print(rubik_win.SMP_DIR_PATH)
    print(SUBSET_PATH_FORMAT.format(1))
    pass

if __name__ == "__main__":
    a = {1, 2, 3, 4, 5}
    print(random.sample(list(a), 5))
    print(a)
    # sampleAct9()
    pass
