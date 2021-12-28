import time
import socket
import os
import pickle
import sys
from rubik_module import (
    SOLVED_NEIGHBOR_DEPTH_MAX, SMP_PATH_FORMAT_ID,
    SMP_DIR_PATH, VERBOSE, LOG_PATH, LOG_DIR_PATH,
    writeAndBackup, printLog,
    randomScramble, randomScrambleDependent,
    inputState, s2hms, Search
)

def collectSamples(loop, tnd, mode=0, shuffle_num=20):
    """
    サンプル収集用関数.
    ファイル名をホスト名から取得.
    """
    t0 = time.time()
    dist_max = SOLVED_NEIGHBOR_DEPTH_MAX + tnd
    fnamew = SMP_PATH_FORMAT_ID.format(dist_max, socket.gethostname())
    gt_key = "gt%d" % dist_max
    # パスが存在しない場合は初期化
    if not os.path.exists(fnamew):
        if not os.path.isdir(SMP_DIR_PATH):
            os.mkdir(SMP_DIR_PATH)
            print("ディレクトリ%sを作成" % SMP_DIR_PATH)
        smp_dic = {dist_max - i: set() for i in range(tnd)}
        smp_dic[gt_key] = set()
        print(fnamew + "を作成")
        writeAndBackup(fnamew, smp_dic)
    with open(fnamew, "rb") as f:
        smp_dic = pickle.load(f)
    # 最初のサンプル数も保存
    len_dic = {}
    printLog("過去のサンプル数")
    for k, v in smp_dic.items():
        len_dic[k] = len(v)
        if type(k) is int:
            printLog("%2d手サンプル数：%d" % (k, len_dic[k]))
        else:
            printLog("%2d手以上サンプル数：%d" % (dist_max + 1, len_dic[k]))
    try:
        for i in range(loop):
            printLog(f"{i + 1}ループ目")
            if mode == 0:
                printLog("通常スクランブル%d手：" % shuffle_num, end="")
                sst = randomScramble(shuffle_num)
            elif mode == 1:
                printLog("冗長排除スクランブル%d手：" % shuffle_num, end="")
                sst = randomScrambleDependent(shuffle_num)
            else:
                printLog("手入力")
                sst = inputState()
                if sst is None:
                    break
            printLog(sst)
            srch = Search(sst, SOLVED_NEIGHBOR_DEPTH_MAX)
            # dist = srch.searchWithDat(tnd)
            dist = srch.searchWithDat2(tnd)
            if dist >= 0:
                printLog("最短%2d手：" % dist, end="")
                mvs = srch.getSolveMovesWithDat()
                for mv in mvs:
                    printLog(mv, end=" ")
                printLog()
                route = srch.getRoute()
                for j in range(dist - SOLVED_NEIGHBOR_DEPTH_MAX):
                    smp_dic[dist - j].add(route[j])
            else:
                printLog("%2d手以上" % (dist_max + 1))
                smp_dic[gt_key].add(sst.toNumNormal())
            for k, v in smp_dic.items():
                smp_len = len(v)
                smp_inc = smp_len - len_dic[k]
                if type(k) is int:
                    printLog("%2d手サンプル数：%d (+%d)" % (k, smp_len, smp_inc))
                else:
                    printLog("%2d手以上サンプル数：%d (+%d)" % (dist_max + 1, smp_len, smp_inc))
            writeAndBackup(fnamew, smp_dic)
            printLog("経過時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))
    except KeyboardInterrupt:
        printLog("強制終了")
    finally:
        printLog("総計算時間：%02d時間%02d分%02d秒" % s2hms(time.time() - t0))

def main():
    global VERBOSE, LOG_PATH
    try:
        VERBOSE = int(sys.argv[1])
    except ValueError:
        VERBOSE = 1
    except IndexError:
        VERBOSE = 1
    try:
        LOG_PATH = LOG_DIR_PATH + sys.argv[2]
    except IndexError:
        LOG_PATH = None
    if LOG_PATH is not None:
        if not os.path.exists(LOG_PATH):
            try:
                with open(LOG_PATH, "w") as f:
                    print(f"「{LOG_PATH}」を作成.")
            except FileNotFoundError:
                print(f"「{LOG_PATH}」の作成失敗.")
                return
    # collectSamples(1000, 7, 0, 100)
    collectSamples(1000, 7, 1, 16)

if __name__ == "__main__":
    VERBOSE = 0
    printLog("abc")
    pass
