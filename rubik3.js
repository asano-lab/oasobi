// ルービックキューブの状態を表すクラス
class State {
    constructor(cp, co, ep, eo) {
        this.cp = cp;
        this.co = co;
        this.ep = ep;
        this.eo = eo;
    }
}

s = new State(0, 1, 2, 3);
console.log(s);
