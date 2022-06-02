import urllib.parse
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="パーセントエンコーディング")
    parser.add_argument("string", help="変換したい文字列")
    args = parser.parse_args()

    print(urllib.parse.quote(args.string, safe=""))
