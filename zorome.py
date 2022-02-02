import re

if __name__ == "__main__":
    moji = input("日付を入力してください (MM/DD): ")
    m = re.match(r"\d*/\d*$", moji)
    print(m)
    pass