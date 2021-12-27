from rubik_module import SMP_DIR_PATH, readPickleFile

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

if __name__ == "__main__":
    checkSampleSetSize("sample_merged_20211224_200000.pickle")
