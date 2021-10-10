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
        this.W = 32;
        this.N = 624;
        this.R = 31;
        this.U = 11;
        this.S = 7;
        this.T = 15;
        this.L = 18;
        this.A = 0x9908B0DF;
        this.B = 0x9D2C5680;
        this.C = 0xEFC60000;

        console.log(this.W);
    }
}