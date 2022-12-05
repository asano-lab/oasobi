NUM_TO_WORD_2DIG = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
    30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}


TMB = ["", "thousand", "million", "billion"]

# n = float(input())
n = 123456789.5
n = 123065011

# 整数部
n_int = int(n)
print(n_int)
moji = ""
for i, j in enumerate(TMB):
    moji_3dig = ""
    n_3dig = (n_int // (1000 ** i)) % 1000
    n_hand = n_3dig // 100
    if n_hand != 0:
        moji_3dig += NUM_TO_WORD_2DIG[n_hand] + " handred "
    n_2dig = n_3dig % 100
    if n_2dig in NUM_TO_WORD_2DIG:
        if n_2dig != 0:
            moji_3dig += NUM_TO_WORD_2DIG[n_2dig]
    else:
        n_1dig = n_2dig % 10
        moji_3dig += NUM_TO_WORD_2DIG[n_2dig - n_1dig] + " "
        moji_3dig += NUM_TO_WORD_2DIG[n_1dig]
    print(moji_3dig)
