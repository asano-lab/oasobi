// 参考：https://sbfl.net/blog/2017/06/01/javascript-reproducible-random/
class Random {
    constructor(seed = 88675123) {
        this.x = 123456789;
        this.y = 362436069;
        this.z = 521288629;
        this.w = seed;
    }

    // XorShift
    next() {
        const t = this.x ^ (this.x << 11);
        this.x = this.y;
        this.y = this.z;
        this.z = this.w;
        return this.w = (this.w ^ (this.w >>> 19)) ^ (t ^ (t >>> 8)); 
    }
}

class RandomMT {
    constructor(seed = 123) {
        // MT19937
        Object.defineProperty(this, "W", {value: 32});
        Object.defineProperty(this, "N", {value: 624});
        Object.defineProperty(this, "M", {value: 397});
        Object.defineProperty(this, "R", {value: 31});
        Object.defineProperty(this, "U", {value: 11});
        Object.defineProperty(this, "S", {value: 7});
        Object.defineProperty(this, "T", {value: 15});
        Object.defineProperty(this, "L", {value: 18});
        Object.defineProperty(this, "A", {value: 0x9908B0DF});
        Object.defineProperty(this, "B", {value: 0x9D2C5680});
        Object.defineProperty(this, "C", {value: 0xEFC60000});
        Object.defineProperty(this, "seed", {value: seed});

        // ビットマスク用
        Object.defineProperty(this, "WHOLE_MASK", {value: 0xffffffff});
        Object.defineProperty(this, "UPPER_MASK", {value: 0x80000000});
        Object.defineProperty(this, "LOWER_MASK", {value: 0x7fffffff});

        // MT 内部状態
        this.i = 0;
        this.x = [this.seed & this.WHOLE_MASK];

        let a, b, c;

        for (let j = 1; j < this.N; j++) {
            a = this.x[j - 1] ^ (this.x[j - 1] >>> 30);
            b = (1406077 * a & this.WHOLE_MASK) * 1289 & this.WHOLE_MASK;
            c = (b + j) & this.WHOLE_MASK;
            if (c < 0) {
                c += this.WHOLE_MASK + 1;
            }
            this.x.push(c);
        }
        console.log(this.x.slice(this.N - 10));
    }
}