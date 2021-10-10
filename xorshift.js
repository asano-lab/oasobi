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
    }
}