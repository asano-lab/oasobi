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

// 完成状態からRをしたときの状態
const r_state = new State(
    [0, 2, 6, 3, 4, 1, 5, 7],
    [0, 1, 2, 0, 0, 2, 1, 0],
    [0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
);

// console.log(solved);
console.log(r_state);

a = [1, 2];
b = [3, 4];
a = a.concat(b);
console.log(a);
