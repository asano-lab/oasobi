import re

def main():
    moji = input("日付を入力してください (MM/DD): ")
    m = re.match(r"(\d*)/(\d*)$", moji)
    if m is None:
        return
    month = int(m.groups()[0])
    if month < 1 or 12 < month:
        return
    date = int(m.groups()[1])
    if date < 1 or 31 < date:
        return
    print(month, date)

if __name__ == "__main__":
    main()
