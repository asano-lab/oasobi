// ルービックキューブの状態を表すクラス
class State {
    constructor(cp, co, ep, eo) {
        this.cp = cp;
        this.co = co;
        this.ep = ep;
        this.eo = eo;
    }
}

solved = new State(
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
)

console.log(solved);
