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

    byteData() {
        let i;
        let c_bin = 0;
        let e_bin = 0;
        let byte_arr = [];
        for (i = 0; i < 8; i++) {
            c_bin = (c_bin << 3) | this.cp[i];
            c_bin = (c_bin << 2) | this.co[i];
        }
        for (i = 0; i < 12; i++) {
            e_bin = (e_bin << 4) | this.ep[i];
            e_bin = (e_bin << 1) | this.eo[i];
        }
        for (i = 0; i < 5; i++) {
            byte_arr.push(c_bin & 0xff);
            c_bin >>>= 8;
        }
        for (i = 0; i < 8; i++) {
            byte_arr.push(e_bin & 0xff);
            e_bin >>>= 8;
        }
        return Buffer.from(byte_arr);
    }
}

function byte2state(buf) {
    
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

const faces = Object.keys(moves);
for (const face_name of faces) {
    moves[face_name + "2"] = moves[face_name].add(moves[face_name]);
    moves[face_name + "'"] = moves[face_name + "2"].add(moves[face_name]);
}

scramble = [
    "L", "D2", "R", "U2", "L", "F2", "U2",
    "L", "F2", "R2", "B2", "R", "U'", "R'",
    "U2", "F2", "R'", "D", "B'", "F2"
]
let scrambled_state = solved;
for (const m of scramble) {
    scrambled_state = scrambled_state.add(moves[m]);
}
console.log(scrambled_state);

const fs = require("fs");

const options = {
    flag: "a"
};

// const data = Buffer.from([0x62, 0x75, 0x66, 0x66, 0x65, 0x72, 0x0a]);
// const data = Buffer.from(scrambled_state);
// const data = "H\n";

// const arr = [1, 2, 3, 4, 5];
console.log(scrambled_state.byteData());

fs.writeFile("file1.txt", scrambled_state, options, (err) => {
    if (err) throw err;
    console.log("正常に書き込みが完了しました");
});
