import re

NUM_TO_WORD_2DIG = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

TMB = ["", "thousand", "million", "billion"]


def main():
    n_str = input()
    # n_str = "317473891017.364289"
    # n_str = "189"
    # n_str = "300.3819"
    # n_str = "1348910.18391"
    try:
        n_int = int(n_str)
        n_dec = None
    except ValueError:
        m = re.match(r'(\d+)\.(\d+)', n_str)
        if m is None:
            return
        mg = m.groups()
        n_int = int(mg[0])
        n_dec = mg[1]
    # 整数部
    # print(n_int)
    moji = ""
    for i, j in enumerate(TMB):
        n_3dig = (n_int // (1000 ** i)) % 1000
        if n_3dig == 0:
            continue
        moji_3dig = ""
        n_hand = n_3dig // 100
        if n_hand != 0:
            moji_3dig += NUM_TO_WORD_2DIG[n_hand] + " handred"
        n_2dig = n_3dig % 100
        if n_2dig != 0:
            if n_hand != 0:
                moji_3dig += " "
            if n_2dig in NUM_TO_WORD_2DIG:
                if n_2dig != 0:
                    moji_3dig += NUM_TO_WORD_2DIG[n_2dig]
            else:
                n_1dig = n_2dig % 10
                moji_3dig += NUM_TO_WORD_2DIG[n_2dig - n_1dig] + " "
                moji_3dig += NUM_TO_WORD_2DIG[n_1dig]
        if j:
            if moji:
                moji = moji_3dig + " " + j + " " + moji
            else:
                moji = moji_3dig + " " + j
        else:
            moji = moji_3dig
    # print(moji)

    # 小数部
    if n_dec:
        moji += " point"
        for i in n_dec:
            moji += " " + NUM_TO_WORD_2DIG[int(i)]
    print(moji)


if __name__ == "__main__":
    main()
