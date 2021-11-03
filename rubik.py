# ルービックキューブソルバを作りたい

import os
import pickle
import time
import json

class Rubik():
    complete = [
        [
            [ 0,  1,  2],
            [ 7, 24,  3],
            [ 6,  5,  4]
        ], [
            [ 8,  9, 10],
            [15, 25, 11],
            [14, 13, 12]
        ], [
            [16, 17, 18],
            [23, 26, 19],
            [22, 21, 20]
        ]
    ]

    # 動かないマス
    # キーが添え字のタプルで値が数値
    immovable = {
        (0, 1, 1): 24,
        (1, 0, 1):  9,
        (1, 1, 0): 15,
        (1, 1, 1): 25,
        (1, 1, 2): 11,
        (1, 2, 1): 13,
        (2, 1, 1): 26
    }

    pos_avail = (0, 2)

    # cnt_max = 1000000
    cnt_max = 500000 # メモリが心配なので少し減らす

    def __init__(self) -> None:
        pass
    
    # 3次元リストを数値に変換 (100bit)
    def lll2num(self, lll: list) -> int:
        n = 0
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    p = lll[i][j][k]
                    if p not in self.immovable.values():
                        n = (n << 5) | p
        return n
    
    def num2lll(self, n: int) -> list:
        lll = [[[0 for i in range(3)] for j in range(3)] for k in range(3)]
        for i in range(2, -1, -1):
            for j in range(2, -1, -1):
                for k in range(2, -1, -1):
                    if (i, j, k) in self.immovable:
                        lll[i][j][k] = self.immovable[(i, j, k)]
                    else:
                        lll[i][j][k] = n & 0b11111
                        n >>= 5
        return lll
    
    # 3次元リストのコピー
    def lllCopy(self, lll: list) -> list:
        lcp = [[] for i in range(3)]
        for i, j in enumerate(lll):
            for k in j:
                lcp[i].append(k.copy())
        return lcp

    # 下方向に90deg回転
    # 第2引数には回転させる位置を与える
    # 0: left, 2: right
    # とりあえず真ん中は1ステップで動かせないものとする
    # 軸に対して右ねじの向きをプラスにした
    def rollPlus(self, cube: list, x: int) -> list:
        if x not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][0][x] = cube[2][0][x]
        n_cube[2][0][x] = cube[2][2][x]
        n_cube[2][2][x] = cube[0][2][x]
        n_cube[0][2][x] = cube[0][0][x]
        n_cube[0][1][x] = cube[1][0][x]
        n_cube[1][0][x] = cube[2][1][x]
        n_cube[2][1][x] = cube[1][2][x]
        n_cube[1][2][x] = cube[0][1][x]
        return n_cube
    
    # 上方向に90deg回転
    # 0: left, 2: right
    def rollMinus(self, cube: list, x: int) -> list:
        if x not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][0][x] = cube[0][2][x]
        n_cube[0][2][x] = cube[2][2][x]
        n_cube[2][2][x] = cube[2][0][x]
        n_cube[2][0][x] = cube[0][0][x]
        n_cube[0][1][x] = cube[1][2][x]
        n_cube[1][2][x] = cube[2][1][x]
        n_cube[2][1][x] = cube[1][0][x]
        n_cube[1][0][x] = cube[0][1][x]
        return n_cube
    
    # y軸周りに回転 (順)
    # 0: back, 2: front
    def pitchPlus(self, cube: list, y: int) -> list:
        if y not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][y][0] = cube[0][y][2]
        n_cube[0][y][2] = cube[2][y][2]
        n_cube[2][y][2] = cube[2][y][0]
        n_cube[2][y][0] = cube[0][y][0]
        n_cube[0][y][1] = cube[1][y][2]
        n_cube[1][y][2] = cube[2][y][1]
        n_cube[2][y][1] = cube[1][y][0]
        n_cube[1][y][0] = cube[0][y][1]
        return n_cube
    
    # y軸周りに回転 (逆)
    # 0: back, 2: front
    def pitchMinus(self, cube: list, y: int) -> list:
        if y not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[0][y][0] = cube[2][y][0]
        n_cube[2][y][0] = cube[2][y][2]
        n_cube[2][y][2] = cube[0][y][2]
        n_cube[0][y][2] = cube[0][y][0]
        n_cube[0][y][1] = cube[1][y][0]
        n_cube[1][y][0] = cube[2][y][1]
        n_cube[2][y][1] = cube[1][y][2]
        n_cube[1][y][2] = cube[0][y][1]
        return n_cube
    
    # z軸周りに回転 (順)
    # 0: top, 2: bottom
    def yawPlus(self, cube: list, z: int) -> list:
        if z not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[z][0][0] = cube[z][2][0]
        n_cube[z][2][0] = cube[z][2][2]
        n_cube[z][2][2] = cube[z][0][2]
        n_cube[z][0][2] = cube[z][0][0]
        n_cube[z][0][1] = cube[z][1][0]
        n_cube[z][1][0] = cube[z][2][1]
        n_cube[z][2][1] = cube[z][1][2]
        n_cube[z][1][2] = cube[z][0][1]
        return n_cube

    # z軸周りに回転 (逆)
    # 0: top, 2: bottom
    def yawMinus(self, cube: list, z: int) -> list:
        if z not in self.pos_avail:
            print("無効な引数です")
            return []
        n_cube = self.lllCopy(cube)
        n_cube[z][0][0] = cube[z][0][2]
        n_cube[z][0][2] = cube[z][2][2]
        n_cube[z][2][2] = cube[z][2][0]
        n_cube[z][2][0] = cube[z][0][0]
        n_cube[z][0][1] = cube[z][1][2]
        n_cube[z][1][2] = cube[z][2][1]
        n_cube[z][2][1] = cube[z][1][0]
        n_cube[z][1][0] = cube[z][0][1]
        return n_cube
    
    # キューブの数値のリストを与えると, 次のキューブの数値の集合を返す
    def allActions(self, cube_num_list: list) -> list:
        next_cube_num_list = []

        # ループの上限を追加
        for i in range(self.cnt_max):
            # 空になったら終了
            if not cube_num_list:
                break

            # ポップしてデコード
            lll = self.num2lll(cube_num_list.pop())

            # 各キューブで12種類の動作を行う
            for pos in self.pos_avail:
                # エンコードしてリストに追加
                next_cube_num_list.append(self.lll2num(self.rollPlus(lll, pos)))
                next_cube_num_list.append(self.lll2num(self.rollMinus(lll, pos)))
                next_cube_num_list.append(self.lll2num(self.pitchPlus(lll, pos)))
                next_cube_num_list.append(self.lll2num(self.pitchMinus(lll, pos)))
                next_cube_num_list.append(self.lll2num(self.yawPlus(lll, pos)))
                next_cube_num_list.append(self.lll2num(self.yawMinus(lll, pos))) 
        
        return next_cube_num_list
    
    # 幅優先探索
    def bfs(self, dir_path: str) -> bool:
        searched = dir_path + "searched.json"
        path_format = dir_path + "act{:02d}_{:02d}.pickle"
        act_num = 0
        sub_num = 0

        # まだ何も作られていない
        # 最初のファイルを作成し, 深さ1の探索も行う
        if not os.path.exists(searched):
            fnamew = path_format.format(0, 0)
            cube_num = self.lll2num(self.complete)
            f = open(fnamew, "wb")
            # 要素が1つだけのリストを作成
            pickle.dump([cube_num], f)
            f.close()

            fnamer = fnamew
        # ファイルが存在する
        else:
            # 探索済みファイルを探す
            f = open(searched, "r")
            act_num, sub_num = json.load(f)
            f.close()

            # 副番号をインクリメントしてファイルの存在を確認
            sub_num += 1
            fnamer = path_format.format(act_num + 1, sub_num)

            # 存在しない (この深さの盤面はすべて探索済み)
            if not os.path.exists(fnamer):
                # 次の深さの最初のファイルを指定
                act_num += 1
                sub_num = 0
                fnamer = path_format.format(act_num, sub_num)

        # 余りファイルの有無をチェック
        rem_fname = dir_path + "act{:02d}_{:02d}rem.pickle".format(act_num, sub_num)
        if os.path.exists(rem_fname):
            # 存在したらそのファイルを指定
            fnamer = rem_fname

        print(fnamer, "から次の状態を計算")

        # ロード
        f = open(fnamer, "rb")
        prev_cubes = pickle.load(f)
        f.close()

        print("探索状態数：", len(prev_cubes))
        # 次の状態を計算
        cubes = self.allActions(prev_cubes)
        # すべて探索しきれなかった場合, 余りファイルに保存
        print("未探索状態数：", len(prev_cubes))
        if prev_cubes:
            f = open(rem_fname, "wb")
            pickle.dump(prev_cubes, f)
            f.close()
        # すべて探索しきった
        else:
            # 探索済みを更新
            f = open(searched, "w")
            json.dump([act_num, sub_num], f)
            f.close()

            # 余りファイルがあったら削除
            if os.path.exists(rem_fname):
                os.remove(rem_fname)
        
        del prev_cubes

        print("新状態数 (重複排除前)：", len(cubes))

        # 集合に変換
        cubes = set(cubes)
        # なんとなく初期化
        known_cubes = []
        latest_act_num = 0
        latest_sub_num = 0

        # 探索済み状態との重複を削除
        for i in range(act_num + 2):
            j = 0
            past_fname = path_format.format(i, j)
            if os.path.exists(past_fname):
                f = open(past_fname, "rb")
                known_cubes = pickle.load(f)
                f.close()
                cubes -= set(known_cubes)

                latest_fname = past_fname
                latest_act_num = i
                latest_sub_num = j
                j += 1
        
        # リストに変換
        cubes = list(cubes)
        print("新状態数 (重複排除後)", len(cubes), "個")

        # 深さが進む場合
        fnamew = path_format.format(act_num + 1, 0)

        # 最新のファイルの深さが, 探索済み深さ+1と一致する
        if latest_act_num == act_num + 1:
            # 直前の状態数と, 新状態数の和が1000万以下なら, 新しいファイルは作らない
            if len(known_cubes) + len(cubes) <= self.cnt_max * 10:
                cubes += known_cubes
                fnamew = latest_fname
                print("ファイル結合")
            # 状態数が多すぎた場合は新ファイル作成
            else:
                fnamew = path_format.format(latest_act_num, latest_sub_num + 1)
        # これ以上状態が増えない場合
        elif not cubes:
            print("探索終了")
            return True

        # リストにして保存
        f = open(fnamew, "wb")
        pickle.dump(cubes, f)
        f.close()
        
        return False
        

def main() -> None:
    r = Rubik()

    for i in range(8):
        t0 = time.time()
        end = r.bfs("./rubik_dat/")
        # end = r.bfs("./test_dir/")
        print(time.time() - t0, "秒")
        if end:
            break
    

if __name__ == "__main__":
    main()
