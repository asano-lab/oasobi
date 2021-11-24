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
    
}

const solved = new State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);

// 完成状態からRを適用したときの状態
const r_state = new State(
    [0, 2, 6, 3, 4, 1, 5, 7],
    [0, 1, 2, 0, 0, 2, 1, 0],
    [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);

// 完成状態からLを適用したときの状態
const l_state = new State(
    [4, 1, 2, 0, 7, 5, 6, 3],
    [2, 0, 0, 1, 1, 0, 0, 2],
    [11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
)

// 完成状態からUを適用したときの状態
const u_state = new State(

)

// console.log(solved);
console.log(l_state);

