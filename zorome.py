import re

def main():
    moji = input("日付を入力してください (MM/DD): ")
    m = re.match(r"(\d*)/(\d*)$", moji)
    if m is None:
        return
    print(m.groups())

if __name__ == "__main__":
    main()
