// ルービックキューブの状態を表すクラス
class State {
    constructor(cp, co, ep, eo) {
        // corner permutation
        this.cp = cp;
        // corner orientation
        this.co = co;
        // edge permutation
        this.ep = ep;
        // edge orientation
        this.eo = eo;
    }
    // 操作を適用
    add(s) {
        let i;
        let ncp = [];
        let nco = [];
        let nep = [];
        let neo = [];
        for (i = 0; i < 8; i++) {
            ncp.push(this.cp[s.cp[i]]);
            nco.push((this.co[s.cp[i]] + s.co[i]) % 3);
        }
        for (i = 0; i < 12; i++) {
            nep.push(this.ep[s.ep[i]]);
            neo.push(this.eo[s.ep[i]] ^ s.eo[i]);
        }
        return new State(ncp, nco, nep, neo)
    }
}

const solved = new State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);

let moves = {
    // 完成状態からUを適用したときの状態
    "U": new State(
        [3, 0, 1, 2, 4, 5, 6, 7],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    // 完成状態からDを適用したときの状態
    "D": new State(
        [0, 1, 2, 3, 5, 6, 7, 4],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    // 完成状態からLを適用したときの状態
    "L": new State(
        [4, 1, 2, 0, 7, 5, 6, 3],
        [2, 0, 0, 1, 1, 0, 0, 2],
        [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    // 完成状態からRを適用したときの状態
    "R": new State(
        [0, 2, 6, 3, 4, 1, 5, 7],
        [0, 1, 2, 0, 0, 2, 1, 0],
        [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ),
    // 完成状態からFを適用したときの状態
    "F": new State(
        [0, 1, 3, 7, 4, 5, 2, 6],
        [0, 0, 1, 2, 0, 0, 2, 1],
        [0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]
    ),
    // 完成状態からBを適用したときの状態
    "B": new State(
        [1, 5, 2, 3, 0, 4, 6, 7],
        [1, 2, 0, 0, 2, 1, 0, 0],
        [4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
        [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    )
};

// console.log(solved);
// console.log(solved.add(moves["B"]).add(moves["B"]));
faces = Object.keys(moves);
console.log(faces);
