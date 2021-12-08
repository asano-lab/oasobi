import pickle
import rubik_win

SUBSET_PATH_FORMAT = rubik_win.SMP_DIR_PATH + "subset_act{:03d}.pickle"

def sampleAct9():
    """
    9手状態のデータ数が多すぎるのでランダム抽出したい
    """
    print(rubik_win.SN_PATH_FORMAT.format(9, 1))
    # print(rubik_win.SMP_DIR_PATH)
    print(SUBSET_PATH_FORMAT.format(1))
    pass

if __name__ == "__main__":
    sampleAct9()
