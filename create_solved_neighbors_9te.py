#!/usr/bin/python3
import time
import os
import pickle
import json
from rubik_module import (
    solved, DIR_PATH, SN_PATH_FORMAT, applyAllMovesNormal,
    ST_LEN_MAX, s2hms, LOOP_MAX
)

def _createSolvedNeighborsFile(max_depth=9):
    """
    完成状態近傍ファイルを作成する関数.
    """
    t0 = time.time()
    searching = DIR_PATH + "searching.json"
    act_num = 0
    sub_num = 0

    if not os.path.isdir(DIR_PATH):
        os.mkdir(DIR_PATH)
        print("ディレクトリ%sを作成" % DIR_PATH)
    # まだ何も作られていない
    # 最初のファイルを作成し, 深さ1の探索も行う
    if not os.path.exists(searching):
        fnamew = SN_PATH_FORMAT.format(0, 0)
        with open(fnamew, "wb") as f:
            # 多分無意味だが一応正規化
            st_num = solved.toNumNormal()
            # 要素が1つだけの集合をファイルに書き込む
            pickle.dump(set([st_num]), f)
        fnamer = fnamew
    # ファイルが存在する
    else:
        # 探索済みファイルを読み出し
        with open(searching, "r") as f:
            act_num, sub_num = json.load(f)

        # 副番号をインクリメントしてファイルの存在を確認
        sub_num += 1
        fnamer = SN_PATH_FORMAT.format(act_num, sub_num)
        # 存在しない (この深さの盤面はすべて探索済み)
        if not os.path.exists(fnamer):
            # 次の深さの最初のファイルを指定
            act_num += 1
            # 最大深さ-1までの探索で終了
            if act_num >= max_depth:
                print(f"全{max_depth}手状態を発見")
                return True
            # 副番号はリセット
            sub_num = 0
            fnamer = SN_PATH_FORMAT.format(act_num, sub_num)

    print(fnamer, "から次の状態を計算")
    # ロード
    with open(fnamer, "rb") as f:
        prev_st_nums = pickle.load(f)
    print("探索状態数：{:d}".format(len(prev_st_nums)))

    # 次の状態を計算
    next_st_nums = []
    while prev_st_nums:
        st_num = prev_st_nums.pop()
        next_st_nums += applyAllMovesNormal(st_num)

    # 探索情報を更新
    with open(searching, "w") as f:
        json.dump([act_num, sub_num], f)

    print("新状態数 (重複排除前)：{:d}".format(len(next_st_nums)))

    # 集合に変換
    next_st_nums = set(next_st_nums)
    # なんとなく初期化
    known_st_nums = set()
    latest_act_num = 0
    latest_sub_num = 0

    # 探索済み状態との重複を削除
    for i in range(act_num + 2):
        j = 0
        past_fname = SN_PATH_FORMAT.format(i, j)
        while os.path.exists(past_fname):
            with open(past_fname, "rb") as f:
                # ループ終了時, 最新ファイルの状態が格納される
                known_st_nums = pickle.load(f)
            next_st_nums -= known_st_nums
            # 最新ファイル名更新
            latest_fname = past_fname
            latest_act_num = i
            latest_sub_num = j
            j += 1
            past_fname = SN_PATH_FORMAT.format(i, j)
    
    # リストに変換
    next_st_nums = list(next_st_nums)
    print("新状態数 (重複排除後)：{:d}".format(len(next_st_nums)))

    # 全探索終了 (ルービックキューブでは無理)
    if not next_st_nums:
        return True

    # 深さ更新
    if latest_act_num == act_num:
        latest_act_num += 1
        latest_sub_num = 0
        latest_fname = SN_PATH_FORMAT.format(latest_act_num, latest_sub_num)
    # 更新しない場合, 最新ファイルの状態と足す
    else:
        next_st_nums = list(known_st_nums) + next_st_nums

    # 分割してファイルに保存
    while len(next_st_nums) > ST_LEN_MAX:
        with open(latest_fname, "wb") as f:
            pickle.dump(set(next_st_nums[:ST_LEN_MAX]), f)
        # 分割した残り
        next_st_nums = next_st_nums[ST_LEN_MAX:]
        # 最新番号の更新
        latest_sub_num += 1
        latest_fname = SN_PATH_FORMAT.format(latest_act_num, latest_sub_num)
    if next_st_nums:
        with open(latest_fname, "wb") as f:
            pickle.dump(set(next_st_nums), f)
    print("%02d:%02d:%02d" % s2hms(time.time() - t0))
    return False

def createSolvedNeighborsFile():
    t0 = time.time()
    for _ in range(LOOP_MAX):
        if _createSolvedNeighborsFile(6):
            break
    print("%02d:%02d:%02d" % s2hms(time.time() - t0))

if __name__ == "__main__":
    createSolvedNeighborsFile()
