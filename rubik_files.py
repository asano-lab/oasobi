# !/usr/bin/python3

import time
import random
from rubik_module import (
    SMP_DIR_PATH, SOLVED_NEIGHBOR_DEPTH_MAX, readPickleFile, s2hms,
    num2state, Search
)

def checkSampleSetSize(fnamer: str):
    """
    サンプル数チェック.
    """
    keys = [i for i in range(10, 17)] + ["gt16"]
    fnamer = SMP_DIR_PATH + fnamer
    smp_dic = readPickleFile(fnamer)
    if smp_dic is None:
        print(f"{fnamer}が存在しません.")
        return
    for i in keys:
        if type(i) is int:
            print("{:4d}".format(i), end=": ")
        else:
            print("{:s}".format(i), end=": ")
        print(len(smp_dic[i]))

def sampleFileTest(fnamer: str, n: int):
    """
    集めたサンプルが指定した手数になっているかチェック.
    ファイル名指定制に変更.
    """
    # 読み込みファイルは固定
    t0 = time.time()
    # fnamer = MERGED_SMP_PATH
    fnamer = SMP_DIR_PATH + fnamer
    smp_dic = readPickleFile(fnamer)
    if smp_dic is None:
        print(f"{fnamer}が存在しません.")
        return
    print(f"{fnamer}をロード")
    for k, v in smp_dic.items():
        smp_len = len(v)
        if type(k) is int:
            print("%2d手サンプル数　　：%d" % (k, smp_len))
        else:
            print("%2d手以上サンプル数：%d" % (17, smp_len))
    if n < 10 or 16 < n:
        key = "gt16"
        print("17手以上サンプル")
    else:
        key = n
        print(f"{key}手サンプル")
    stn = random.choice(list(smp_dic[key]))
    st = num2state(stn)
    del smp_dic
    try:
        print(st)
        srch = Search(st, SOLVED_NEIGHBOR_DEPTH_MAX)
        dist = srch.searchWithDat2(7)
        if dist >= 0:
            print("最短%2d手：" % dist, end="")
            mvs = srch.getSolveMovesWithDat()
            for mv in mvs:
                print(mv, end=" ")
            print()
            route = srch.getRoute()
            print(route)
        else:
            print("%2d手以上" % (17))
    except KeyboardInterrupt:
        print("強制終了")
    print("総計算時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))

if __name__ == "__main__":
    # checkSampleSetSize("sample_merged_20211224_200000.pickle")
    # checkSampleSetSize("sample_ipmsb-gs_20211224_200000.pickle")
    # checkSampleSetSize("sample100_z370_20211227_142520.pickle")
    sampleFileTest("sample_ipmsb-gs_20211224_200000.pickle", 100)
    pass
